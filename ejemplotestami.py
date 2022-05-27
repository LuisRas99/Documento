import socket
import time
from tkinter import *

def iniciar_ami(user,password):
    s.send ("Action:Login\n".encode())
    comando = "Username:"+user+"\n"
    s.send (comando.encode())
    comando = "Secret:"+password+"\n"
    s.send (comando.encode())
    s.send ("\n".encode())

def llamar(numero):
    s.send ("Action:Originate\n".encode())
    comando = "Channel:SIP/"+str(numero)+"\n"
    s.send (comando.encode())
    s.send ("Context:prueba\n".encode())
    s.send ("Exten:902\n".encode())
    s.send ("Priority:1\n".encode())
    s.send ("\n".encode())
    
def finalizar_ami():
    s.send ("Action:Logoff\n".encode())
    s.send ("\n".encode())

def revisar():
    llamar(200)

s=socket.socket()
s.connect(("172.17.207.207",5038))
ventana = Tk() 
ventana.geometry("380x300")
iniciar_ami("diagnocons","diagnocons2022")

boton = Button(ventana,text="Llamar",command=revisar) 
boton.pack()
ventana.mainloop()

print("Iniciando Login")
time.sleep(8)
print("Mandando Logoff")
finalizar_ami()	


print("Fin del programa")
