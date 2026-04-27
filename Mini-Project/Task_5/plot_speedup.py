import matplotlib.pyplot as plt

workers = [1, 2, 4, 5, 10]
times = [
    697.3322526300326,
    422.019617295824,
    335.2729838839732,
    244.38789928518236,
    133.89653525920585
] 

speedups = [times[0] / t for t in times]
ideal = workers

plt.figure()
plt.plot(workers, speedups, marker="o", label="Measured")
plt.plot(workers, ideal, marker="o", linestyle="--", label="Ideal")
plt.xlabel("Number of workers")
plt.ylabel("Speed-up")
plt.title("Static scheduling speed-up")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("static_speedup.png", dpi=200)
plt.show()