import socket

s = socket.socket()

s.bind(("192.168.150.100",9999))

s.listen(3)

print("Waiting for Client")

clients = []
while len(clients)<3:
    client, addr = s.accept()
    print("Client Connected, address is :",addr)
    
    client.send(bytes('Welcome to JaySoft','utf-8'))
    
    clients.append((client,addr))

for client,addr in clients:
    print(client,addr," : Closing Connection")
    client.close()
    
