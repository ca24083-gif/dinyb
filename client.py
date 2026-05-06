# client_ubuntu.py
import socket

HOST = "WINDOWS_VM_IP"
PORT = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msg = input("Ubuntu message: ")
    client.sendall(msg.encode())

    if msg.lower() == "exit":
        break

    reply = client.recv(1024).decode()
    print(reply)

client.close()
