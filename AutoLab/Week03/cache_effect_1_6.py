import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt

# At least 100 repetitions
REPS = 200
sizes = np.unique(np.logspace(2, 8, num=30, dtype=int))

perf = []
sizes_kb = []

for SIZE in sizes:
    mat = np.random.rand(1, SIZE)

    # Warm-up
    _ = 2 * mat[0, :]

    start = perf_counter()
    for _ in range(REPS):
        x = 2 * mat[0, :]
    end = perf_counter()

    elapsed = end - start

    # One multiply per element
    mflops = (REPS * SIZE) / elapsed / 1e6
    size_kb = mat.nbytes / 1024

    perf.append(mflops)
    sizes_kb.append(size_kb)

    print(f"SIZE={SIZE:10d}, size={size_kb:12.2f} KB, perf={mflops:12.2f} MFLOP/s")

perf = np.array(perf)
sizes_kb = np.array(sizes_kb)

np.savez(
    "row_vector_scaling.npz",
    sizes=sizes,
    sizes_kb=sizes_kb,
    perf=perf,
)

plt.figure()
plt.loglog(sizes_kb, perf, "o-")
plt.xlabel("Row vector size [KB]")
plt.ylabel("Performance [MFLOP/s]")
plt.title("Row scaling performance")
plt.grid(True, which="both")
plt.tight_layout()
plt.savefig("row_vector_scaling.png", dpi=200)
plt.show()