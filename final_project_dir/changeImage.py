#! /usr/bin/env python3
import os
from PIL import Image


def process_images():
    """Solves the following Problem: Change image size from 3000x2000 to 600x400
    then change format from .TIFF to .JPEG"""

    # Note: Files have a transparency layer, convert to RGB
    # Note: Save files in the same directory, with .JPEG extension
    images = '/home/student-00-4094e4e9d9f9/supplier-data/images/'

    for img in os.listdir(images):
        if img.endswith(".jpeg"):
            print('{img} is already in .JPEG format'.format(img=img))
        else:
            try:
                with Image.open(images + img) as out_img:
                    # print('Image details: {img.format} | {img.size} | {img.mode}'.format(img=img))
                    out_file_name = img[:-5]
                    # print(out_file_nath)
                    out_img = out_img.convert("RGB")
                    out_img = out_img.resize((600, 400))
                    out_path = [images, out_file_name]
                    # print("/".join(out_path))
                    out_img.save("/".join(out_path) + ".jpeg", "JPEG")
            except OSError as e:
                print('Could not open file: {e}'.format(e=e))


if __name__ == "__main__":
    process_images()
