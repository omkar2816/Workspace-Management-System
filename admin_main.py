from tkinter import messagebox

import mysql.connector
from customtkinter import CTkLabel, CTkEntry

import connection
import customtkinter
from customtkinter import *
from PIL import Image
from user_login import Login

ADMIN_SIDE_IMAGE_DATA = Image.open("images/admin_side_img.png")


class Starter(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("login")
        set_appearance_mode("system")
        self.geometry("700x480+600+200")
        self.s_pass = IntVar(value=0)
        self.admin_side_img = CTkImage(dark_image=ADMIN_SIDE_IMAGE_DATA, light_image=ADMIN_SIDE_IMAGE_DATA, size=(350, 480))

        CTkLabel(master=self, text="", image=self.admin_side_img).pack(expand=True, side="left")

        self.main_frame = CTkFrame(master=self, width=400, height=480, fg_color="#FFFFFF")
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(expand=True, side="right")

        CTkLabel(master=self.main_frame, text="Welcome Back!", text_color="#774280", anchor="w", justify="left", font=("Arial", 24, "bold")).pack(anchor="w", pady=(40, 5), padx=(25, 0))
        CTkLabel(master=self.main_frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial", 14, "bold")).pack(anchor="w", pady=(10, 5), padx=(25, 0))

        self.admin_entry = CTkEntry(master=self.main_frame, placeholder_text="Admin", height=35, width=280, fg_color="#EEEEEE", font=("Arial", 14))
        self.admin_entry.pack(anchor="w", padx=(25, 25), pady=(50, 0))
        self.admin_password = CTkEntry(master=self.main_frame, placeholder_text="Password", height=35, width=280, fg_color="#EEEEEE", font=("Arial", 14), show="●")
        self.admin_password.pack(anchor="w", padx=(25, 25), pady=(25, 0))
        self.show_password = CTkCheckBox(master=self.main_frame, checkbox_height=15, checkbox_width=15, text="Show Password ?", text_color="#7E7E7E", variable=self.s_pass, onvalue=1, offvalue=0, command=self.toggle_password)
        self.show_password.pack(anchor="w", padx=(180, 0), pady=(5, 0))
        self.login = CTkButton(master=self.main_frame, text="Log In", fg_color="#774280", hover_color="#9553a0", font=("Arial Bold", 14), text_color="#ffffff", width=200, height=35, corner_radius=12)
        self.login.pack(anchor="w", pady=(30, 0), padx=(70, 0))
        self.switch = CTkButton(master=self.main_frame, text="Switch to User", fg_color="transparent", hover_color="#ffffff", font=("Arial", 12), text_color="#7E7E7E", command=self.switch)
        self.switch.pack(anchor="w", padx=(100, 0), pady=(50, 0))

    def get_entries(self):
        global username
        username = self.admin_entry.get()
        global password
        password = self.admin_password.get()

        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            # sql = "INSERT INTO user_login (username, password) VALUES (%s, %s);"
            # val = (username, password)
            # # sql = " select * from user_login "
            # cursor.execute(sql, val)
            # result = cursor.fetchall()
            # # result1 = result[0][0]
            # db.commit()
            # db.close()
            if self.check_user(username, password):
                messagebox.showinfo("Success", "Successfully Logged in to your account.")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error occured: {e}")

    def check_user(self, e_username, e_password):
        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "SELECT * FROM user_login;"
            cursor.execute(sql)
            users = cursor.fetchall()
            for user in users:
                db_username = user[0]
                db_password = user[1]
                if e_username == db_username and e_password == db_password:
                    return True
                elif e_username == '' and e_password == '':
                    messagebox.showinfo("Null fields", "Null value cannot be accepted\nAll fields are required")
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
            self.admin_password.configure(show='')
        else:
            self.admin_password.configure(show='●')

    def switch(self):
        self.destroy()
        login_main = Login()
        login_main.mainloop()
