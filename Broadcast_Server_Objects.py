#!/usr/bin/python3

"""
file: service.py
socket service
"""


import socket
import threading
import sys
import time


def socket_service():
    try:
        # # Receiver
        # # Create socket & Receive Object
        s_o_i = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s_o_i.connect(("192.168.1.128", 17171))

        # Send
        # Sending Objects
        s_o_o = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Avoid socket server is occupied （socket.error: [Errno 98] Address already in use）
        s_o_o.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s_o_o.bind(('127.0.0.1', 6666))
        # Connection limit
        s_o_o.listen(1)

    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('Waiting connection...')

    while 1:
        conn, addr = s_o_o.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr, s_o_i))
        t.start()


def deal_data(conn, addr, s_i):
    print ('Accept new connection from {0}'.format(addr))
    for index in range(100):
        time.sleep(1)
        conn.sendall(b'Hi, Welcome to the server!')
    # conn.sendall(s_o.recv(1024))
    # while s_i:
    #     data = s_i.recv(1024)
    #     print(data)
    #     conn.sendall(data)
    conn.close()


if __name__ == '__main__':
    socket_service()