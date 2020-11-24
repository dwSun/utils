#!/usr/bin/env bash
# usage: deploy_pubkeys.sh user@xxx.xxx.xxx.xxx
while read -r line
do
    echo $line
    if [ ! -n "$line" ]; then
        continue
    else
        ssh $*  "
if [ ! -d ~/.ssh ]; then
    mkdir ~/.ssh
    echo '~/.ssh created'
fi
echo $line >> ~/.ssh/authorized_keys
echo 'ssh key deployed'
        "
    fi
done < ~/.ssh/id_rsa.pub
