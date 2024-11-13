#!/usr/bin/env bash

# Set up autograder files

cp /autograder/submission/ex1.py /autograder/source/ex1.py

cd /autograder/source

python3 run_tests.py
