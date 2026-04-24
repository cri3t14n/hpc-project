import numpy as np
from numba import cuda
from time import perf_counter


@cuda.jit
def add_kernel(x, y, a):
    i = cuda.grid(1)
    if i < len(a):
        a[i] = x[i] + y[i]


def main():
    n = 1_000_000

    x = np.random.rand(n).astype(np.float32)
    y = np.random.rand(n).astype(np.float32)
    a = np.empty_like(x)

    d_x = cuda.to_device(x)
    d_y = cuda.to_device(y)
    d_a = cuda.device_array_like(x)

    tpb = 256
    bpg = (n + tpb - 1) // tpb

    # Warm-up / JIT compile
    add_kernel[bpg, tpb](d_x, d_y, d_a)
    cuda.synchronize()

    t0 = perf_counter()
    add_kernel[bpg, tpb](d_x, d_y, d_a)
    cuda.synchronize()
    elapsed = perf_counter() - t0

    d_a.copy_to_host(a)

    print(elapsed)


if __name__ == "__main__":
    main()