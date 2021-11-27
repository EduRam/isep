#!/usr/bin/env bash

set -x

# create files txt with some contents
echo '1sample1
2sample1
3sample1' > sample1.txt


echo '1sample2
2sample2
3sample2' > sample2.txt


echo '1sample3
sample3
sample3' > sample3.txt

# create potencial error conditions

# create a directory named .txt to test error condition
mkdir -p directory.txt

# create a directory named .txt to test error condition
echo 'ERROR
ERROR
ERROR' > error.text



