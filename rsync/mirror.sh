#!/bin/bash
#mirror from $1 to $2 directory
#rsync -azvhP --dry-run --delete jlooper@waasccserv3:/user/home/jlooper/work/ /mnt/c/work
#rsync -avzhP --delete --dry-run jlooper@waasccserv3:~/work/archive/anomaly_meeting/ . 


if [ $# -eq 3 ] && [ $3 = "--dry-run" ]; then
    echo "default dry-run"
    set -x
    rsync -avzc --delete --dry-run $1 $2
    set +x
elif [ $# -eq 3 ] && [ $3 = "--sync" ] ; then
    echo "sync from source to dest"
    set -x
    rsync -avzc --delete $1 $2
    set +x
else
    echo "Invalid usage: mirror.sh [source] [dest] [--dry-run | --sync]"
fi
