import sys
import numpy as np
import cupy as cp


def distance_matrix_oneloop(p1, p2):
    p1 = cp.asarray(p1)
    p2 = cp.asarray(p2)

    p1, p2 = cp.radians(p1), cp.radians(p2)

    cos_p2 = cp.cos(p2[:, 0])

    D = cp.empty((len(p1), len(p2)), dtype=cp.float64)
    for i in range(len(p1)):
        dsin2 = cp.sin(0.5 * (p1[i] - p2)) ** 2
        cosprod = cp.cos(p1[i, 0]) * cos_p2
        a = dsin2[:, 0] + cosprod * dsin2[:, 1]
        D[i, :] = 2 * cp.arcsin(cp.sqrt(a))

    D *= 6371
    return D


def distance_matrix_noloop(p1, p2):
    p1 = cp.asarray(p1)
    p2 = cp.asarray(p2)

    p1, p2 = cp.radians(p1), cp.radians(p2)

    lat1 = p1[:, 0][:, None]
    lon1 = p1[:, 1][:, None]
    lat2 = p2[:, 0][None, :]
    lon2 = p2[:, 1][None, :]

    dlat = lat1 - lat2
    dlon = lon1 - lon2

    dsin2_lat = cp.sin(0.5 * dlat) ** 2
    dsin2_lon = cp.sin(0.5 * dlon) ** 2

    a = dsin2_lat + cp.cos(lat1) * cp.cos(lat2) * dsin2_lon
    D = 2 * cp.arcsin(cp.sqrt(a))

    D *= 6371
    return D


def load_points(fname):
    return np.loadtxt(fname, delimiter=",", skiprows=1, usecols=(1, 2))


def distance_stats(D):
    assert D.shape[0] == D.shape[1], "D must be square"
    idx = cp.triu_indices(D.shape[0], k=1)
    distances = D[idx]
    return {
        "mean": float(cp.asnumpy(distances.mean())),
        "std": float(cp.asnumpy(distances.std())),
        "max": float(cp.asnumpy(distances.max())),
        "min": float(cp.asnumpy(distances.min())),
    }


fname = sys.argv[1]
points = load_points(fname)

# D = distance_matrix_one_loop(points, points)
D = distance_matrix_no_loop(points, points)

stats = distance_stats(D)
print(stats)