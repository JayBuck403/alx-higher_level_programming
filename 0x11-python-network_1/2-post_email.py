#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import urllib.parse as parse
import urllib.request as req


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = parse.urlencode(email).encode("ascii")

    request = req.Request(url, data)
    with req.urlopen(request) as response:
        print(response.read().decode("utf-8"))
