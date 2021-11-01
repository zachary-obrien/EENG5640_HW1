import numpy as np


def get_z(point):
    (x, y) = point
    z = x + y * 1j
    return z


def get_fft(k, point_array):
    N = len(point_array)
    summation = 0
    for n in range(N):
        z = get_z(point_array[n])
        exponent = (-1j * 2 * np.pi * k * n) / N
        inner = z * np.exp(exponent)
        summation = summation + inner
    return summation


def get_fk(point_array):
    f_k_vals = []
    for k in range(len(point_array)):
        f_k = get_fft(k, point_array)
        f_k_vals.append(f_k)
    return f_k_vals


def get_ck(point_array):
    f_k_vals = get_fk(point_array)
    f_0 = f_k_vals[0]
    f_1 = f_k_vals[1]
    c_k = {}
    for f_k in range(2, len(f_k_vals)):
        c_k[f_k - 2] = np.abs(f_k_vals[f_k]) / np.abs(f_1)
    return c_k


points1 = [(3, 3), (4, 4), (4, 5), (4, 6), (5, 6), (6, 5), (6, 4), (7, 3), (6, 2), (5, 2), (4, 2)]

points2 = [(0, 2), (0, 4), (2, 4), (3, 5), (4, 6), (5, 5), (5, 3), (4, 2), (4, 0), (2, 0), (1, 1)]

c_k_1 = get_ck(points1)
print(c_k_1)

c_k_2 = get_ck(points2)
print(c_k_2)
