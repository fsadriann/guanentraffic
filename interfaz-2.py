import customtkinter
from customtkinter import *
import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("GUANENTRAFFIC 0.1")
        self.geometry("1280x720")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # logo
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo_g.png")), size=(52, 52))

        #qr
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        self.qr_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "qr.png")), size=(100, 100))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        # titulo app

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Guanentraffic", image=self.logo_image, compound="left", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.configure(font=('Arial Rounded MT Bold',40))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        #boton inicio

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Inicio", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
        self.home_button.configure(font=('Arial Rounded MT Bold',20))


        #boton 2

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")
        self.frame_2_button.configure(font=('Arial Rounded MT Bold',20))

        #boton 3

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        self.frame_3_button.configure(font=('Arial Rounded MT Bold',20))


        # cambiar tema app

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # home frame --------------------------------------------------------------------------------
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # canvas frame

        self.videocapture_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color='white', width=900, height=500)
        self.videocapture_frame.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        # canvas(en realidad ahi a a estar el video)

        self.videocapture = customtkinter.CTkCanvas(self.videocapture_frame, bg="black", width=800, height=400)
        self.videocapture.grid(padx=20, pady=20)

        #qr frame

        self.qr_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color='white', width=20, height=20)
        self.qr_frame.place(relx=0.9, rely=0.9, anchor=customtkinter.CENTER)

        # qr

        self.qr_label= customtkinter.CTkLabel(self.qr_frame, text="", image=self.qr_image, compound="center", font=customtkinter.CTkFont(size=100, weight="bold"))
        self.qr_label.grid(padx=10, pady=10)    

        # create second frame --------------------------------------------------------------------------------------------
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame ---------------------------------------------------------------------------------------------
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("Inicio")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "Inicio" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "Inicio":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("Inicio")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
