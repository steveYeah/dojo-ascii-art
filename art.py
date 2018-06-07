#!/usr/bin/env python3

import argparse
import sys

import numpy
from PIL import Image


def convert(file, width):
    image = Image.open(file.name).convert('L')

    factor = image.width // width
    height = image.height // factor

    image = image.resize((width, height))
    data = numpy.array(image, dtype="int32")

    out = []

    for row in data:
        out_line = []
        out.append(out_line)
        for col in row:
            value = chr(col + 255)
            out_line.append(value)

    for line in out:
        print(''.join(line))


def main(argv):
    parser = argparse.ArgumentParser(
        description="ASCII YEAHHH",
    )

    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--width', type=int, default=78)


    parsed = parser.parse_args()

    return convert(parsed.file, parsed.width)


if __name__ == "__main__":
    main(sys.argv)
