import sys
from os.path import dirname, abspath, join
from time import perf_counter

import numpy as np
from numba import cuda

HERE = dirname(abspath(__file__))
PARENT = dirname(HERE)
sys.path.insert(0, PARENT)

from simulate import load_data, summary_stats


LOAD_DIR = "/dtu/projects/02613_2025/data/modified_swiss_dwellings/"
MAX_ITER = 20_000


@cuda.jit
def jacobi_step(u_old, u_new, interior_mask):
    i, j = cuda.grid(2)

    if i < interior_mask.shape[0] and j < interior_mask.shape[1]:
        ui = i + 1
        uj = j + 1

        if interior_mask[i, j]:
            u_new[ui, uj] = 0.25 * (u_old[ui, uj-1] + u_old[ui, uj+1] + u_old[ui-1, uj] + u_old[ui+1, uj])
        else:
            u_new[ui, uj] = u_old[ui, uj]


def jacobi_cuda(u, interior_mask, max_iter):
    d_u_old = cuda.to_device(u)
    d_u_new = cuda.to_device(u)
    d_mask = cuda.to_device(interior_mask)

    tpb = (16, 16)
    bpg = (
        (interior_mask.shape[0] + tpb[0] - 1) // tpb[0],
        (interior_mask.shape[1] + tpb[1] - 1) // tpb[1],
    )

    for _ in range(max_iter):
        jacobi_step[bpg, tpb](d_u_old, d_u_new, d_mask)
        d_u_old, d_u_new = d_u_new, d_u_old

    return d_u_old.copy_to_host()


def main():
    with open(join(LOAD_DIR, "building_ids.txt"), "r") as f:
        building_ids = f.read().splitlines()

    N = int(sys.argv[1])

    building_ids = building_ids[:N]

    # Warm up CUDA compilation once
    u0, interior_mask = load_data(LOAD_DIR, building_ids[0])
    _ = jacobi_cuda(u0, interior_mask, 1)
    cuda.synchronize()

    t0 = perf_counter()

    all_results = []
    for bid in building_ids:
        u0, interior_mask = load_data(LOAD_DIR, bid)
        u = jacobi_cuda(u0, interior_mask, MAX_ITER)
        stats = summary_stats(u, interior_mask)
        all_results.append((bid, stats))

    cuda.synchronize()
    elapsed = perf_counter() - t0

    stat_keys = ["mean_temp", "std_temp", "pct_above_18", "pct_below_15"]
    print("building_id, " + ", ".join(stat_keys))
    for bid, stats in all_results:
        print(f"{bid},", ", ".join(str(stats[k]) for k in stat_keys))

    print(f"\nelapsed_seconds,{elapsed}")


if __name__ == "__main__":
    main()