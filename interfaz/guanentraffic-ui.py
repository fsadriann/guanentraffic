# se importan las librerias

import customtkinter
from tkinter import messagebox

## se define el tema de la app

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# creamos la ventana

ventana_principal = customtkinter.CTk()
ventana_principal.geometry("1280x720")

def button_function():
    messagebox.showinfo("Guanentraffic","aplicación en proceso...")

# barra lateral

barra_lateral = customtkinter.CTkFrame(master=ventana_principal,width=300,height=1240)
barra_lateral.pack(side='left', fill='y')

# botón

button = customtkinter.CTkButton(master=barra_lateral, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

#titulo app

titulo_app = customtkinter.CTkLabel(master=barra_lateral, text="Guanentraffic")
titulo_app.configure(font=('Arial Rounded MT Bold',40))
titulo_app.grid(row=0, columnspan=2, pady=20, padx=20)

# frame combo
frame_combo = customtkinter.CTkFrame(master=ventana_principal, width= 920, height=200)
frame_combo.place(x=795, y=120, anchor=customtkinter.CENTER)



# combobox

combobox = customtkinter.CTkComboBox(frame_combo)
combobox


ventana_principal.mainloop()