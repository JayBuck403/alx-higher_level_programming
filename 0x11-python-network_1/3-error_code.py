#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import urllib.error as error
import urllib.request as req


if __name__ == "__main__":
    url = sys.argv[1]

    request = req.Request(url)
    try:
        with req.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
