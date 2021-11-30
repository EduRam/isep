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
  then echo " Usage: C1-3-files-other.sh [OPTION] <DIR>"
	  echo "OPTIONS	:"
	  echo "--help	: help menu"
	  echo "<DIR>	: specify a full path directory"
	  echo "example	: C1-3-files-other.sh /home/user/dir1"
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
#  MAIN - list files which others have write permissions
##############
APP_FILES_OTHERS_WRITE=($(find ${APP_ARGS[0]} -maxdepth 1 -type f -perm -o+w))
echo "Files with others write privilege:"
echo "Search DIR: ${APP_ARGS[0]}"
echo "FILES:"
if [[ ${#APP_FILES_OTHERS_WRITE[@]} -eq 0 ]]
then echo "No files found"
else 
 for app_file in ${APP_FILES_OTHERS_WRITE[@]}
 do echo $app_file
 done
fi


