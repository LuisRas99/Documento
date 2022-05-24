import socket

print("Iniciando programa")
s=socket.socket()
s.connect(("172.17.207.207",5038))

print("Fin del programa")
