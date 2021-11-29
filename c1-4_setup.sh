#!/usr/bin/env bash

set -x


mkdir -p c1-4_test_dir

cd c1-4_test_dir

# directory name end with .txt
mkdir -p dir.txt

# empty file
touch 0.txt

seq 1 1 > 1.txt

seq 1 10 > 10.txt

seq 1 100 > 100.txt

seq 1 2 > 2.txt

seq 1 3 > 4.txt

seq 1 40 > 40.txt

seq 1 50 > 50.txt

seq 1 60 > 60.txt

seq 1 70 > 70.txt

cd ..

ls -l c1-4_test_dir

echo ""
echo ""
