#!/bin/bash
message="$(echo -n "autosave: " && date --rfc-3339=seconds)"

git add . 
git commit -m "$message"
git push origin master