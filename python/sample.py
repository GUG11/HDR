""" sample points for estimation
    M: number of images, N: number of points
    we have N + 256 unknown variables, and MN + 256 - 1 functions
    Let
        MN + 256 - 1 > k(N + 256), k \in Z
        (M-k)N > 256k - 255
        N > (256k - 255) / (M - k)

    Let k = M - 1
        N > 256M - 511
"""

import numpy as np

def uniform_grid_sample(imagestack, N=15):
    M = len(imagestack)
    N = max(0, min(20, N));
    m, n, _ = imagestack[0].shape
    # sample ratio
    Rx = int((m - 20) / (N - 1))
    Ry = int((n - 20) / (N - 1))
    points = np.zeros((N*N, M, 3))
    for ch in range(3):
        for k in range(M):
            points[:,k,ch] = imagestack[k][10:-1:Rx, 10:-1:Ry, ch].ravel()
    return points

def random_sample(imagestack, k=1):
    M = len(imagestack)
    N = int(np.ceil(np.sqrt( (256 * k - 255) / (M - k) )))
    m, n, _ = imagestack[0].shape
    # randomly sample N points
    indexes = np.arange(m * n)
    np.random.shuffle(indexes)
    idx_selected = indexes[:N*N]
    points = np.zeros((N*N, M, 3))
    for ch in range(3):
        for k in range(M):
            points[:,k,ch] = imagestack[k][:,:,ch].ravel()[idx_selected]
    return points
