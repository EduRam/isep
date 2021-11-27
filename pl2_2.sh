#!/usr/bin/env bash

#set -x

args=("$@")
echo Number of arguments: $#

# iterar por todos 
for value in ${args[@]}
do
	echo ""
	echo $value
	isEven=$(( $value%2 ))
	if [[ $isEven -eq 0 ]]
	then
		echo "Even"
	else
		echo "Odd"
	fi
done
