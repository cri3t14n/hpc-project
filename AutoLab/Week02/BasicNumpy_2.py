import sys
import numpy as np

vector = np.array([float(x) for x in sys.argv[1:]])
print(np.linalg.norm(vector))