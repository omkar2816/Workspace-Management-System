from customtkinter import *
from tkinter import *
import customtkinter
from tkcalendar import *
from PIL import Image
import connection
from tkinter import messagebox
import mysql.connector


class AddEmployee(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Add new Employee")
        set_appearance_mode("system")
        self.geometry("500x550+600+200")
        self.s_pass = IntVar(value=0)
        self.name_entry = CTkEntry(master=self, placeholder_text="Enter name of Employee", height=35, width=330, fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.name_entry.pack(anchor="n", padx=(25, 25), pady=(40, 0))
        self.profession_entry = CTkComboBox(master=self, height=35, width=330, border_color="#601e88", button_color="#601e88", dropdown_fg_color="#601e88", dropdown_text_color="#ffffff", dropdown_hover_color="#491669", button_hover_color="#601e88", values=["Select Job role", "Administrator", "Engineer", "Management"])
        self.profession_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.date_of_birth_entry = CTkEntry(master=self, placeholder_text="Select Date of Birth", height=35, width=330, fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.date_of_birth_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.contact_entry = CTkEntry(master=self, placeholder_text="Contact No.", height=35, width=330, fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.contact_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.emergency_contact_entry = CTkEntry(master=self, placeholder_text="Emergency Contact No.", height=35, width=330, fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.emergency_contact_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.username_entry = CTkEntry(master=self, placeholder_text="Username", height=35, width=330, fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.username_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.password_entry = CTkEntry(master=self, placeholder_text="Password", height=35, width=330, fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14), show="●")
        self.password_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.show_password = CTkCheckBox(master=self, checkbox_height=15, checkbox_width=15, text="Show Password ?", text_color="#7E7E7E", variable=self.s_pass, onvalue=1, offvalue=0, command=self.toggle_password).pack(anchor="n", padx=(200, 0), pady=(5, 0))
        self.add_button = CTkButton(master=self, text="Add Employee", height=35, fg_color="#601e88", hover_color="#491669", text_color="#ffffff", font=("Arial", 14), command=self.get_entries).pack(anchor="n", padx=(25, 25), pady=(25, 0))

    def toggle_password(self):
        if self.s_pass.get() == 1:
            self.password_entry.configure(show='')
        else:
            self.password_entry.configure(show='●')

    def get_entries(self):
        global username
        employee_name = self.name_entry.get()
        profession = self.profession_entry.get()
        date_of_birth = self.date_of_birth_entry.get()
        contact = self.contact_entry.get()
        emergency_contact = self.emergency_contact_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            if employee_name == '' or profession == '' or date_of_birth == '' or contact == '' or username == '' or password == '':
                messagebox.showinfo("Null Info", "All feilds are required to create profile")
            elif self.check_duplicate_user(username):
                db = connection.Connection().get_connection()
                cursor = db.cursor()
                sql = "INSERT INTO employee_details (employee_name, profession, date_of_birth, contact_no, emergency_contact_no) VALUES (%s, %s, %s, %s, %s)"
                val = (employee_name, profession, date_of_birth, contact, emergency_contact)
                sql_1 = "INSERT INTO user_login (username, password) VALUES (%s, %s)"
                val_1 = (username, password)
                cursor.execute(sql, val)
                cursor.execute(sql_1, val_1)
                db.commit()
                messagebox.showinfo("Successful", "Employee profile is created successfully")
            else:
                pass
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error occured: {e}")

    def check_duplicate_user(self, e_username):
        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "select * from user_login;"
            cursor.execute(sql)
            users = cursor.fetchall()
            print(users[0][0])
            for user in users:
                db_username = user[0]
                if e_username == db_username:
                    messagebox.showinfo("Already Exist", "Username already exist")
                else:
                    print("omakr")
        except mysql.connector.Error as e:
            messagebox.showerror("Database error", f"Error occured: {e}")

if __name__ == '__main__':
    app = AddEmployee()
    app.mainloop()