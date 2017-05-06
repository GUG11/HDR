import process
import os


if __name__ == '__main__':
    datadir = os.path.join('..', 'data')
    resultdir = os.path.join('..', 'result')
    src_lists = ['Big_City_Lights', 'Hall', 'High_Five', 'Izmir_Harbor', 'The_Marble_Hall']

    for src in src_lists:
        print('processing {}'.format(src))
        process.process(datadir, resultdir, src)
