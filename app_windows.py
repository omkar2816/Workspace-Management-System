import itertools

import customtkinter
from tkinter import *
import mysql.connector
from customtkinter import *
from tkinter import messagebox, ttk
from CTkTable import CTkTable
from PIL import Image
import connection
from tkcalendar import Calendar
from calendar import Calendar


LOGO_IMG_DATA = Image.open("images/logo.png")
DASHBOARD_IMG_DATA = Image.open("images/dashboard_icon.png")
EMPLOYEE_IMG_DATA = Image.open("images/employee_icon.png")
PROJECT_IMG_DATA = Image.open("images/project.png")
SALARY_IMG_DATA = Image.open("images/salary_icon.png")
SETTINGS_IMG_DATA = Image.open("images/settings_icon.png")
LOGOUT_IMG_DATA = Image.open("images/log-out.png")
SEARCH_IMG_DATA = Image.open("images/search-icon.png")

COLORS = ["#D60000", "#FF9700", "#005DFF", "#42F200", "#DAE801"]

class DashboardWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        set_appearance_mode("system")
        self.geometry("956x645+350+100")
        # Images
        self.logo_img = CTkImage(dark_image=LOGO_IMG_DATA, light_image=LOGO_IMG_DATA, size=(77.68, 85.42))
        self.dashboard_img = CTkImage(dark_image=DASHBOARD_IMG_DATA, light_image=DASHBOARD_IMG_DATA)
        self.employee_img = CTkImage(dark_image=EMPLOYEE_IMG_DATA, light_image=EMPLOYEE_IMG_DATA)
        self.project_img = CTkImage(dark_image=PROJECT_IMG_DATA, light_image=PROJECT_IMG_DATA)
        self.salary_img = CTkImage(dark_image=SALARY_IMG_DATA, light_image=SALARY_IMG_DATA)
        self.settings_img = CTkImage(dark_image=SETTINGS_IMG_DATA, light_image=SETTINGS_IMG_DATA)
        self.logout_img = CTkImage(dark_image=LOGOUT_IMG_DATA, light_image=LOGOUT_IMG_DATA)
        self.search_img = CTkImage(dark_image=SEARCH_IMG_DATA, light_image=SEARCH_IMG_DATA)

        # Frame creation
        self.side_frame = CTkFrame(master=self, fg_color="#601e88", width=176, height=650, corner_radius=0)
        self.side_frame.pack_propagate(0)
        self.side_frame.pack(fill="y", anchor="w", side="left")

        CTkLabel(master=self.side_frame, text="", image=self.logo_img).pack(pady=(38, 0), anchor="center")

        self.dashboard_button = CTkButton(master=self.side_frame, image=self.dashboard_img, text="Dashboard", fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669", anchor="w", command=self.dashboard)
        self.dashboard_button.pack(anchor="center", ipady=5, pady=(60, 0))

        self.employee_button = CTkButton(master=self.side_frame, image=self.employee_img, text="Employees", fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669", anchor="w", command=self.employees)
        self.employee_button.pack(anchor="center", ipady=5, pady=(16, 0))

        self.project_button = CTkButton(master=self.side_frame, image=self.project_img, text="Projects", fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669", anchor="w", command=self.projects)
        self.project_button.pack(anchor="center", ipady=5, pady=(16, 0))

        self.salary_button = CTkButton(master=self.side_frame, image=self.salary_img, text="Salary", fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669", anchor="w", command=self.salary)
        self.salary_button.pack(anchor="center", ipady=5, pady=(16, 0))

        self.settings_button = CTkButton(master=self.side_frame, image=self.settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669", anchor="w", command=self.settings)
        self.settings_button.pack(anchor="center", ipady=5, pady=(16, 0))

        self.logout_button = CTkButton(master=self.side_frame, image=self.logout_img, text="Log Out", fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669", anchor="w")
        self.logout_button.pack(anchor="center", ipady=5, pady=(160, 0))

        self.window_count = 1
        if self.window_count == 1:
            self.dashboard()

    def dashboard(self):
        if self.window_count == 1:
            pass
        elif self.window_count == 2:
            self.main_frame.destroy()
        elif self.window_count == 3:
            self.main_frame.destroy()
        elif self.window_count == 4:
            self.main_frame.destroy()
        elif self.window_count == 5:
            self.main_frame.destroy()

        if self.window_count == self.window_count:
            pass
        self.main_frame = CTkFrame(master=self, fg_color="#ffffff", width=780, height=650, corner_radius=0)
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(side="left")

        # self.user_button = CTkButton(master=self.main_frame, text="username", fg_color="transparent", font=("Arial Bold", 14), hover_color="#ffffff", anchor="ne")
        self.check_in_frame = CTkFrame(master=self.main_frame, fg_color="#ffffff", width=200, height=30, corner_radius=0)
        self.check_in_frame.pack(anchor="nw", padx=10, pady=(10, 0))
        self.check_in = CTkRadioButton(master=self.check_in_frame, text="Check In", font=("Arial Bold", 14))
        self.check_in.pack(anchor="n", side="left", padx=27, pady=(20, 0))
        self.check_out = CTkRadioButton(master=self.check_in_frame, text="Check Out", font=("Arial Bold", 14))
        self.check_out.pack(anchor="n", side="right", padx=27, pady=(20, 0))

        self.graph_frame = CTkFrame(master=self.main_frame, fg_color="#F0F0F0", width=720, height=280, corner_radius=13)
        self.graph_frame.pack(anchor="center", padx=27, pady=(20, 0))

        self.task_number = 5
        self.complete_task = 10
        self.current = float(self.task_number / self.complete_task)
        self.task_progress_frame = CTkScrollableFrame(master=self.main_frame, fg_color="#F0F0F0", width=345, height=200, corner_radius=13)
        self.task_progress_frame.pack(anchor="n", side="left", padx=(27, 0), pady=(20, 0))

        self.progress_bar_width = 310
        self.label1 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}", width=30).pack(anchor="ne", padx=(0, 25), pady=(5,0))
        self.progress_bar1 = CTkProgressBar(master=self.task_progress_frame, fg_color="#F0F0F0", width=self.progress_bar_width, height=20, corner_radius=8, progress_color=COLORS[0], border_color="#491669", border_width=2)
        self.progress_bar1.pack(anchor="n", padx=10, pady=(5, 0))
        self.progress_bar1.set(self.current)

        self.label2 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}", width=30).pack(
            anchor="ne", padx=(0, 25), pady=(35, 0))
        self.progress_bar2 = CTkProgressBar(master=self.task_progress_frame, fg_color="#F0F0F0", width=self.progress_bar_width, height=20,
                                            corner_radius=8, progress_color=COLORS[1], border_color="#491669", border_width=2)
        self.progress_bar2.pack(anchor="n", padx=10, pady=(5, 0))

        self.label3 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}", width=30).pack(
            anchor="ne", padx=(0, 25), pady=(35, 0))
        self.progress_bar3 = CTkProgressBar(master=self.task_progress_frame, fg_color="#F0F0F0", width=self.progress_bar_width, height=20,
                                            corner_radius=8, progress_color=COLORS[4], border_color="#491669", border_width=2)
        self.progress_bar3.pack(anchor="n", padx=10, pady=(5, 0))

        self.label4 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}", width=30).pack(
            anchor="ne", padx=(0, 25), pady=(35, 0))
        self.progress_bar4 = CTkProgressBar(master=self.task_progress_frame, fg_color="#F0F0F0", width=self.progress_bar_width, height=20,
                                            corner_radius=8, progress_color=COLORS[2], border_color="#491669", border_width=2)
        self.progress_bar4.pack(anchor="n", padx=10, pady=(5, 0))

        self.label5 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}", width=30).pack(
            anchor="ne", padx=(0, 25), pady=(35, 0))
        self.progress_bar5 = CTkProgressBar(master=self.task_progress_frame, fg_color="#F0F0F0", width=self.progress_bar_width, height=20,
                                            corner_radius=8, progress_color=COLORS[3], border_color="#491669", border_width=2)
        self.progress_bar5.pack(anchor="n", padx=10, pady=(5, 0))

        self.calendar_frame = CTkFrame(master=self.main_frame, fg_color="#F0F0F0", width=330, height=230, corner_radius=13)
        self.calendar_frame.pack(anchor="n", side="right", padx=(0, 27), pady=(20, 0))

        # self.cal = Calendar(self.calendar_frame, selectmode="day", date_pattern="y-mm-dd")
        # self.cal.pack(fill="both", expand=True)
        self.window_count = 1

    def employees(self):
        if self.window_count == 1:
            self.main_frame.destroy()
        elif self.window_count == 2:
            pass
        elif self.window_count == 3:
            self.main_frame.destroy()
        elif self.window_count == 4:
            self.main_frame.destroy()
        elif self.window_count == 5:
            self.main_frame.destroy()

        if self.window_count == self.window_count:
            pass
        self.main_frame = CTkFrame(master=self, fg_color="#ffffff", width=780, height=650, corner_radius=0)
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(side="left")

        title_frame = CTkFrame(master=self.main_frame, fg_color="transparent")
        title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        self.label = CTkLabel(master=title_frame, text="Employee & their details", font=("Arial Black", 23),
                              text_color="#601e88")
        self.label.pack(anchor="nw", side="left", pady=(8, 0))

        self.add_employee_button = CTkButton(master=title_frame, text="+ New Employee", font=("Arial Black", 15),
                                             text_color="#fff", fg_color="#601e88", hover_color="#491669",
                                             corner_radius=15, command=self.add_employee)
        self.add_employee_button.pack(anchor="ne", side="right", ipady=10)

        self.search_container = CTkFrame(master=self.main_frame, height=50, fg_color="#F0F0F0")
        self.search_container.pack(fill="x", pady=(30, 0), padx=27)

        self.search_entry = CTkEntry(master=self.search_container, width=650, placeholder_text="Search Employee with its ID or Name",
                                     border_color="#70438C", border_width=2)
        self.search_entry.pack(side="left", padx=(13, 0), pady=15)

        self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color="#601e88", hover_color="#491669", width=28)
        self.search_button.pack(side="left", padx=(13, 0), pady=15)

        self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, colors=["#E6E6E6", "#EEEEEE"], header_color="#601e88",
                              hover_color="#DCDCDC")
        self.table.edit_row(0, text_color="#fff", hover_color="#491669")
        self.table.pack(expand=True)

        self.window_count = 2

    def add_employee(self):
        self.main_frame.destroy()
        self.main_frame = CTkFrame(master=self, fg_color="#ffffff", width=780, height=650, corner_radius=0)
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(side="left")

        self.s_pass = IntVar(value=0)
        self.name_entry = CTkEntry(master=self.main_frame, placeholder_text="Enter name of Employee", height=35, width=330,
                                   fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.name_entry.pack(anchor="n", padx=(25, 25), pady=(80, 0))
        self.profession_entry = CTkComboBox(master=self.main_frame, height=35, width=330, border_color="#601e88",
                                            button_color="#601e88", dropdown_fg_color="#601e88",
                                            dropdown_text_color="#ffffff", dropdown_hover_color="#491669",
                                            button_hover_color="#601e88",
                                            values=["Select Job role", "Administrator", "Engineer", "Management"])
        self.profession_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.date_of_joining_entry = CTkEntry(master=self.main_frame, placeholder_text="Enter Date of Joining i.e. dd/mm/yyyy",
                                              height=35, width=330, fg_color="#EEEEEE", border_color="#601e88",
                                              font=("Arial", 14))
        self.date_of_joining_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.contact_entry = CTkEntry(master=self.main_frame, placeholder_text="Contact No.", height=35, width=330,
                                      fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.contact_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.emergency_contact_entry = CTkEntry(master=self.main_frame, placeholder_text="Emergency Contact No.", height=35,
                                                width=330, fg_color="#EEEEEE", border_color="#601e88",
                                                font=("Arial", 14))
        self.emergency_contact_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.username_entry = CTkEntry(master=self.main_frame, placeholder_text="Username", height=35, width=330,
                                       fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.username_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.password_entry = CTkEntry(master=self.main_frame, placeholder_text="Password", height=35, width=330,
                                       fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14), show="●")
        self.password_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.show_password = CTkCheckBox(master=self.main_frame, checkbox_height=15, checkbox_width=15, text="Show Password ?",
                                         text_color="#7E7E7E", variable=self.s_pass, onvalue=1, offvalue=0,
                                         command=self.toggle_password).pack(anchor="n", padx=(200, 0), pady=(5, 0))
        self.add_button = CTkButton(master=self.main_frame, text="Add Employee", height=35, fg_color="#601e88",
                                    hover_color="#491669", text_color="#ffffff", font=("Arial", 14),
                                    command=self.get_entries).pack(anchor="n", padx=(25, 25), pady=(25, 0))

    def projects(self):
        if self.window_count == 1:
            self.main_frame.destroy()
        elif self.window_count == 2:
            self.main_frame.destroy()
        elif self.window_count == 3:
            pass
        elif self.window_count == self.window_count:
            pass
        elif self.window_count == 4:
            self.main_frame.destroy()
        elif self.window_count == 5:
            self.main_frame.destroy()

        if self.window_count == self.window_count:
            pass
        self.main_frame = CTkFrame(master=self, fg_color="#ffffff", width=780, height=650, corner_radius=0)
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(side="left")

        title_frame = CTkFrame(master=self.main_frame, fg_color="transparent")
        title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        self.label = CTkLabel(master=title_frame, text="Project Details", font=("Arial Black", 23),
                              text_color="#601e88")
        self.label.pack(anchor="nw", side="left", pady=(8, 0))

        self.add_project_button = CTkButton(master=title_frame, text="Create New Project", font=("Arial Black", 15),
                                            text_color="#fff", fg_color="#601e88", hover_color="#491669",
                                            corner_radius=15)
        self.add_project_button.pack(anchor="ne", side="right", ipady=10)

        self.search_container = CTkFrame(master=self.main_frame, height=50, fg_color="#F0F0F0")
        self.search_container.pack(fill="x", pady=(30, 0), padx=27)

        self.search_entry = CTkEntry(master=self.search_container, width=650, placeholder_text="Search Project with Unique ID",
                                     border_color="#70438C", border_width=2)
        self.search_entry.pack(side="left", padx=(13, 0), pady=15)

        self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color="#601e88",
                                       hover_color="#491669", width=28)
        self.search_button.pack(side="left", padx=(13, 0), pady=15)

        self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, colors=["#E6E6E6", "#EEEEEE"], header_color="#601e88",
                              hover_color="#DCDCDC")
        self.table.edit_row(0, text_color="#fff", hover_color="#491669")
        self.table.pack(expand=True)

        self.window_count = 3

    def salary(self):
        if self.window_count == 1:
            self.main_frame.destroy()
        elif self.window_count == 2:
            self.main_frame.destroy()
        elif self.window_count == 3:
            self.main_frame.destroy()
        elif self.window_count == 4:
            pass
        elif self.window_count == self.window_count:
            pass
        elif self.window_count == 5:
            self.main_frame.destroy()

        if self.window_count == self.window_count:
            pass
        self.main_frame = CTkFrame(master=self, fg_color="#ffffff", width=780, height=650, corner_radius=0)
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(side="left")

        # title_frame = CTkFrame(master=self.main_frame, fg_color="transparent")
        # title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        # self.label = CTkLabel(master=title_frame, text="Projects History", font=("Arial Black", 23),
        #                       text_color="#601e88")
        # self.label.pack(anchor="nw", side="left", pady=(8, 0))

        self.search_container = CTkFrame(master=self.main_frame, height=50, fg_color="#F0F0F0")
        self.search_container.pack(anchor="n", fill="x", pady=(30, 0), padx=27)

        self.search_entry = CTkEntry(master=self.search_container, width=650, placeholder_text="Search Employee with  its ID or Name",
                                     border_color="#70438C", border_width=2)
        self.search_entry.pack(side="left", padx=(13, 0), pady=15)

        self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color="#601e88",
                                       hover_color="#491669", width=28)
        self.search_button.pack(side="left", padx=(13, 0), pady=15)

        try:
            db = connection.Connection.get_connection()
            cursor = db.cursor()

            sql = "SELECT * FROM employee_details"
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                print(result)
        except mysql.connector.Error as e:
            print(e)

        self.table_data = [[("ID", "Name", "Profession", "Date of Joining", "Contact No.", "Emergency Contact No.")]]
        self.table_data.append(result)
        self.table_data = list(itertools.chain(*self.table_data))

        self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#601e88",
                              hover_color="#DCDCDC")
        self.table.edit_row(0, text_color="#fff", hover_color="#491669")
        self.table.pack(expand=True)

        self.window_count = 4

    def settings(self):
        if self.window_count == 1:
            self.main_frame.destroy()
        elif self.window_count == 2:
            self.main_frame.destroy()
        elif self.window_count == 3:
            self.main_frame.destroy()
        elif self.window_count == 4:
            self.main_frame.destroy()
        elif self.window_count == 5:
            pass
        elif self.window_count == self.window_count:
            pass

        if self.window_count == self.window_count:
            pass

        self.window_count = 5
        pass

    def toggle_password(self):
        if self.s_pass.get() == 1:
            self.password_entry.configure(show='')
        else:
            self.password_entry.configure(show='●')

    def get_entries(self):
        global username
        employee_name = self.name_entry.get()
        profession = self.profession_entry.get()
        date_of_joining = self.date_of_joining_entry.get()
        contact = self.contact_entry.get()
        emergency_contact = self.emergency_contact_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if employee_name == '' or profession == '' or date_of_joining == '' or contact == '' or username == '' or password == '':
            messagebox.showinfo("Null Info", "All fields are required to create profile")
        elif contact.isdigit() is not True or emergency_contact.isdigit() is not True:
            messagebox.showinfo("Invalid", "Contact number should contain only digits")
        elif len(contact) != 10 or len(emergency_contact) != 10:
            messagebox.showinfo("Invalid", "Contact number should contain 10 digits")
        elif password.isdigit() is not True:
            messagebox.showinfo("Invalid", "Password should contain digits only")
        elif self.check_duplicate_user(username):
            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = "INSERT INTO employee_details (employee_name, profession, date_of_joining, contact_no, emergency_contact_no) VALUES (%s, %s, %s, %s, %s)"
                val = (employee_name, profession, date_of_joining, contact, emergency_contact)

                sql_1 = "INSERT INTO user_login (username, password) VALUES (%s, %s)"
                val_1 = (username, password)

                cursor.execute(sql, val)
                cursor.execute(sql_1, val_1)

                db.commit()
                app.destroy()
                messagebox.showinfo("Successful", "Employee profile is created successfully")
                self.main_frame.destroy()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error occured: {e}")
        else:
            pass

    def check_duplicate_user(self, e_username):
        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "select * from user_login;"
            cursor.execute(sql)
            users = cursor.fetchall()

            for user in users:
                db_username = user[0]
                if e_username == db_username:
                    messagebox.showinfo("Already Exist", "Username already exist")
        except mysql.connector.Error as e:
            messagebox.showerror("Database error", f"Error occured: {e}")


if __name__ == '__main__':
    app = DashboardWindow()
    app.mainloop()