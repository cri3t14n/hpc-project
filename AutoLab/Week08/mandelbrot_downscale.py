import sys
import numpy as np
from PIL import Image

path = sys.argv[1]
N = int(sys.argv[2])
n = int(sys.argv[3])

arr = np.memmap(path, dtype="int32", mode="r", shape=(N, N))
downsampled = np.array(arr[::n, ::n])

img = (255 * downsampled.astype(float) / downsampled.max()).astype("uint8")
Image.fromarray(img).save("result.png")