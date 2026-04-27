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
ABS_TOL = 1e-4

def jacobi_cupy(u, interior_mask, max_iter, atol=1e-6):
    u_gpu = cp.asarray(u)
    mask_gpu = cp.asarray(interior_mask)

    for _ in range(max_iter):
        u_new = 0.25 * (u_gpu[1:-1, :-2] + u_gpu[1:-1, 2:] + u_gpu[:-2, 1:-1] + u_gpu[2:, 1:-1])
        u_new_interior = u_new[mask_gpu]
        delta = cp.abs(u_gpu[1:-1, 1:-1][mask_gpu] - u_new_interior).max()
        u_gpu[1:-1, 1:-1][mask_gpu] = u_new_interior

        if delta < atol:
            break

    return cp.asnumpy(u_gpu)


def main():
    with open(join(LOAD_DIR, "building_ids.txt"), "r") as f:
        building_ids = f.read().splitlines()

    N = int(sys.argv[1])

    building_ids = building_ids[:N]

    # Warm up CuPy once
    u0, interior_mask = load_data(LOAD_DIR, building_ids[0])
    _ = jacobi_cupy(u0, interior_mask, 1, ABS_TOL)
    cp.cuda.Stream.null.synchronize()

    t0 = perf_counter()

    all_results = []
    for bid in building_ids:
        u0, interior_mask = load_data(LOAD_DIR, bid)
        u = jacobi_cupy(u0, interior_mask, MAX_ITER, ABS_TOL)
        stats = summary_stats(u, interior_mask)
        all_results.append((bid, stats))

    cp.cuda.Stream.null.synchronize()
    elapsed = perf_counter() - t0

    stat_keys = ["mean_temp", "std_temp", "pct_above_18", "pct_below_15"]
    print("building_id, " + ", ".join(stat_keys))
    for bid, stats in all_results:
        print(f"{bid},", ", ".join(str(stats[k]) for k in stat_keys))

    print(f"\nelapsed_seconds,{elapsed}")



if __name__ == "__main__":
    main()