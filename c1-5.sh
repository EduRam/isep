#!/usr/bin/env bash

# To setup this script on cron
#
#    $> sudo crontab -e
# 
# Add the following line
#
#    30 23 * * * /home/e/wrk/isep/c1-5.sh > /tmp/password_notices.log
#
# To verify previous command
#
#  $> sudo crontab -l
#
#
# To run this script "by hand".
#
#  $> sudo ./c1-5_setup.sh 
#  $> sudo ./c1-5.sh 
#  $> sudo ./c1-5_teardown.sh 
#
# To run on TRACE mode
#
#
APP_ARGS=($@)

if [[ ${APP_ARGS[0]} == "TRACE" ]]
then 
	echo set TRACE 
	set -x 
fi


# this script must run a root
if [[ "$EUID" -ne 0 ]]
  then echo "Please run this script as root"
  exit
fi


# number of seconds in a day
# 24h x 60min x 60sec
# this will be use later to convert days to seconds.
SECONDS_IN_A_DAY=$((24 * 60 * 60)) 



# 5 days to warn before passwd expires
WARN_BEFORE_N_DAYS=5



# get current date as seconds since Unix Epoch Time
# Note: we could convert here to days and always calculate in days later
current_time_in_seconds_since_1970=$(date +%s)


# bash recipe - set variable "line" from each line on file shadowll
cat /etc/shadow | while read line; do

 
	# bash recipe - parse string on variable line, seperated by ":" and set each on an array
	IFS=':' read -r -a array <<< "$line"


	# debug
	# note: '#' symbol is used to count elements
	#echo "LINE number of elements ${#array[@]}"
	

	username=${array[0]}
	passwd_change_day_since_1970=${array[2]}
	passwd_number_of_days_to_expire=${array[4]}

	# if passwd_number_of_days_to_expire is empty (not defined) 
	# do not continue in this line
	if [ -z "$passwd_number_of_days_to_expire" ]
	then
		continue  
	fi	
	
	passwd_expiration_day_since_1970=$((passwd_change_day_since_1970 + passwd_number_of_days_to_expire))
	#echo "passwd_expiration_day_since_1970=$passwd_expiration_day_since_1970"
	

	passwd_expiration_seconds_since_1970=$((passwd_expiration_day_since_1970 * SECONDS_IN_A_DAY))
	#echo "passwd_expiration_seconds_since_1970=$passwd_expiration_seconds_since_1970"

	# difference in seconds between current date and expiration date
	seconds_to_expire=$((passwd_expiration_seconds_since_1970 - current_time_in_seconds_since_1970))
	#echo "seconds_to_expire=$seconds_to_expire"
	
	# seconds to warning expiration date 5 days and convert to seconds
	seconds_to_warning=$((WARN_BEFORE_N_DAYS * SECONDS_IN_A_DAY))
	#echo "seconds_to_warning=$seconds_to_warning"
	
	if [[ $seconds_to_expire -le $seconds_to_warning ]]
	then
		echo $username
	fi
  
done

