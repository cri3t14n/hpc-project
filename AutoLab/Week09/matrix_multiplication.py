import numpy as np
from numba import jit
from time import perf_counter


def matmul(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i, j] += A[i, k] * B[k, j]
    return C


@jit(nopython=True)
def matmul_jit(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    for k in range(A.shape[0]):
        for i in range(B.shape[1]):
            for j in range(A.shape[1]):
                C[i, j] += A[i, k] * B[k, j]
    return C


A = np.random.rand(100, 100)
B = np.random.rand(100, 100)

# Warm up JIT
matmul_jit(A, B)

t0 = perf_counter()
C1 = matmul(A, B)
t_python = perf_counter() - t0

t0 = perf_counter()
C2 = matmul_jit(A, B)
t_jit = perf_counter() - t0

speedup = t_python / t_jit

print("Python time:", t_python)
print("JIT time:", t_jit)
print("Speedup:", speedup)
print("Same result:", np.allclose(C1, C2))