import numpy as np
import time


def w_mid(z):
    return 1 - np.abs(z - 128.0) / 130.0

def gsolve(points, ln_te, lmd, weight_fcn=w_mid):
    """
        @params points: N x M N - number of points M - number of images
    """
    N, M = points.shape
    nlevels = 256  # [0, 255]
    A = np.zeros((N * M + nlevels - 1, nlevels + N))
    b = np.zeros(A.shape[0])
    print('system size:{}'.format(A.shape))
    t_s = time.time()

    k = 0
    for i in range(N):
        for j in range(M):
            wij = weight_fcn(points[i, j])
            A[k, int(points[i, j])] = wij
            A[k, nlevels + i] = -wij
            b[k] = wij * ln_te[j]
            k += 1

    A[k, 128] = 1   # Fix the curve by setting its middle value to 0
    k += 1

    for i in range(nlevels-2):
        wi = weight_fcn(i)
        A[k, i] = lmd * wi
        A[k, i+1] = -2 * lmd * wi
        A[k, i+2] = lmd * wi
        k += 1

    x, _, _, _ = np.linalg.lstsq(A, b)
    g = x[:nlevels]
    lnE = x[nlevels:]
    t_e = time.time()
    print('estimate time:{}'.format(t_e - t_s))

    return g, lnE


def hdr_recon(g, I, ln_te, weight_fcn=w_mid):
    lnE = np.zeros(I[0].shape)
    ln_te_mat = np.array([np.tile(ln_te[i], I.shape[1:-1]) for i in range(I.shape[0])])
    for ch in range(3):
        weighted_sum = np.sum(weight_fcn(I[:,:,:,ch]) * (g[ch][I[:,:,:,ch]] - ln_te_mat), axis=0)
        weight_sum = np.sum(weight_fcn(I[:,:,:,ch]), axis=0)
        lnE[:,:,ch] = weighted_sum / weight_sum
    return lnE
