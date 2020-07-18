# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 23:46:59 2020

@author: Lulock
"""

import socket
from _thread import *

server = "YOUR LOCAL IPv4 ADDRESS HERE"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen(2)
print("Waiting for a connection, Server started.")


def read_pos(string):
    string = string.split(",")
    return int(string[0]), int(string[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(0, 0), (100, 100)]


def threaded_client(conn, player):
    print("ïnside threaded client")
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while(True):
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while(True):
    conn, addr = s.accept()
    print("Connected to: ", addr)

    # Start a thread to allow for multiple client updates. Multiple threads within a process share the same data space with the main thread and can therefore share information or communicate with each other more easily than if they were separate processes.
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
