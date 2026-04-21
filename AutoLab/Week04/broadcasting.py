import numpy as np


def standardize_rows(data, mean, std):
    return (data - mean) / std


def outer(x, y):
    return np.array([[xi * yj for yj in y] for xi in x])


def distmat_1d(x, y):
    return abs(x[:, None] - y[None, :])