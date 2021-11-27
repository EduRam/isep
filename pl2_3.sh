#!/usr/bin/env bash


directory_path=$1
echo "Path $1"

if [[ -d $directory_path ]]
then

	for i in $directory_path/*.txt
	do
		if [[ -f $i ]]
		then
			echo "Analisar ficheiro: $i"
			head -n 1 $i
		else 
			echo "WARNING não é ficheiro: $i"
		fi
	done
else
	echo "$directory_path is not a directory"
fi
