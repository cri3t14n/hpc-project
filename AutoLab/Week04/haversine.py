import sys
import numpy as np


# @profile
def distance_matrix(p1, p2):
    p1, p2 = np.radians(p1), np.radians(p2)

    D = np.empty((len(p1), len(p2)))
    for i in range(len(p1)):
        for j in range(len(p2)):
            dsin2 = np.sin(0.5 * (p1[i] - p2[j])) ** 2
            cosprod = np.cos(p1[i, 0]) * np.cos(p2[j, 0])
            a = dsin2[0] + cosprod * dsin2[1]
            D[i, j] = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    D *= 6371  # Earth radius in km
    return D

# @profile
def distance_matrix_one_loop(p1, p2):
    p1, p2 = np.radians(p1), np.radians(p2)

    cos_p2 = np.cos(p2[:, 0])

    D = np.empty((len(p1), len(p2)))
    for i in range(len(p1)):
        dsin2 = np.sin(0.5 * (p1[i] - p2)) ** 2
        cosprod = np.cos(p1[i, 0]) * cos_p2
        a = dsin2[:, 0] + cosprod * dsin2[:, 1]
        D[i, :] = 2 * np.arcsin(np.sqrt(a))

    D *= 6371  # Earth radius in km
    return D


@profile
def distance_matrix_no_loop(p1, p2):
    p1, p2 = np.radians(p1), np.radians(p2)

    lat1 = p1[:, 0][:, None]
    lon1 = p1[:, 1][:, None]
    lat2 = p2[:, 0][None, :]
    lon2 = p2[:, 1][None, :]

    dlat = lat1 - lat2
    dlon = lon1 - lon2

    dsin2_lat = np.sin(0.5 * dlat) ** 2
    dsin2_lon = np.sin(0.5 * dlon) ** 2

    a = dsin2_lat + np.cos(lat1) * np.cos(lat2) * dsin2_lon
    D = 2 * np.arcsin(np.sqrt(a))

    D *= 6371  # Earth radius in km
    return D

def load_points(fname):
    data = np.loadtxt(fname, delimiter=',', skiprows=1, usecols=(1, 2))
    return data


def distance_stats(D):
    # Extract upper triangular part to avoid duplicate entries
    assert D.shape[0] == D.shape[1], 'D must be square'
    idx = np.triu_indices(D.shape[0], k=1)
    distances = D[idx]
    return {
        'mean': float(distances.mean()),
        'std': float(distances.std()),
        'max': float(distances.max()),
        'min': float(distances.min()),
    }


fname = sys.argv[1]
points = load_points(fname)
D = distance_matrix_no_loop(points, points)
stats = distance_stats(D)
print(stats)