import sys
import numpy as np

matrix = np.load(sys.argv[1])

cols = np.mean(matrix, axis=0)
rows = np.mean(matrix, axis=1)

np.save("cols.npy", cols)
np.save("rows.npy", rows)