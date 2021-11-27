#!/usr/bin/env bash

# This will create several users
# and set each different expiration intervals 
# so script c1-5.sh can have some expected output

# this script must run a root
if [[ "$EUID" -ne 0 ]]
  then echo "Please run this script as root"
  exit
fi

set -x

# always create user without home directory because we don't need them to login
userdel usrtest1
userdel usrtest2
userdel usrtest5
userdel usrtest6
userdel usrtest0

