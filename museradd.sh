#!/bin/bash
user=$1
pass=$2
pass_file=/home/infesto/userslist
if [ "$user" == '' ] || [ "$pass" == '' ]
	then echo "Usage: museradd <user> <password>"
	exit 1
fi
/usr/sbin/useradd -m -d /home/$user -s /usr/sbin/nologin -p "$(mkpasswd --method=sha-512 "$pass")" $user 2> /dev/null
erro=$?
if [ $erro == 0 ] #if useradd executed successfully
        then echo "User $user added"
        echo "$user     $pass" >> $pass_file #writes pass to file
        sed -i "/^everyone7887:/ s/$/,$user/" /etc/aliases #addes to everyone alias
        exit 0
elif [ $erro == 9 ]
    	then echo "User $user already exists"
fi
exit 1
