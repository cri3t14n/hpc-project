import matplotlib.pyplot as plt

workers = [1, 2, 4, 5, 10]

static_times = [
    697.3322526300326,
    422.019617295824,
    335.2729838839732,
    244.38789928518236,
    133.89653525920585
] 

dynamic_times = [
    605.216198253911,
    329.67688998393714,
    190.29051605099812,
    168.41827539307997,
    125.26284557115287
]
static_speedup = [static_times[0] / t for t in static_times]
dynamic_speedup = [dynamic_times[0] / t for t in dynamic_times]
ideal_speedup = workers

plt.figure()
plt.plot(workers, static_speedup, marker="o", label="Static")
plt.plot(workers, dynamic_speedup, marker="o", label="Dynamic")
plt.plot(workers, ideal_speedup, marker="o", linestyle="--", label="Ideal")

plt.xlabel("Number of workers")
plt.ylabel("Speed-up")
plt.title("Static vs dynamic scheduling speed-up")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("static_dynamic_speedup.png", dpi=200)
plt.show()