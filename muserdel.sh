#!/bin/bash
user=$1
if [ "$user" == '' ]
	then echo "Usage: muserdel <user>"
	exit 1
fi
/usr/sbin/userdel $user 2> /dev/null
erro=$?
mv /home/$user /srv/home.deleted/
if [ $erro == 0 ] #if userdel executed successfully
        then echo -e "User $user deleted\nMoving /home/$user to /srv/home.deleted/"
        sed -i "/^everyone7887:/ s/,$user//" /etc/aliases #delete from everyone
        exit 0
fi
exit 1