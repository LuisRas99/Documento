from tkinter import *
from asterisk.ami import AMIClient
from asterisk.ami import SimpleAction

def revisar():
    print("Funciona")
    client.send_action(action)
    
client = AMIClient(address='172.17.207.207',port=5038)
client.login(username='diagnocons',secret='diagnocons2022')
action = SimpleAction(
   	'Originate',
    Channel='SIP/200',
 	Exten='902',
  	Priority=1,
  	Context='prueba',
 	CallerID='python',
)

ventana = Tk() 
ventana.geometry("380x300")

boton = Button(ventana,text="Llamar",command=revisar) 
boton.pack()
ventana.mainloop()

print("Fin del programa")
client.logoff()

