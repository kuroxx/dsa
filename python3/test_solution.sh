#!/bin/bash
Path="$1"
cd ${Path}

python3 -m unittest test_solution.py

cd ../..