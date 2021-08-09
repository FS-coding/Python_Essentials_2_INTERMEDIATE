# 4.4.1.8 The os module: LAB
# Write a function or method called 'find' that
# takes two arguments called 'path' and 'dir'.
# The 'path' argument should accept a relative or absolute path to a directory
# where the search should start,
# while the 'dir' argument should be the name of a directory
# that you want to find in the given path.
# Your program should display the absolute paths if it finds a directory with the given name.

# The directory search should be done recursively.
# This means that the search should also include all subdirectories in the given path.

# Example input:
# path="./tree", dir="python"

# Example output:

# .../tree/python
# .../tree/cpp/other_courses/python
# .../tree/c/other_courses/python

import os

path = "./tree"
dir = "python"


def scan_d(dir, path):
    for d in os.listdir(path):
        if d == dir:
            print(path + "/" + d)
        new = path + "/" + d
        scan_d(dir, new)


scan_d(dir, path)
