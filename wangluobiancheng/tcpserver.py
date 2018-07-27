# 这个脚本创建一个 TCP 服务器，它接受来自客户端的消息，然后将消息加上时间戳前缀并发送回客户端

from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZE = 1024
ADDR =(HOST,PORT)

tcpss = socket(AF_INET,SOCK_STREAM)
tcpss.bind(ADDR)
tcpss.listen(5)

while True:
    print("waiting for connecting......")
    tcpcs,addr = tcpss.accept()
    print("...connect from ",addr)

    while True:
        data = tcpcs.recv(BUFSIZE).decode()
        if not data:
            break
        tcpcs.send(('[%s] %s' %(ctime(),data)).encode())
    tcpcs.close()
tcpss.close