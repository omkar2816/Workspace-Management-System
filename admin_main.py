import mysql.connector
from customtkinter import CTkLabel, CTkEntry

import connection
import customtkinter
from customtkinter import *
from PIL import Image
from user_login import Login

ADMIN_SIDE_IMAGE_DATA = Image.open("admin_side_img.png")


class Starter(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("login")
        set_appearance_mode("system")
        self.geometry("700x480+600+200")
        self.admin_side_img = CTkImage(dark_image=ADMIN_SIDE_IMAGE_DATA, light_image=ADMIN_SIDE_IMAGE_DATA,
                                       size=(350, 480))

        CTkLabel(master=self, text="", image=self.admin_side_img).pack(expand=True, side="left")

        self.main_frame = CTkFrame(master=self, width=400, height=480, fg_color="#FFFFFF")
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(expand=True, side="right")

        CTkLabel(master=self.main_frame, text="Welcome Back!", text_color="#774280", anchor="w", justify="left",
                 font=("Arial", 24, "bold")).pack(anchor="w", pady=(40, 5), padx=(25, 0))
        CTkLabel(master=self.main_frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w",
                 justify="left", font=("Arial", 14, "bold")).pack(anchor="w", pady=(10, 5), padx=(25, 0))

        self.admin_entry = CTkEntry(master=self.main_frame, placeholder_text="Admin", height=35, width=280,
                                    fg_color="#EEEEEE", font=("Arial", 14)).pack(anchor="w", padx=(25, 25),
                                                                                 pady=(50, 0))
        self.admin_password = CTkEntry(master=self.main_frame, placeholder_text="Password", height=35, width=280,
                                       fg_color="#EEEEEE", font=("Arial", 14), show="●").pack(anchor="w",
                                                                                              padx=(25, 25),
                                                                                              pady=(25, 0))
        self.show_password = CTkCheckBox(master=self.main_frame, checkbox_height=15, checkbox_width=15,
                                         text="Show Password ?", text_color="#7E7E7E").pack(anchor="w",
                                                                                            padx=(180, 0),
                                                                                            pady=(5, 0))

        self.login = CTkButton(master=self.main_frame, text="Log In", fg_color="#774280", hover_color="#9553a0",
                               font=("Arial Bold", 14), text_color="#ffffff", width=200, height=35,
                               corner_radius=12).pack(anchor="w", pady=(30, 0), padx=(70, 0))
        self.switch = CTkButton(master=self.main_frame, text="Switch to User", fg_color="transparent",
                                hover_color="#ffffff", font=("Arial", 12), text_color="#7E7E7E").pack(anchor="w",
                                                                                                      padx=(100, 0),
                                                                                                      pady=(50, 0))

# app = CTk()
# app.title("login")
# set_appearance_mode("system")
# app.geometry("700x480+600+200")
# admin_side_img = CTkImage(dark_image=ADMIN_SIDE_IMAGE_DATA, light_image=ADMIN_SIDE_IMAGE_DATA,
#                                size=(350, 480))
#
# CTkLabel(master=app, text="", image=admin_side_img).pack(expand=True, side="left")
#
# main_frame = CTkFrame(master=app, width=400, height=480, fg_color="#FFFFFF")
# main_frame.pack_propagate(0)
# main_frame.pack(expand=True, side="right")
#
# CTkLabel(master=main_frame, text="Welcome Back!", text_color="#774280", anchor="w", justify="left",
#          font=("Arial", 24, "bold")).pack(anchor="w", pady=(40, 5), padx=(25, 0))
# CTkLabel(master=main_frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w",
#          justify="left", font=("Arial", 14, "bold")).pack(anchor="w", pady=(10, 5), padx=(25, 0))
#
# admin_entry = CTkEntry(master=main_frame, placeholder_text="Admin", height=35, width=280,
#                             fg_color="#EEEEEE", font=("Arial", 14)).pack(anchor="w", padx=(25, 25),
#                                                                          pady=(50, 0))
# admin_password = CTkEntry(master=main_frame, placeholder_text="Password", height=35, width=280,
#                                fg_color="#EEEEEE", font=("Arial", 14), show="●").pack(anchor="w",
#                                                                                       padx=(25, 25),
#                                                                                       pady=(25, 0))
# show_password = CTkCheckBox(master=main_frame, checkbox_height=15, checkbox_width=15,
#                                  text="Show Password ?", text_color="#7E7E7E").pack(anchor="w",
#                                                                                     padx=(180, 0),
#                                                                                     pady=(5, 0))
#
# login = CTkButton(master=main_frame, text="Log In", fg_color="#774280", hover_color="#9553a0",
#                        font=("Arial Bold", 14), text_color="#ffffff", width=200, height=35,
#                        corner_radius=12).pack(anchor="w", pady=(30, 0), padx=(70, 0))
# switch = CTkButton(master=main_frame, text="Switch to User", fg_color="transparent",
#                         hover_color="#1B1A1A", font=("Arial", 12), text_color="#7E7E7E").pack(anchor="w",
#                                                                                               padx=(100, 0),
#                                                                                               pady=(50, 0))
#
# app.mainloop()