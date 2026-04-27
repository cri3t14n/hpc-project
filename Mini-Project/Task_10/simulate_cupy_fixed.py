import sys
from os.path import dirname, abspath, join
from time import perf_counter

import numpy as np
import cupy as cp

HERE = dirname(abspath(__file__))
PARENT = dirname(HERE)
sys.path.insert(0, PARENT)

from simulate import load_data, summary_stats  


LOAD_DIR = "/dtu/projects/02613_2025/data/modified_swiss_dwellings/"
MAX_ITER = 20_000

jacobi_kernel = cp.RawKernel(r'''
extern "C" __global__
void jacobi_step(const float* u_old,
                 float* u_new,
                 const bool* mask,
                 int nrows,
                 int ncols)
{
    int i = blockDim.y * blockIdx.y + threadIdx.y;
    int j = blockDim.x * blockIdx.x + threadIdx.x;

    if (i < nrows - 2 && j < ncols - 2) {
        int ui = i + 1;
        int uj = j + 1;

        int idx_full = ui * ncols + uj;
        int idx_mask = i * (ncols - 2) + j;

        if (mask[idx_mask]) {
            u_new[idx_full] = 0.25f * (u_old[ui * ncols + (uj-1)] + u_old[ui * ncols + (uj+1)] + u_old[(ui-1) * ncols + uj] + u_old[(ui+1) * ncols + uj]);
        } else {
            u_new[idx_full] = u_old[idx_full];
        }
    }
}
''', 'jacobi_step')


def jacobi_cupy_raw(u, interior_mask, max_iter):
    u_old = cp.asarray(u, dtype=cp.float32)
    u_new = cp.asarray(u, dtype=cp.float32)
    mask = cp.asarray(interior_mask.ravel(), dtype=cp.bool_)

    nrows, ncols = u.shape

    threads = (16, 16, 1)
    blocks = (
        (ncols - 2 + threads[0] - 1) // threads[0],
        (nrows - 2 + threads[1] - 1) // threads[1],
        1
    )

    for _ in range(max_iter):
        jacobi_kernel(
            blocks, threads,
            (u_old, u_new, mask, np.int32(nrows), np.int32(ncols))
        )
        u_old, u_new = u_new, u_old

    return cp.asnumpy(u_old)


def main():
    with open(join(LOAD_DIR, "building_ids.txt"), "r") as f:
        building_ids = f.read().splitlines()

    N = int(sys.argv[1])
    building_ids = building_ids[:N]

    u0, interior_mask = load_data(LOAD_DIR, building_ids[0])
    _ = jacobi_cupy_raw(u0, interior_mask, 1)
    cp.cuda.Stream.null.synchronize()

    t0 = perf_counter()

    all_results = []
    for bid in building_ids:
        u0, interior_mask = load_data(LOAD_DIR, bid)
        u = jacobi_cupy_raw(u0, interior_mask, MAX_ITER)
        stats = summary_stats(u, interior_mask)
        all_results.append((bid, stats))

    cp.cuda.Stream.null.synchronize()
    elapsed = perf_counter() - t0

    stat_keys = ["mean_temp", "std_temp", "pct_above_18", "pct_below_15"]
    print("building_id," + ",".join(stat_keys))
    for bid, stats in all_results:
        print(f"{bid}," + ",".join(str(stats[k]) for k in stat_keys))

    print(f"elapsed_seconds,{elapsed}", file=sys.stderr)




if __name__ == "__main__":
    main()