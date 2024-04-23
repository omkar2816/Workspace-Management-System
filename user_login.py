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

        self.main_frame = CTkFrame(master=self, width=400, height=480, fg_color="#FFFFFF")
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(expand=True, side="right")

        CTkLabel(master=self.main_frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=("Arial", 24, "bold")).pack(anchor="w", pady=(40, 5), padx=(25, 0))
        CTkLabel(master=self.main_frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial", 14, "bold")).pack(anchor="w", pady=(10, 5), padx=(25, 0))

        self.user_entry = (CTkEntry(master=self.main_frame, placeholder_text="Username", border_color="#601e88", height=35, width=280, fg_color="#EEEEEE", font=("Arial", 14)))
        self.user_entry.pack(anchor="w", padx=(25, 25), pady=(50, 0))
        self.u_password = (CTkEntry(master=self.main_frame, placeholder_text="Password", border_color="#601e88", height=35, width=280, fg_color="#EEEEEE", font=("Arial", 14), show="●"))
        self.u_password.pack(anchor="w", padx=(25, 25), pady=(25, 0))
        self.show_password = CTkCheckBox(master=self.main_frame, checkbox_height=15, checkbox_width=15, text="Show Password ?", text_color="#7E7E7E", variable=self.s_pass, onvalue=1, offvalue=0, command=self.toggle_password).pack(anchor="w", padx=(180, 0), pady=(5, 0))

        self.login = CTkButton(master=self.main_frame, text="Log In", fg_color="#601E88", hover_color="#700777", font=("Arial Bold", 14), text_color="#ffffff", width=200, height=35, corner_radius=12, command=self.get_entries).pack(anchor="w", pady=(30, 0), padx=(70, 0))
        self.new_user = CTkButton(master=self.main_frame, text="Register as New Employee?", fg_color="transparent", hover_color="#ffffff",
                                  font=("Arial", 12, "underline"), text_color="#7E7E7E", width=200, height=35, corner_radius=12,
                                  command=self.add_details_user).pack(anchor="w", pady=(20, 0), padx=(70, 0))
        self.switch = CTkButton(master=self.main_frame, text="Switch to Admin?", fg_color="transparent", hover_color="#ffffff", font=("Arial", 12, "underline"), text_color="#7E7E7E", command=self.switch).pack(anchor="w", padx=(100, 0), pady=(20, 0))

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

# if __name__ == '__main__':
#     app = Login()
#     app.mainloop()