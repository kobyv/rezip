#!/bin/sh
T="$(mktemp)"
rezip.py >$T
cat $T
rm $T
