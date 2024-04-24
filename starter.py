from tkinter import *
from PIL import Image
import customtkinter

COLORS = ["#FFFFFF", "#491669"]
FONTS = ["Arial Bold", "Arial", "Century Gothic"]
ANCHORS = ["nw", "n", "ne", "w", "center", "e"]


class Stater(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Workspace Management System")
        self.geometry("895x680+350+80")
        self.config(bg=COLORS[1])
        self.resizable(False, False)
        self.image = customtkinter.CTkImage(light_image=Image.open('Images/WORK.png'),
                                            dark_image=Image.open('Images/WORK.png'),
                                            size=(895, 640))
        self.label = customtkinter.CTkLabel(self, image=self.image, text="")
        self.label.pack()

        self.button = customtkinter.CTkButton(self, text="Get Started as Admin", width=140, height=28, corner_radius=16,
                                              bg_color=COLORS[1], fg_color=COLORS[1], text_color=COLORS[0],
                                              font=(FONTS[2], 18, "underline"), hover=False,
                                              command=self.login_as_admin)
        self.button.pack(anchor=ANCHORS[4], side="left", padx=(175, 0))

        self.button1 = customtkinter.CTkButton(self, text="Get Started as User", width=140, height=28, corner_radius=16,
                                              bg_color=COLORS[1], fg_color=COLORS[1], text_color=COLORS[0],
                                              font=(FONTS[2], 18, "underline"), hover=False,
                                              command=self.login_as_user)
        self.button1.pack(anchor=ANCHORS[2], side="right", padx=(0, 175))

    def login_as_user(self):
        self.destroy()
        import user_login
        user_login = user_login.Login()
        user_login.mainloop()

    def login_as_admin(self):
        self.destroy()
        import admin_login
        admin_login = admin_login.Starter()
        admin_login.mainloop()


if __name__ == '__main__':
    stater = Stater()
    stater.mainloop()