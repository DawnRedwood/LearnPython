# server
import socket
import threading, time

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...\r\n' % addr)
    sock.send(b'Welcome %s!' % addr)
    # while True:
    #     data = sock.recv(1024).decode('utf-8')
    #     print('Data: %s.' % data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(('127.0.0.1', 9999))
s.listen(10)
print('Waiting for connection...')
while True:
    # 接收一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
