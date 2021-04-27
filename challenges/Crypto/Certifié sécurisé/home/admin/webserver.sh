#!/bin/sh

while true; do nc -l -p 80 -e "/webpage.sh" ; done;
