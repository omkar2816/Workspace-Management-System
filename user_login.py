from tkinter import messagebox

import customtkinter
import mysql.connector
from PIL import Image
from customtkinter import *

import connection
# from app_admin_windows import DashboardWindow
from app_user_windows import DashboardWindow

SIDE_IMG_DATA = Image.open("images/side-img.png")
USER_SIDE_IMAGE_DATA = Image.open("images/side-image.jpg")
ADMIN_SIDE_IMAGE_DATA = Image.open("images/admin_side_img.png")

COLORS = ["#FFFFFF", "#601E88", "#7E7E7E", "#EEEEEE", "#700777"]
ANCHORS = ["nw", "n", "ne", "w", "center", "e"]
FONTS = ["Arial Bold", "Arial", "Rockwell"]


class Login(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("login")
        set_appearance_mode("system")
        self.geometry("700x480+600+200")
        self.side_img = CTkImage(dark_image=SIDE_IMG_DATA, light_image=SIDE_IMG_DATA, size=(350, 480))
        self.user_side_image = CTkImage(dark_image=USER_SIDE_IMAGE_DATA, light_image=USER_SIDE_IMAGE_DATA, size=(350, 480))
        self.admin_side_img = CTkImage(dark_image=ADMIN_SIDE_IMAGE_DATA, light_image=ADMIN_SIDE_IMAGE_DATA, size=(350, 480))
        self.s_pass = IntVar(value=0)
        # creates login frames
        CTkLabel(master=self, text="", image=self.user_side_image).pack(expand=True, side="left")

        self.main_frame = CTkFrame(master=self, width=400, height=480, fg_color=COLORS[0])
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(expand=True, side="right")

        CTkLabel(master=self.main_frame, text="Welcome Back!", text_color=COLORS[1], anchor=ANCHORS[3], justify="left", font=(FONTS[1], 24, "bold")).pack(anchor=ANCHORS[3], pady=(40, 5), padx=(25, 0))
        CTkLabel(master=self.main_frame, text="Sign in to your account", text_color=COLORS[2], anchor=ANCHORS[3], justify="left", font=(FONTS[1], 14, "bold")).pack(anchor=ANCHORS[3], pady=(10, 5), padx=(25, 0))

        self.user_entry = (CTkEntry(master=self.main_frame, placeholder_text="Username", border_color=COLORS[1], height=35, width=280, fg_color=COLORS[3], font=(FONTS[1], 14)))
        self.user_entry.pack(anchor=ANCHORS[3], padx=(25, 25), pady=(50, 0))
        self.u_password = (CTkEntry(master=self.main_frame, placeholder_text="Password", border_color=COLORS[1], height=35, width=280, fg_color=COLORS[3], font=(FONTS[1], 14), show="●"))
        self.u_password.pack(anchor=ANCHORS[3], padx=(25, 25), pady=(25, 0))
        self.show_password = CTkCheckBox(master=self.main_frame, checkbox_height=15, checkbox_width=15, text="Show Password ?", text_color=COLORS[2], variable=self.s_pass, onvalue=1, offvalue=0, command=self.toggle_password).pack(anchor=ANCHORS[3], padx=(180, 0), pady=(5, 0))

        self.login = CTkButton(master=self.main_frame, text="Log In", fg_color=COLORS[1], hover_color=COLORS[4], font=(FONTS[0], 14), text_color=COLORS[0], width=200, height=35, corner_radius=12, command=self.get_entries).pack(anchor=ANCHORS[3], pady=(30, 0), padx=(70, 0))
        self.new_user = CTkButton(master=self.main_frame, text="Register as New Employee?", fg_color="transparent", hover_color=COLORS[0],
                                  font=(FONTS[1], 12, "underline"), text_color=COLORS[2], width=200, height=35, corner_radius=12,
                                  command=self.add_details_user).pack(anchor=ANCHORS[3], pady=(20, 0), padx=(70, 0))
        self.switch = CTkButton(master=self.main_frame, text="Switch to Admin?", fg_color="transparent", hover_color=COLORS[0], font=(FONTS[1], 12, "underline"), text_color=COLORS[2], command=self.switch).pack(anchor=ANCHORS[3], padx=(100, 0), pady=(20, 0))

    def add_details_user(self):
        self.destroy()
        import add_employee
        add = add_employee.AddEmployee()
        add.mainloop()

    global username
    global password
    def get_entries(self):

        username = self.user_entry.get()

        password = self.u_password.get()

        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            if self.check_user(username, password):
                messagebox.showinfo("Success", "Successfully Logged in to your account.")
                self.destroy()
                dashboard = DashboardWindow(username=username, password=password)
                dashboard.mainloop()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error occured: {e}")

    def check_user(self, e_username, e_password):
        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "SELECT * FROM user_login WHERE username=%s;"
            val = (e_username, )
            cursor.execute(sql, val)
            users = cursor.fetchall()
            if e_username == '' and e_password == '':
                messagebox.showinfo("Null fields", "Null value cannot be accepted\nAll fields are required")
            for user in users:
                db_username = user[0]
                db_password = user[1]
                print(db_username)
                print(db_password)

                if e_username == db_username and e_password == db_password:
                    return True
                elif e_username != db_username and e_password != db_password:
                    messagebox.showinfo("Not exist", "User doesn't exist\nAdd your details to employee list")
                elif e_username != db_username and e_password == db_password:
                    messagebox.showerror("Invalid", "Invalid username")
                elif e_username == db_username and e_password != db_password:
                    messagebox.showerror("Incorrect", "Incorrect Password")
                else:
                    pass
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error occured: {e}")

    def toggle_password(self):
        if self.s_pass.get() == 1:
            self.u_password.configure(show='')
        else:
            self.u_password.configure(show='●')

    def switch(self):
        self.destroy()
        import admin_login
        login_main = admin_login.Starter()
        login_main.mainloop()
