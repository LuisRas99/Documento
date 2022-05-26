import socket
import time

print("Iniciando programa")
s=socket.socket()
s.connect(("172.17.207.207",5038))

print("Mandando Login")
s.send ("Action:Login\n".encode())
s.send ("Username:diagnocons\n".encode())
s.send ("Secret:diagnocons2022\n".encode())
s.send ("\n".encode())
time.sleep(8)

print("Mandando Logoff")
s.send ("Action:Logoff\n".encode())
s.send ("\n".encode())

print("Fin del programa")
