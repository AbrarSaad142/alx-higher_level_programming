#!/usr/bin/python3
#Bash script that takes in a URL,sends a request,displays size of the body response
curl -sI $1 | grep Content-Length | cut -d" " -f20.
