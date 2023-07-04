#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request as req


if __name__ == "__main__":
    url = sys.argv[1]

    request = req.Request(url)
    with req.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
