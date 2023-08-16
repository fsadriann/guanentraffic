# importar las librerias
from customtkinter import *
import customtkinter
import os
from PIL import Image

# funciones

def ir_inicio():
    pass

def ir_opciones():
    pass

def guardar():
    pass

def salir():
    pass

# crear la ventana

app = CTk()
app.title("Guanentraffic")
app.geometry("1280x720")

# grid layout 1x2

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

#imagenes
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"img")


#frame de navegación
navigation_frame=customtkinter.CTkFrame(master=app,corner_radius=0)
navigation_frame.grid(row=0, column=0, sticky="nsew")
navigation_frame.grid_rowconfigure(4,weight=2)

navigation_frame_label= customtkinter.CTkLabel(master=navigation_frame, text="Guanentraffic", compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
navigation_frame_label.grid(row=0, column=0, padx=60, pady=20)

# boton inicio
home_button= customtkinter.CTkButton(master=navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Inicio", fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),anchor="w",command=ir_inicio)
home_button.grid(row=1, column=0, sticky="ew")

#botón opciones
frame_2_button= customtkinter.CTkButton(master=navigation_frame,corner_radius=0, height=40,border_spacing=10, text="Opciones", fg_color="transparent", text_color=("gray10","gray90"), hover_color=("gray70","gray30"),anchor="w", command=ir_opciones)
frame_2_button.grid(row=2, column=0, sticky="ew")


app.mainloop()
