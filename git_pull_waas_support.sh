#!/bin/bash

# Bash, with GNU sleep
spin() {
  local i=0
  local sp='.'
  local n=${#sp}
  printf ' '
  while sleep 0.2; do
    printf '%s' "${sp:i++%n:1}" 
  done
}

echo "Running git pull on waas_support"
spin & spinpid=$!
cd ./code/waas_support
git pull
kill "$spinpid"
