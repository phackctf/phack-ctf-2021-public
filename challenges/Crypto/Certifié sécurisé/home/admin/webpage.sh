#!/bin/sh

# Basic webserver returning hostname

CL=$(expr `hostname | wc -c` + 3)

printf "HTTP/1.1 200 OK\r\nContent-Length: $CL\r\n\r\n$(hostname)\r\n\r\n"
