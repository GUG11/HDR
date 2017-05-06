import numpy as np
import imageio, alignment, sample, gsolve
import os
import tonemap
import util
import matplotlib.pyplot as plt
import scipy.io as sio
from scipy.misc import imsave

import process


if __name__ == '__main__':
    datadir = os.path.join('..', 'data')
    resultdir = os.path.join('..', 'result')
    source_name = 'Big_City_Lights'

    process.process(datadir, resultdir, source_name)
