import numpy as np
import util


def align_two_images(R, T):
    """
    align two images
    @param R: reference
    @param T: target
    register T to R
    return registered image of T
    """
    shift = estimate_translation(R, T)
    Rt = translate(T, shift)
    return Rt, shift

def estimate_translation(R, T, max_size=1024):
    """
        estimate translation
        T(x,y) = R(x - dx, y - dy)
        motion vector (dx, dy)
    """
    Rcrop = util.crop_image(R, (max_size, max_size))
    Tcrop = util.crop_image(T, (max_size, max_size))
    rgb2gray = lambda x: (0.2125 * x[:,:,0] + 0.7154 * x[:,:,1] + 0.0721 * x[:,:,2])
    if len(R.shape) == 3 and R.shape[2] == 3:
        Rg = rgb2gray(Rcrop)
        Tg = rgb2gray(Tcrop)
    elif len(R.shape) == 2:
        Rg = R
        Tg = T
    else:
        raise RuntimeError("Invalid image size!")

    # FFT
    Fr = np.fft.fft2(Rg)
    Ft = np.fft.fft2(Tg)
    Fc = Fr * np.conj(Ft)
    Rc = Fc / np.abs(Fc)
    r = np.fft.ifft2(Rc)
    # get the peak
    max_r = np.max(r)
    max_index = np.argmax(r)
    shift = list(np.unravel_index(max_index, r.shape))
    for i in range(2):
        if r.shape[i] / 2 <= shift[i]:
            shift[i] -= r.shape[i]
    return shift

def translate(T, shift):
    Rt = np.roll(T, shift=shift[0], axis=0)
    Rt = np.roll(T, shift=shift[1], axis=1)
    return Rt
