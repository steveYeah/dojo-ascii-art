#!/usr/bin/env python3

import argparse
import sys

import numpy
from PIL import Image


def convert(file, outfile):
    image = Image.open(file.name).convert('L')
    data = numpy.array(image, dtype="int32" )
    import pdb; pdb.set_trace()


def main(argv):
    parser = argparse.ArgumentParser(
        description="ASCII YEAHHH",
        )

    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('outfile', type=argparse.FileType('w'))
    

    parsed = parser.parse_args()

    return convert(parsed.file, parsed.outfile)


if __name__ == "__main__":
    main(sys.argv)
