#!/usr/bin/env bash

set -x


mkdir -p c1-3_test_dir

cd c1-3_test_dir

touch file_000
chmod 000 file_000

touch file_222
chmod 222 file_222

touch file_700
chmod 700 file_700

touch file_070
chmod 070 file_070

touch file_007
chmod 007 file_007

touch file_001
chmod 001 file_001

touch file_002
chmod 002 file_002

touch file_004
chmod 004 file_004

cd ..

ls -l c1-3_test_dir

echo ""
echo ""
