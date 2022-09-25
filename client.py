import socket
limit = 3
for _ in range(3):
    c = socket.socket()

    c.connect(("192.168.150.100",9999))

    response = c.recv(1024).decode()

    print(response)