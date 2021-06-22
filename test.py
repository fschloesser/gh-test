#!/usr/env/python

# simple script to work with all python versions instead of 3.8

import sys

print("Running python {}".format(sys.version_info))
print("Running python {major}.{minor}.{micro} exiting".format(
    major=sys.version_info.major,
    minor=sys.version_info.minor,
    micro=sys.version_info.micro))

if (sys.version_info.major == 3 and sys.version_info.minor == 8):
    print("ERROR detected python 3.8. exiting")
    exit(1)
else:
    print("SUCCESS not running python 3.8. exiting")
    exit(0)

