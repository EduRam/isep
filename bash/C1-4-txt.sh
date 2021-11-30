#!/bin/bash

APP_NUM_ARGS=1
APP_ARGS=($@)

##############
## check if script is running as root
###############
if [[ $EUID -eq 0 ]]
then
    echo " !! WARNING !! - You are running the script as root"
fi

#############
# check number params
#############
if [[ $# -ne $APP_NUM_ARGS ]]
 then echo "Too many params, use --help"
 exit 1
fi
####################
# check if param is for help
################
if [[ ${APP_ARGS[0]} == "--help" ]]
  then echo " Usage: C1-4-txt.sh [OPTION] <DIR>"
	  echo "OPTIONS	:"
	  echo "--help	: help menu"
	  echo "<DIR>	: specify a full path directory"
	  echo "example	: C1-4-txt.sh /home/user/dir1"
  exit 1
fi
####################
# check if param is a directory
###################
if [[ ! -d "${APP_ARGS[0]}" ]]
  then echo "${APP_ARGS[0]} is NOT a directory, use --help";
  exit 1
fi

##############
#  MAIN - list top 5 txt files by lines number
##############
APP_FILES_LINES_COUNT=($(wc ${APP_ARGS[0]}/*.txt -l | sort -rn | head -n 6))
echo "Top 5 txt files by line numbers:"
echo "Search DIR: ${APP_ARGS[0]}"
echo "FILES:"
if [[ ${#APP_FILES_LINES_COUNT[@]} -eq 0 ]]
then echo "No txt files found"
else 
  # use for loop to read all values and indexes
  for (( i=2; i<${#APP_FILES_LINES_COUNT[@]}; i=$i+2 ));
  do
    echo "Total Lines: ${APP_FILES_LINES_COUNT[$i]},- file name: ${APP_FILES_LINES_COUNT[$i+1]}"
  done
fi

