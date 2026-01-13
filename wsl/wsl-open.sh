#!/bin/bash

windowspath="$(wslpath -w $1)"
powershell.exe -c "start $windowspath"
