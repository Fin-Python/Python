import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5001))
server.listen()

print("Waiting for a connection...")

conn, addr = server.accept()
print(f"Connected to {addr}")

data = conn.recv(1024).decode()
response = data.upper()

conn.sendall(response.encode())

conn.close()
server.close()
