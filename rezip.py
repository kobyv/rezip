#!/usr/bin/env python
import sys, os, zipfile, tempfile
from io import BytesIO

stdin_stream = BytesIO(sys.stdin.read())
z_in = zipfile.ZipFile(stdin_stream, 'r')

z_out = zipfile.ZipFile(sys.stdout, 'w', zipfile.ZIP_STORED)

for name in z_in.namelist():
    with z_in.open(name) as stream:
        b = stream.read()
    z_out.writestr(name, b)
