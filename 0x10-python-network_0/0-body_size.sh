#!/bin/bash
# Gets the size of HTTP response header
curl -s "$1" | wc -c
