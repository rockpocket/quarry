

import socket

s = socket.socket(AF_UNIX,SOCK_STREAM)

socket.bind(cfgmgr09sxm1.shr.oclc.org, 25)

socket.listen()

socket.accept()