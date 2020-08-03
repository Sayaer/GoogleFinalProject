#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

images_dir = '/home/student-00-4094e4e9d9f9/supplier-data/images/'

# update this URL - http://[linux-instance-external-IP]/fruits
url = "http://localhost/upload/"

for file in os.listdir(images_dir):
        if file.endswith('.jpeg'):
                with open((images_dir + file), 'rb') as opened:
                        print("Opened {file} OK!".format(file=file))
                        r = requests.post(url, files={'file': opened})

