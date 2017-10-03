#!/usr/bin/env python
# code adapted from https://pjreddie.com/projects/mnist-in-csv/

from __future__ import print_function
import sys

def convert(f, l, o, n):
    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        image = [ord(l.read(1))]
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        print(",".join(str(pix) for pix in image))

if len(sys.argv) != 4:
    print('syntax: {} [image_file] [label_file] [image_count]'.format(sys.argv[0]),file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1], "rb") as f, open(sys.argv[2], "rb") as l:
    convert(f, l, int(sys.argv[3]))
