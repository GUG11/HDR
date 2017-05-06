import numpy as np
import imageio, alignment, sample, gsolve
import os
import tonemap
import util
import matplotlib.pyplot as plt
import scipy.io as sio
from scipy.misc import imsave


def process(datadir, resultdir, source_name):
    filepath = os.path.join(datadir, source_name)
    savepath_exp = os.path.join(resultdir, source_name + '_ex.jpg')
    savepath_final = os.path.join(resultdir, source_name + '.jpg')
    # if os.path.exists(savepath_final):
    if False:
         print('{} already processed'.format(source_name))
    else:
        print('load images')
        imagestack, exposure_times = imageio.loadImages2(filepath)
        index = [i[0] for i in sorted(enumerate(exposure_times), key=lambda x:x[1])]
        exposure_times = [exposure_times[i] for i in index]
        imagestack = [imagestack[i] for i in index]
        print(exposure_times)

        # alignment
        print('align images')
        is_aligned = [imagestack[0]]
        shifts = []
        for i in range(1, len(imagestack)):
            print('align image {}'.format(i))
            Treg, shift = alignment.align_two_images(is_aligned[i-1], imagestack[i])
            #is_aligned.append(Treg)
            is_aligned.append(imagestack[i])
            shifts.append(shift)
        print(shifts)
        shifts = np.array(shifts)
        margin = np.max(shifts, axis=0)
        assert np.all(margin < 20)
        # for i in range(len(is_aligned)):
        #    is_aligned[i] = util.crop_image(is_aligned[i], np.array(is_aligned[i].shape[:2]) - margin)
        print('margin:{}'.format(margin))
        print('new image size:{}'.format(is_aligned[0].shape))

        # sample points
        points = sample.uniform_grid_sample(is_aligned, N=20)

        I = np.array(is_aligned)

        # recon
        print('estimate exposure')
        lmd = 2
        ln_te = np.log(exposure_times)
        gs = [gsolve.gsolve(points[:,:,i], ln_te, lmd)[0] for i in range(3)]

        lnE = gsolve.hdr_recon(gs, I, ln_te)

        E = np.exp(lnE)
        """f, axs = plt.subplots(1, 3)
        channel_names = ('red', 'green', 'blue')
        for i in range(3):
            cax = axs[i].imshow(lnE[:,:,i], cmap='gray')
            axs[i].set_title(channel_names[i])
            axs[i].axis('off')
        cbar = f.colorbar(cax, orientation='horizontal', ax=axs.ravel().tolist(), aspect=40)
        plt.show()"""
        # param
        print('tone mapping')
        l_remap = (0, 1)
        saturation = 2.
        numtiles = (4, 4)
        I = tonemap.tonemap(E, l_remap=l_remap, saturation=saturation, numtiles=numtiles)
        plt.imshow(I)
        plt.show()
        imsave(savepath_final, I)
