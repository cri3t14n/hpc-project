import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt

REPS = 2000

# Logarithmically spaced sizes
sizes = np.unique(np.logspace(1, 4, num=25, dtype=int))

row_perf = []
col_perf = []
matrix_sizes_kb = []

for SIZE in sizes:
    mat = np.random.rand(SIZE, SIZE)

    # Warm-up
    _ = 2 * mat[:, 0]
    _ = 2 * mat[0, :]

    # Time column doubling
    start = perf_counter()
    for _ in range(REPS):
        x = 2 * mat[:, 0]
    end = perf_counter()
    col_time = end - start

    # Time row doubling
    start = perf_counter()
    for _ in range(REPS):
        x = 2 * mat[0, :]
    end = perf_counter()
    row_time = end - start

    # MFLOP/s: SIZE multiplications per repetition
    col_mflops = (REPS * SIZE) / col_time / 1e6
    row_mflops = (REPS * SIZE) / row_time / 1e6

    col_perf.append(col_mflops)
    row_perf.append(row_mflops)

    matrix_kb = SIZE * SIZE * 8 / 1024
    matrix_sizes_kb.append(matrix_kb)

    print(f"SIZE={SIZE:5d}, matrix={matrix_kb:10.2f} KB, "
          f"col={col_mflops:10.2f} MFLOP/s, row={row_mflops:10.2f} MFLOP/s")

matrix_sizes_kb = np.array(matrix_sizes_kb)
col_perf = np.array(col_perf)
row_perf = np.array(row_perf)
ratio = row_perf / col_perf

# Save raw data
np.savez(
    "cache_scaling_results.npz",
    sizes=sizes,
    matrix_sizes_kb=matrix_sizes_kb,
    col_perf=col_perf,
    row_perf=row_perf,
    ratio=ratio,
)

# Plot 1: performance
plt.figure()
plt.loglog(matrix_sizes_kb, col_perf, "o-", label="Column doubling")
plt.loglog(matrix_sizes_kb, row_perf, "o-", label="Row doubling")
plt.xlabel("Matrix size [KB]")
plt.ylabel("Performance [MFLOP/s]")
plt.title("Cache effects: row vs column doubling")
plt.legend()
plt.grid(True, which="both")
plt.tight_layout()
plt.savefig("cache_performance.png", dpi=200)

# Plot 2: ratio
plt.figure()
plt.semilogx(matrix_sizes_kb, ratio, "o-")
plt.xlabel("Matrix size [KB]")
plt.ylabel("Row / Column MFLOP/s")
plt.title("Performance ratio")
plt.grid(True, which="both")
plt.tight_layout()
plt.savefig("cache_ratio.png", dpi=200)