# import customtkinter
# from PIL import Image
# from customtkinter import *
#
# WORKSPACE_IMG_DATA = Image.open("images/WORKSPACE MANAGEMENT SYSTEM.png")
#
#
# class Starter(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("Starter")
#         self.geometry("800x600+500+150")
#         set_appearance_mode("system")
#         self.workspace_img = CTkImage(dark_image=WORKSPACE_IMG_DATA, light_image=WORKSPACE_IMG_DATA, size=(800, 530))
#
#         self.starter_img = CTkLabel(master=self, image=self.workspace_img, text="")
#         self.starter_img.pack()
#
#         self.button = CTkButton(master=self, text="Get Started", height=35, width=200, font=("Arial Bold", 14), command=self.get_started)
#         self.button.pack(anchor="n", padx=(25, 25), pady=(560, 0))
#
#     def get_started(self):
#         self.destroy()
#         import user_login
#         start = user_login.Login()
#         start.mainloop()
#
#
# if __name__ == '__main__':
#     starter = Starter()
#     starter.mainloop()

from tkinter import *
from PIL import Image
import customtkinter

colors = ["#070F2B", "#1B1A55", "#535C91"]


class Stater(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Workspace Management System")
        self.geometry("895x680+350+80")
        self.config(bg="#491669")
        self.resizable(False, False)
        self.image = customtkinter.CTkImage(light_image=Image.open('Images/WORK.png'),
                                            dark_image=Image.open('Images/WORK.png'),
                                            size=(895, 640))
        self.label = customtkinter.CTkLabel(self, image=self.image, text="")
        self.label.pack()

        self.button = customtkinter.CTkButton(self, text="Get Started", width=140, height=28, corner_radius=16,
                                              bg_color="#491669", fg_color="#491669", text_color="#ffffff",
                                              font=("Century Gothic", 18, "underline"), hover=False,
                                              command=self.login)
        self.button.pack(anchor="center")

    def login(self):
        self.destroy()
        import user_login
        login = user_login.Login()
        login.mainloop()


if __name__ == '__main__':
    stater = Stater()
    stater.mainloop()