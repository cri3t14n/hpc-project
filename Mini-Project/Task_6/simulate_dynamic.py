import sys
from os.path import dirname, abspath, join
from time import perf_counter
import multiprocessing as mp

HERE = dirname(abspath(__file__))
PARENT = dirname(HERE)
sys.path.insert(0, PARENT)

from simulate import load_data, jacobi, summary_stats 


LOAD_DIR = "/dtu/projects/02613_2025/data/modified_swiss_dwellings/"
MAX_ITER = 20_000
ABS_TOL = 1e-4


def process_one_floorplan(bid):
    u0, interior_mask = load_data(LOAD_DIR, bid)
    u = jacobi(u0, interior_mask, MAX_ITER, ABS_TOL)
    stats = summary_stats(u, interior_mask)
    return bid, stats


def main():
    N = int(sys.argv[1])
    n_workers = int(sys.argv[2])

    with open(join(LOAD_DIR, "building_ids.txt"), "r") as f:
        building_ids = f.read().splitlines()

    building_ids = building_ids[:N]

    t0 = perf_counter()

    with mp.Pool(processes=n_workers) as pool:
        results = list(pool.imap_unordered(process_one_floorplan, building_ids, chunksize=1))

    elapsed = perf_counter() - t0

    order = {bid: i for i, bid in enumerate(building_ids)}
    results.sort(key=lambda x: order[x[0]])

    stat_keys = ["mean_temp", "std_temp", "pct_above_18", "pct_below_15"]
    print("building_id, " + ", ".join(stat_keys))
    for bid, stats in results:
        print(f"{bid},", ", ".join(str(stats[k]) for k in stat_keys))

    print(f"\nworkers,{n_workers}")
    print(f"N,{N}")
    print(f"elapsed_seconds,{elapsed}")


if __name__ == "__main__":
    main()