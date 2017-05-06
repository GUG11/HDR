import numpy as np
import imageio, util
import os
import matplotlib.pyplot as plt

plt.rc('font', size=30)


def histogram(filedir):
    imagestack, TE = imageio.loadImages2(os.path.join('..', 'data', filedir))
    channels = ['red', 'green', 'blue']

    save_dir = os.path.join('..', 'result', filedir, 'hist')
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for I, te in zip(imagestack, TE):
        print('processing image te={:8.4f}'.format(te))
        fig = plt.figure(num=1, figsize=(20, 12))
        plt.subplot(1, 2, 1)
        plt.imshow(I)
        plt.subplot(1, 2, 2)
        RGB_freqs = []
        for i in range(len(channels)):
            RGB_freqs.append(util.hist_count(I[:,:,i]))
            plt.plot(np.arange(256), RGB_freqs[i], lw=1, color=channels[i])
        plt.xlabel('Intensity')
        plt.ylabel('Freqeuncy')
        plt.tight_layout()
        print(RGB_freqs)
        plt.show()
        fig.savefig(os.path.join(save_dir, 'te_{:8.4f}.svg'.format(te)))
        fig.savefig(os.path.join(save_dir, 'te_{:8.4f}.pdf'.format(te)))


if __name__ == '__main__':
    histogram('example')
