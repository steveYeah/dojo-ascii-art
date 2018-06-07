#!/usr/bin/env python3

import argparse
import sys

import numpy
from PIL import Image


def convert(file, outfile, width):
    image = Image.open(file.name).convert('L')
    import pdb; pdb.set_trace()

    image_width = image.shape[1]
    image_height = image.shape[0]

    int(factor) = image_width / width
    height = image_hight / factor

    image.resize((width, height))
    data = numpy.array(image, dtype="int32" )

    out = []

    for row in data:
        out_line = []
        out.append(out_line)
        for col in row:
            value = chr(col) + 255
            out_line.append(value)

def main(argv):
    parser = argparse.ArgumentParser(
        description="ASCII YEAHHH",
    )

    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('outfile', type=argparse.FileType('w'))
    parser.add_argument('--width', type=int, default=78)


    parsed = parser.parse_args()

    return convert(parsed.file, parsed.outfile, width)


if __name__ == "__main__":
    main(sys.argv)
