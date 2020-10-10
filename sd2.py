import numpy as np
import os
import stroll
import sys
import wavio
from pathlib import Path

FRAMERATE = 44100
ROOT = Path('/Users/tom/Documents/audio/openLoop')
SOURCE = ROOT / 'source'
TARGET = ROOT / 'extracted'
COUNT = 100


def main():
    os.chdir(ROOT)
    i = 0
    for f in stroll.stroll('source', relative=True):
        if f.suffix != '.Sd2f':
            continue

        i += 1
        if i > COUNT:
            break

        target = 'target' / f.with_suffix('.wav')
        source = 'source' / f
        target.parent.mkdir(exist_ok=True, parents=True)
        read(source, str(target))
        print(target.absolute())


def read(infile, outfile):
    samples = np.fromfile(infile, dtype='>i2')
    if len(samples) % 2:
        samples = samples[:-1]

    samples = samples.reshape(len(samples) // 2, 2)
    wavio.write(outfile, samples, FRAMERATE, sampwidth=2, scale='none')


if __name__ == '__main__':
    main()
