#! /usr/bin/env python3

import os
import requests

feedback_path = "/data/feedback/"
target_addr = ""
feedback = {}
keys = ("title", "name", "date", "feedback")

for file in os.listdir(feedback_path):
    feedback[file] = {}
#