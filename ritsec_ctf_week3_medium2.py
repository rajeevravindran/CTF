#!/usr/bin/python3

import socket
import re

dictionary = {
    "plus" : "+",
    "minus" : "-",
    "multiply" : "*",
    "floor_division" : "//"
}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 1234))
i = 1

while True:
    print("Loop #" + str(i),end=' ')
    i = i + 1
    raw_socket_data = b''
    while True:
        chunk = client.recv(4096)
        raw_socket_data += chunk
        if len(chunk) < 4096:
            break

    sockdata = raw_socket_data.decode('utf-8')

    if 'RS{' in sockdata:
        print("!!!!!!")
        print("RITSEC FLAG ->" + sockdata)
        break


    for key,value in dictionary.items():
        # print(key, value)
        sockdata = sockdata.replace(key, dictionary[key])
    # print(sockdata)
    try:
        cleanedup = sockdata.replace("=","").strip()

        # print("Expression {" + cleanedup + "}")
        result = eval(cleanedup)

        # print(cleanedup + ' = ' + str(result))

        data = str(result).encode('utf-8') + b'\n'
        client.send(data)
    except Exception as e:
        print("Error", e)