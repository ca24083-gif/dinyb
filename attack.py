# server_windows.py
import socket

HOST = "0.0.0.0"
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Listening on port {PORT}...")
conn, addr = server.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == "exit":
        break

    print("Ubuntu says:", data)
    conn.sendall(f"Windows received: {data}".encode())

conn.close()
server.close()
