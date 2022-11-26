import socket
import time

# 컴퓨터 서버의 역할을 하도록 테스트
# host 의 값을 비워둔다
# HOST =''
# PORT = 7477
#
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
# server_socket.bind(('',7477))
# server_socket.listen()
# client_socket, addr=server_socket.accept()
# print('Connected by', addr)
#
# while True:
#     order = input('명령을 입력하세요')
#     client_socket.sendall(order.encode('utf-8'))
#     time.sleep(1)
#     data = client_socket.recv(1024)
#     if not data:
#         break
#     print('addr:{} data:{}'.format(addr, data.decode()))
#
# client_socket.close()
# server_socket.close()


import time
import socket

# 라즈베리파이에 사용하는 주소
HOST = '192.168.0.6'
PORT = 7477

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, 7477))

while True:
    data = client_socket.recv(1024)
    if not data:
        break

    print(data.decode('utf-8'))
    client_socket.sendall('receive13'.encode())
# client_socket.close()