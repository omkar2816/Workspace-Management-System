from tkinter import messagebox
import mysql.connector
import connection
import customtkinter
from customtkinter import *
from PIL import Image
import user_login
import app_admin_windows

ADMIN_SIDE_IMAGE_DATA = Image.open("images/admin_side_img.png")

COLORS = ["#FFFFFF", "#774280", "#7E7E7E", "#EEEEEE", "#9553A0"]
FONTS = ["Arial Bold", "Arial", "Rockwell"]
ANCHORS = ["nw", "n", "ne", "w", "center", "e"]


class Starter(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("login")
        set_appearance_mode("Light")
        self.geometry("700x480+600+200")
        self.s_pass = IntVar(value=0)
        self.admin_side_img = CTkImage(dark_image=ADMIN_SIDE_IMAGE_DATA, light_image=ADMIN_SIDE_IMAGE_DATA,
                                       size=(350, 480))

        CTkLabel(master=self, text="", image=self.admin_side_img).pack(expand=True, side="left")

        self.main_frame = CTkFrame(master=self, width=400, height=480, fg_color=COLORS[0])
        self.main_frame.pack_propagate(False)
        self.main_frame.pack(expand=True, side="right")

        CTkLabel(master=self.main_frame, text="Welcome Back!", text_color=COLORS[1], anchor=ANCHORS[3], justify="left",
                 font=(FONTS[1], 24, "bold")).pack(anchor=ANCHORS[3], pady=(40, 5), padx=(25, 0))
        CTkLabel(master=self.main_frame, text="Sign in to your account", text_color=COLORS[2], anchor=ANCHORS[3],
                 justify="left", font=(FONTS[1], 14, "bold")).pack(anchor=ANCHORS[3], pady=(10, 5), padx=(25, 0))

        self.admin_entry = CTkEntry(master=self.main_frame, placeholder_text="Admin", height=35, width=280,
                                    fg_color=COLORS[3], font=(FONTS[1], 14))
        self.admin_entry.pack(anchor=ANCHORS[3], padx=(25, 25), pady=(50, 0))
        self.admin_password = CTkEntry(master=self.main_frame, placeholder_text="Password", height=35, width=280,
                                       fg_color=COLORS[3], font=(FONTS[1], 14), show="●")
        self.admin_password.pack(anchor=ANCHORS[3], padx=(25, 25), pady=(25, 0))
        self.show_password = CTkCheckBox(master=self.main_frame, checkbox_height=15, checkbox_width=15,
                                         text="Show Password ?", text_color=COLORS[2], variable=self.s_pass,
                                         onvalue=1, offvalue=0, command=self.toggle_password)
        self.show_password.pack(anchor=ANCHORS[3], padx=(180, 0), pady=(5, 0))
        self.login = CTkButton(master=self.main_frame, text="Log In", fg_color=COLORS[1], hover_color=COLORS[4],
                               font=(FONTS[0], 14), text_color=COLORS[0], width=200, height=35,
                               corner_radius=12, command=self.get_entries)
        self.login.pack(anchor=ANCHORS[3], pady=(30, 0), padx=(70, 0))
        self.switch = CTkButton(master=self.main_frame, text="Switch to User", fg_color="transparent",
                                hover_color=COLORS[0], font=(FONTS[1], 12), text_color=COLORS[2], command=self.switch)
        self.switch.pack(anchor=ANCHORS[3], padx=(100, 0), pady=(50, 0))

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
                self.destroy()
                app = app_admin_windows.DashboardWindow(username=username, password=password)
                app.mainloop()
                messagebox.showinfo("Success", "Successfully Logged in to your account.")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error occured: {e}")

    def check_user(self, e_username, e_password):
        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "SELECT * FROM admin_login;"

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
            messagebox.showerror("Database Error", f"Error occurred: {e}")

    def toggle_password(self):
        if self.s_pass.get() == 1:
            self.admin_password.configure(show='')
        else:
            self.admin_password.configure(show='●')

    def switch(self):
        self.destroy()
        login_main = user_login.Login()
        login_main.mainloop()


if __name__ == '__main__':
    stater = Starter()
    stater.mainloop()
