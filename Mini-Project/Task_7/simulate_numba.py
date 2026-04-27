import sys
from os.path import dirname, abspath, join
from time import perf_counter

import numpy as np
from numba import jit


HERE = dirname(abspath(__file__))
PARENT = dirname(HERE)
sys.path.insert(0, PARENT)

from simulate import load_data, summary_stats  # noqa: E402


LOAD_DIR = "/dtu/projects/02613_2025/data/modified_swiss_dwellings/"
MAX_ITER = 20_000
ABS_TOL = 1e-4

@jit(nopython=True)
def jacobi_jit(u, interior_mask, max_iter, atol=1e-6):
    u_old = np.copy(u)
    u_new = np.copy(u)

    nrows, ncols = u.shape

    for _ in range(max_iter):
        delta = 0.0

        for i in range(1, nrows - 1):
            for j in range(1, ncols - 1):
                if interior_mask[i - 1, j - 1]:
                    new_val = 0.25 * (u_old[i, j-1] + u_old[i, j+1] + u_old[i-1, j] + u_old[i+1, j])

                    diff = abs(u_old[i, j] - new_val)
                    if diff > delta:
                        delta = diff

                    u_new[i, j] = new_val
                else:
                    u_new[i, j] = u_old[i, j]

        if delta < atol:
            return u_new

        tmp = u_old
        u_old = u_new
        u_new = tmp

    return u_old


def main():
    with open(join(LOAD_DIR, "building_ids.txt"), "r") as f:
        building_ids = f.read().splitlines()

    N = int(sys.argv[1])

    building_ids = building_ids[:N]

    # Warm up JIT compilation
    u0, interior_mask = load_data(LOAD_DIR, building_ids[0])
    _ = jacobi_jit(u0, interior_mask, 1, ABS_TOL)

    t0 = perf_counter()

    all_results = []
    for bid in building_ids:
        u0, interior_mask = load_data(LOAD_DIR, bid)
        u = jacobi_jit(u0, interior_mask, MAX_ITER, ABS_TOL)
        stats = summary_stats(u, interior_mask)
        all_results.append((bid, stats))

    elapsed = perf_counter() - t0

    stat_keys = ["mean_temp", "std_temp", "pct_above_18", "pct_below_15"]
    print("building_id, " + ", ".join(stat_keys))
    for bid, stats in all_results:
        print(f"{bid},", ", ".join(str(stats[k]) for k in stat_keys))

    print(f"\nelapsed_seconds,{elapsed}")


if __name__ == "__main__":
    main()