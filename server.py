import socket

x = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2 arguments : type of  address (IPv4 or IPv6 by default)
#print("server socket created!")

x.bind(("localhost",9999)) #0-65535 0-1000 dont use it

x.listen(3) #min 1 max 5

print('server is up nd running......')

while True:
    c, add = x.accept()
    print(f"succesfully connected with, {add}")
    name = c.recv(1024).decode()
    c.send(f"welcome to my world {name}".encode())
    c.close()




