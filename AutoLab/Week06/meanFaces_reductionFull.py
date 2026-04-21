import ctypes
import multiprocessing as mp
import sys
from time import perf_counter as time
import numpy as np
from PIL import Image


def init(shared_arr_):
    global shared_arr
    shared_arr = shared_arr_


def tonumpyarray(mp_arr):
    return np.frombuffer(mp_arr, dtype='float32')


def reduce_step(args):
    b, e, s, elemshape = args
    arr = tonumpyarray(shared_arr).reshape((-1,) + elemshape)
    arr[b:e:s] += arr[b + s:e + s:s]


if __name__ == '__main__':
    n_processes = 1

    data = np.load(sys.argv[1])
    n_images = len(data)
    elemshape = data.shape[1:]

    shared_arr = mp.RawArray(ctypes.c_float, data.size)
    arr = tonumpyarray(shared_arr).reshape(data.shape)
    np.copyto(arr, data)
    del data

    t = time()
    pool = mp.Pool(n_processes, initializer=init, initargs=(shared_arr,))

    step = 1
    while step < n_images:
        pool.map(
            reduce_step,
            [
                (i, i + 1, step, elemshape)
                for i in range(0, n_images - step, 2 * step)
            ],
            chunksize=1
        )
        step *= 2

    final_image = arr[0] / n_images

    print(time() - t)

    Image.fromarray(
        (255 * final_image.astype(float)).astype('uint8')
    ).save('result.png')