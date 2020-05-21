# client
import socket
import threading, time

def tcplink(n, data):
    print('Thread %s is running...\r\n' % n)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, int(port)))
    # s.send(data.encode('utf-8'))
    # print(s.recv(1024).decode('utf-8'))

# ip = input('IP: ')
# port = input('Port: ')
# data = input('Data: ')
# num = input('Number: ')
ip = '127.0.0.1'
port = '5003'
data = 'TestData'
num = '100'

for n in range(int(num)):
    t = threading.Thread(target=tcplink, args=(n, data))
    t.start()  
    # if n % 2 == 0:
    #     t = threading.Thread(target=tcplink, args=(n, data1))
    #     t.start()
    # else:
    #     t = threading.Thread(target=tcplink, args=(n, data2))
    #     t.start()

exit = input('Input any word to exit: ')
