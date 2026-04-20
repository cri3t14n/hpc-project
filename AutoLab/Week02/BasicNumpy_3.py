import sys
import numpy as np

diagonal = [float(x) for x in sys.argv[1:]]
matrix = np.diag(diagonal)

np.save("matrix.npy", matrix)