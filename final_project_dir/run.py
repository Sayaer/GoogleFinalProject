"""Write a Python script named run.py to process the text files (001.txt, 003.txt ...) from the
 supplier-data/descriptions directory. The script should turn the data into a JSON dictionary by
  adding all the required fields, including the image associated with the fruit (image_name), and
   uploading it to http://[linux-instance-external-IP]/fruits using the Python requests library."""

"""
Apple
500 lbs
Apple is one of the most nutritious and healthiest fruits. It is very rich in antioxidants and dietary fiber. Moderate consumption can not only increase satiety, but also help promote bowel movements. Apple also contains minerals such as calcium and magnesium, which can help prevent and delay bone loss and maintain bone health. It is good for young and old. 
"""

#! /usr/bin/env python3

import os
import requests
import json

description_dir = '/home/student-00-4094e4e9d9f9/supplier-data/descriptions/'
url = 'http://34.68.197.32/fruits/'

fruit_profile = {}

for file in os.listdir(description_dir):
        with open((description_dir + file), 'r') as opened_file:
                lines = opened_file.readlines()
                fruit_profile['name'] = lines[0].strip()
                weight = lines[1].strip()
                cut_weight = weight[:4].strip()
                fruit_profile['weight'] = int(cut_weight)
                fruit_profile['description'] = lines[2].strip()
                image_name = file[:-4] + ".jpeg"
                fruit_profile['image_name'] = image_name
                print("Sending data now")
                # payload = json.dumps(fruit_profile)
                r = requests.post(url, json=fruit_profile)
                print(r.status_code)

