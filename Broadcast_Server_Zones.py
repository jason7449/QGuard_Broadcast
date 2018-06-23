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
        s_z_i = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s_z_i.connect(("192.168.1.128", 17172))

        # Send
        # Sending zones
        s_z_o = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Avoid socket server is occupied （socket.error: [Errno 98] Address already in use）
        s_z_o.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s_z_o.bind(('0.0.0.0', 8888))
        # Connection limit
        s_z_o.listen(10)



    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('Waiting connection...')


    while 1:
        conn2, addr2 = s_z_o.accept()
        t2 = threading.Thread(target=deal_data, args=(conn2, addr2, s_z_i))
        t2.start()



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