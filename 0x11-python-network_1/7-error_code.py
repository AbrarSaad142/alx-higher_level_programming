#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status
"""
import requests
import sys

if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    status = request.status_code
    print(request.text) if status < 400 else print(
        "Error code: {}".format(request.status_code))
