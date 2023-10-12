from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils

global logo_col
global logo_guanentraffic

#funciones

def salir():
    main.destroy()

def iniciar():
    pass

def archivo():
    pass

def ir_basedatos():
    pass

# creamos la ventana

main = Tk()
main.geometry('720x320')
main.config(bg='navy')
main.title('Guanentraffic')
main.resizable(False,False)

# frame principal de la interfaz

BASE=300
ALTURA=280

frameInicio = Frame(main)
frameInicio.config(bg='white', width=BASE, height=ALTURA)
frameInicio.place(x= 20, y=20)

# Titulo app

appTitle = Label(frameInicio, text='Guanentraffic')
appTitle.config(bg="white", fg="navy", font=("Bold", 25), justify="center")
appTitle.place(x=BASE/6, y=ALTURA/6)

logo_guanentraffic = PhotoImage(file="img/logo_g.png")

# logo label

logolbl = Label(frameInicio)
logolbl.config(bg='white', image=logo_guanentraffic)
logolbl.place(x=BASE/2-30, y=ALTURA/2-40)

btnSalir = Button(frameInicio)
btnSalir.config(text='Salir',width=20, command=salir)
btnSalir.place(x=BASE/2-70, y=ALTURA/4+120)


### Frame 2

BASE2 = 360
ALTURA2 = 280

mainFrame = Frame(main)
mainFrame.config(bg='white', width=BASE2, height=ALTURA2)
mainFrame.place(x=340, y=20)

# boton inciar

btnIniciar = Button(mainFrame)
btnIniciar.config(text='Iniciar', width=25, command=iniciar)
btnIniciar.place(x=BASE2/2-90, y=ALTURA2/6+25)

# botón archivo

btnArch = Button(mainFrame)
btnArch.config(text='Archivo', width=25, command=archivo)
btnArch.place(x=BASE2/2-90, y=ALTURA2/6+75)

# botón base datos

btnBaseDatos = Button(mainFrame)
btnBaseDatos.config(text='Base de Datos', width=25, command=ir_basedatos)
btnBaseDatos.place(x=BASE2/2-90, y=ALTURA2/6+125)

main.mainloop()