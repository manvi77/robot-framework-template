#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from os.path import abspath, dirname, isdir, join as path_join
from unittest import TestLoader, TestSuite, TextTestRunner


libs_base = abspath(dirname(__file__))

paths_for_libs = [path_join(libs_base, dirname) for dirname in
                  os.listdir(libs_base) if isdir(path_join(libs_base, dirname))]

all_tests = TestSuite()
for libpath in paths_for_libs:
    sys.path.insert(1, libpath)
    all_tests.addTest(TestLoader().discover(libpath))

if len(sys.argv) > 1 and 'verbosity=' in sys.argv[1]:
    verbosity = int(sys.argv[1].split('=')[1])
else:
    verbosity = 1

if all_tests.countTestCases() < 1:
    print 'No tests found!'
    sys.exit(1)

result = TextTestRunner(verbosity=verbosity).run(all_tests)

# Flip the boolean value so `True` becomes `0`
sys.exit(int(not result.wasSuccessful()))