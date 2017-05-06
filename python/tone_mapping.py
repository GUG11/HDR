import numpy as np
from fastbilateral import gpa

import util

def tone_mapping(E, scale, offset, gamma=0.5):
    """
        tone mapping based on fast bilateral
        @param E: exposure
        @param scale: scale of the contrast reduction
        @param offset:
        return HDR image
    """
    chrome_weights = np.array([20.0, 40.0, 1.0]) / 61.0
    G = E[:,:,0] * chrome_weights[0] + E[:,:,1] * chrome_weights[1] + E[:,:,2] * chrome_weights[2]
    color_shares = [E[:,:,i] / G for i in range(3)]
    L = np.log2(G)
    L = util.rescale(L, (0.0, 255.0))
    sigmar = 40 #(np.max(L) - np.min(L)) / 30
    rough = gpa(L, sigmas=5, sigmar=sigmar, eps=0.1)
    detail = L - rough
    I_reduced = (rough - offset) * scale
    I_new = I_reduced + detail
    # I_new = np.exp(I_reduced + detail)
    In = (I_new - np.min(I_new)) / (np.max(I_new) - np.min(I_new))
    In = In ** gamma
    I = np.zeros_like(E)
    for ch in range(3):
        I[:,:,ch] = In * color_shares[ch]
    return I
