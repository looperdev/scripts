#!/bin/bash

zipinfo Jonathan.zip | egrep -o ' Jonathan/.[^/]+/' | sort -u
