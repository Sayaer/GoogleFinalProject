#!/usr/bin/env python3

from PIL import Image
import os, sys
from pathlib import Path

"Rotate 90, resize to 128x128, save to jpeg"
"save to folder /opt/icons/"


def fix_images(filepath):
    print('Starting process')
    cleanpath = filepath[0]

    for file in os.listdir(cleanpath):
        if file.endswith(".py") or file.endswith(".DS_Store"):
            pass
        else:
            print('Porcessing: ' + file)
            outfilepath = "/opt/icons/" + file + ".jpeg"
            im = Image.open(file)
            im.rotate(-90).resize((128, 128)).convert("RGB").save(outfilepath)
            im.close()


if __name__ == "__main__":
    fix_images(sys.argv[1:])


