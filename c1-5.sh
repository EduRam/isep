#!/usr/bin/env bash

# To call this script on cron
#
#    $> sudo crontab -e
# 
# Add the following line
#
#    * * * * * /home/e/wrk/isep/c1-5.sh > /tmp/password_notices.log
#
# To verify previous command
#
#  $> sudo crontab -l
#
# EXTRA: Call this script with any parameter to activate debug trace.
#
#    e.g: ./c1-5.sh TRACE
#
TRACE="$1"
if [ -n "$TRACE" ]
then
	echo set TRACE
	set -x 
fi

# get current date as seconds since Unix Epoch Time
# Note: we could convert here to days and always calculate in days later
currentTimeInSecondsSince1970=$(date +%s)
#echo "currentTimeInSecondsSince1970=$currentTimeInSecondsSince1970"


# number of seconds in a day
# 24h x 60min x 60sec
# this will be use later to convert days to seconds.
dayseconds=$((24 * 60 * 60)) 

# bash recipe - set variable "line" from each line on file shadow
cat /etc/shadow | while read line; do

	# debug
	if [ -n "$TRACE" ]
	then
		echo ""
		echo ""
		echo ""
		echo ""
		echo "LINE: $line"
	fi

 
	# bash recipe - parse string on variable line, seperated by ":" and set each on an array
	IFS=':' read -r -a array <<< "$line"


	# debug
	# note: '#' symbol is used to count elements
	#echo "LINE number of elements ${#array[@]}"
	

	username=${array[0]}
	passwdChangeDaySince1970=${array[2]}
	passwdNumberOfDaysToExpire=${array[4]}

	# if passwdNumberOfDaysToExpire is empty (not defined) 
	# do not continue in this line
	if [ -z "$passwdNumberOfDaysToExpire" ]
	then
		continue  
	fi	
	
	passwdExpirationDaySince1970=$((passwdChangeDaySince1970 + passwdNumberOfDaysToExpire))
	#echo "passwdExpirationDaySince1970=$passwdExpirationDaySince1970"
	

	passwdExpirationSecondsSince1970=$((passwdExpirationDaySince1970 * dayseconds))
	#echo "passwdExpirationSecondsSince1970=$passwdExpirationSecondsSince1970"

	# difference in seconds between current date and expiration date
	secondsToExpire=$((passwdExpirationSecondsSince1970 - currentTimeInSecondsSince1970))
	#echo "secondsToExpire=$secondsToExpire"
	
	# seconds to warning expiration date 5 days and convert to seconds
	secondsToWarning=$((5 * dayseconds))
	#echo "secondsToWarning=$secondsToWarning"
	
	# NOTE: Use (()) instead of [] because we are evaluating number expressions?
	
	if (( $secondsToExpire <= $secondsToWarning ))
	then
	
		echo $username
		
		if [ -n "$TRACE" ]
		then
			echo "FOUND ... continue to next line."
		fi

	fi
  
done

