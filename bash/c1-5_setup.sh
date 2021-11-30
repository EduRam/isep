#!/usr/bin/env bash

# This will create several users
# and set each different expiration intervals 
# so script c1-5.sh can have some expected output

# this script must run a root
if [[ "$EUID" -ne 0 ]]
  then echo "Please run this script as root"
  exit
fi

# always create user 
# use -m because we don't need them to have a home dir

set -x

useradd usrtest1 -M
passwd usrtest1 -x 1

useradd usrtest2 -M
passwd usrtest2 -x 2

useradd usrtest5 -M
passwd usrtest5 -x 5

useradd usrtest6 -M
passwd usrtest6 -x 6

useradd usrtest0 -M
passwd usrtest0 -x -1