import socket
import time

def iniciar_ami(usuario,clave):
    s.send("Action:Login\n".encode())
    comando = "Username:"+usuario+"\n"
    s.send(comando.encode())
    comando = "Secret:"+clave+"\n"
    s.send(comando.encode())
    s.send("\n".encode())
    
def finalizar_ami():
    s.send("Action:Logoff\n".encode())
    s.send("\n".encode())
    

print("Iniciando Programa")
s=socket.socket()
s.connect(("172.17.207.207",5038))

print("Iniciando Login")
iniciar_ami("diagnocons","diagnocons2022")
while True:
    mensaje = s.recv(4096) 
    print(mensaje.decode())

print("Mandando Logoff")
finalizar_ami()



print("Fin de programa")