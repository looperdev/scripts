#!/bin/bash
old_ip="$(cat last_ip.txt)"
new_ip="$(dig +short myip.opendns.com @resolver1.opendns.com)"


if [ "$old_ip" = "$new_ip" ]; then
    echo "They are the same"
fi
