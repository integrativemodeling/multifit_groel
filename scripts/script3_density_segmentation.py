#!/usr/bin/env python

from __future__ import print_function
import subprocess
import os

print("cd output")
os.chdir('output')

cmd = ['multifit', 'segment', "../data/em_maps/groel-11.5A.mrc",
       "14", "0.7", "groel_segments_center.pdb",
       "--seg", "groel_subunit", "--apix", "2.7",
       "--x", "-135", "--y", "-135", "--z", "-135"]
print("======running command:")
print(" ".join(cmd))
subprocess.call(cmd)
