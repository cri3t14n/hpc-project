import sys
import numpy as np
from time import perf_counter

matrix = np.load(sys.argv[1])
p = int(sys.argv[2])

start = perf_counter()

result = matrix.copy()
for _ in range(p):
    result = result @ matrix

end = perf_counter()

np.save("result.npy", result)
print(end - start)