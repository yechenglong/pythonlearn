# 这个脚本创建一个 TCP 客户端，它提示用户输入发送到服务器端的消息，并接收从服务器端返回的添加了时间戳前
# 缀的相同消息，然后将结果展示给用户。
from socket import  *
HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR =(HOST,PORT)

tcpcs =socket(AF_INET,SOCK_STREAM)
tcpcs.connect(ADDR)
while True:
    data = input('> ')
    if not data:
        break
    tcpcs.send(data.encode())
    data =tcpcs.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))

tcpcs.close()

