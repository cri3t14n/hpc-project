import sys
import numpy as np

def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if abs(z) > 2.0:
            return i
    return 100

N = int(sys.argv[1])

xmin, xmax = -2, 2
ymin, ymax = -2, 2

x_values = np.linspace(xmin, xmax, N)
y_values = np.linspace(ymin, ymax, N)

arr = np.memmap("mandelbrot.raw", dtype="int32", mode="w+", shape=(N, N))

for i, x in enumerate(x_values):
    for j, y in enumerate(y_values):
        arr[i, j] = mandelbrot_escape_time(complex(x, y))

arr.flush()