from scipy import misc
import os
import re

def loadImages(filedir):
    filenames = os.listdir(filedir)
    imagestack = []
    exposure_times = []
    file_pattern = re.compile('room_([\d]+)(_([\d]+))*\.[\w]+')
    for filename in filenames:
        filepath = os.path.join(filedir, filename)
        imagestack.append(misc.imread(filepath))
        m = file_pattern.match(filename)
        if m.group(3) is not None:
            exposure_times.append(float(m.group(1)) / float(m.group(3)))
        else:
            exposure_times.append(float(m.group(1)))
    return imagestack, exposure_times


def loadImages2(filedir, capture_info='exposure.info'):
    filenames = os.listdir(filedir)
    filenames.remove(capture_info)
    imagestack = []
    exposure_times = []
    # fetch capture info
    with open(os.path.join(filedir, capture_info)) as f:
        content = f.read()

    for filename in filenames:
        filepath = os.path.join(filedir, filename)
        S = re.search('{}\s+([\d\./]+)'.format(filename), content)
        print('load file:{}, exposure time:{:8.4f}'.format(filename, 1.0 / eval(S.group(1))))
        imagestack.append(misc.imread(filepath))
        exposure_times.append(1.0 / eval(S.group(1)))

    return imagestack, exposure_times
