import itertools
import time

import customtkinter
from tkinter import *
import mysql.connector
import pandas as pd
from customtkinter import *
from tkinter import messagebox, ttk
from CTkTable import CTkTable
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

Engineer_salary = 400
Management_salary = 500
Administrative_salary = 300


class DashboardWindow(customtkinter.CTk):
    def __init__(self, username, password):
        super().__init__()
        self.title("Dashboard")
        set_appearance_mode("system")
        self.geometry("956x645+350+100")
        self.username = username
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

        self.dashboard_button = CTkButton(master=self.side_frame, image=self.dashboard_img, text="Dashboard",
                                          fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669",
                                          anchor="w", command=self.dashboard)
        self.dashboard_button.pack(anchor="center", ipady=5, pady=(60, 0))

        self.employee_button = CTkButton(master=self.side_frame, image=self.employee_img, text="Employees",
                                         fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669",
                                         anchor="w", command=self.employees)
        self.employee_button.pack(anchor="center", ipady=5, pady=(16, 0))

        self.project_button = CTkButton(master=self.side_frame, image=self.project_img, text="Projects",
                                        fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669",
                                        anchor="w", command=self.projects)
        self.project_button.pack(anchor="center", ipady=5, pady=(16, 0))

        self.salary_button = CTkButton(master=self.side_frame, image=self.salary_img, text="Salary",
                                       fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669",
                                       anchor="w", command=self.salary)
        self.salary_button.pack(anchor="center", ipady=5, pady=(16, 0))

        self.settings_button = CTkButton(master=self.side_frame, image=self.settings_img, text="Settings",
                                         fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669",
                                         anchor="w", command=self.settings)
        self.settings_button.pack(anchor="center", ipady=5, pady=(16, 0))

        self.logout_button = CTkButton(master=self.side_frame, image=self.logout_img, text="Log Out",
                                       fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669",
                                       anchor="w", command=self.logout_listner)
        self.logout_button.pack(anchor="center", ipady=5, pady=(160, 0))

        self.window_count = 1
        if self.window_count == 1:
            self.dashboard()
            global job
        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "SELECT * FROM employee_details WHERE username=%s"
            val = (username,)

            cursor.execute(sql, val)
            job = cursor.fetchall()
            print(job)
            job = job[0][2]


        except mysql.connector.Error as e:
            print(e)
            messagebox.showerror("Database Error", f"Error Occured :{e}")

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
        self.check_frame = CTkFrame(master=self.main_frame, fg_color="#ffffff", width=200, height=30, corner_radius=0)
        self.check_frame.pack(anchor="nw", padx=10, pady=(10, 0))
        self.radio_var = IntVar(value=0)
        self.check_in = CTkRadioButton(master=self.check_frame, text="Check In", font=("Arial Bold", 14), value=1,
                                       variable=self.radio_var, command=self.stop_timer)
        self.check_in.pack(anchor="n", side="left", padx=27, pady=(20, 0))
        self.check_out = CTkRadioButton(master=self.check_frame, text="Check Out", font=("Arial Bold", 14), value=2,
                                        variable=self.radio_var, command=self.stop_timer)
        self.check_out.pack(anchor="n", side="right", padx=27, pady=(20, 0))

        self.graph_frame = CTkFrame(master=self.main_frame, fg_color="#F0F0F0", width=720, height=280, corner_radius=13)
        self.graph_frame.pack(anchor="center", padx=27, pady=(20, 0))

        global df
        # create a connection to the database
        try:
            db = connection.Connection().get_connection()

            # read the data from the database
            query = 'SELECT employee_name, working_hours  FROM salary'
            df = pd.read_sql(query, con=db)
            print(df)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error Occured: {e}")
            print(e)
        # plot the data as a bar graph
        plt.figure(figsize=(12, 9))
        plt.bar(df['employee_name'], df['working_hours'])
        plt.xlabel('employee name')
        plt.ylabel('time (in hrs)')
        plt.title('analytics')
        # plt.style.use("Solarize_light2")

        # plt.show()
        self.add = plt.gcf()
        canvas = FigureCanvasTkAgg(self.add, master=self.graph_frame)
        canvas.get_tk_widget().configure(width=900, height=360)
        ctk_canvas = canvas.get_tk_widget()
        ctk_canvas.place(relx=0, rely=0, anchor="nw")

        self.task_number = 5
        self.complete_task = 10
        self.current = float(self.task_number / self.complete_task)
        self.task_progress_frame = CTkScrollableFrame(master=self.main_frame, fg_color="#F0F0F0", width=345, height=200,
                                                      corner_radius=13)
        self.task_progress_frame.pack(anchor="n", side="left", padx=(27, 0), pady=(20, 0))

        self.progress_bar_width = 310
        self.label1 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}",
                               width=30).pack(anchor="ne", padx=(0, 25), pady=(5, 0))
        self.progress_bar1 = CTkProgressBar(master=self.task_progress_frame, fg_color="#F0F0F0",
                                            width=self.progress_bar_width, height=20, corner_radius=8,
                                            progress_color=COLORS[0], border_color="#491669", border_width=2)
        self.progress_bar1.pack(anchor="n", padx=10, pady=(5, 0))
        self.progress_bar1.set(self.current)

        self.label2 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}",
                               width=30).pack(
            anchor="ne", padx=(0, 25), pady=(35, 0))
        self.progress_bar2 = CTkProgressBar(master=self.task_progress_frame, fg_color="#F0F0F0",
                                            width=self.progress_bar_width, height=20,
                                            corner_radius=8, progress_color=COLORS[1], border_color="#491669",
                                            border_width=2)
        self.progress_bar2.pack(anchor="n", padx=10, pady=(5, 0))

        self.label3 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}",
                               width=30).pack(
            anchor="ne", padx=(0, 25), pady=(35, 0))
        self.progress_bar3 = CTkProgressBar(master=self.task_progress_frame, fg_color="#F0F0F0",
                                            width=self.progress_bar_width, height=20,
                                            corner_radius=8, progress_color=COLORS[4], border_color="#491669",
                                            border_width=2)
        self.progress_bar3.pack(anchor="n", padx=10, pady=(5, 0))

        # self.label4 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}", width=30).pack(
        #     anchor="ne", padx=(0, 25), pady=(35, 0))
        # self.progress_bar4 = CTkProgressBar(master=self.task_progress_frame, fg_color="#F0F0F0", width=self.progress_bar_width, height=20,
        #                                     corner_radius=8, progress_color=COLORS[2], border_color="#491669", border_width=2)
        # self.progress_bar4.pack(anchor="n", padx=10, pady=(5, 0))
        #
        # self.label5 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}", width=30).pack(
        #     anchor="ne", padx=(0, 25), pady=(35, 0))
        # self.progress_bar5 = CTkProgressBar(master=self.task_progress_frame, fg_color="#F0F0F0", width=self.progress_bar_width, height=20,
        #                                     corner_radius=8, progress_color=COLORS[3], border_color="#491669", border_width=2)
        # self.progress_bar5.pack(anchor="n", padx=10, pady=(5, 0))

        self.calendar_frame = CTkFrame(master=self.main_frame, fg_color="#F0F0F0", width=330, height=230,
                                       corner_radius=13)
        self.calendar_frame.pack(anchor="n", side="right", padx=(0, 27), pady=(20, 0))

        # self.cal = Calendar(self.calendar_frame, selectmode="day", date_pattern="y-mm-dd")
        # self.cal.pack(fill="both", expand=True)
        self.window_count = 1

    def stop_timer(self):
        global stop_time, elapsed_time, salary
        self.val = self.radio_var.get()
        if self.val == 1:
            stop_time = time.time()
        # input("Press enter to stop the timer..."
        elif self.val == 2:
            elapsed_time = time.time() - stop_time
            elapsed_time = round(elapsed_time)
            print(f"time spend {elapsed_time} seconds")
            final_time = (elapsed_time * 10) / 60
            print(final_time)
            if job == 'Engineer':
                salary = final_time * Engineer_salary
            elif job == "Administrator":
                salary = final_time * Administrative_salary
            elif job == "Management":
                salary = final_time * Management_salary
            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = "UPDATE salary SET working_hours=%s, salary=%s WHERE username=%s"
                val = (final_time, salary, self.username,)
                cursor.execute(sql, val)

                db.commit()
            except mysql.connector.Error as e:
                messagebox.showinfo("Database Error", f"Error Occured: {e}")
                print(e)

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

        self.search_entry = CTkEntry(master=self.search_container, width=650,
                                     placeholder_text="Search Employee with its ID or Name",
                                     border_color="#70438C", border_width=2)
        self.search_entry.pack(side="left", padx=(13, 0), pady=15)

        self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color="#601e88",
                                       hover_color="#491669", width=28, command=self.search)
        self.search_button.pack(side="left", padx=(13, 0), pady=15)

        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "SELECT * FROM employee_details"
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                print(result)
        except mysql.connector.Error as e:
            print(e)

        self.table_data = [
            [("ID", "Name", "Profession", "Date of Joining", "Contact No.", "Emergency\nContact No.")]
        ]
        self.table_data.append(results)
        self.table_data = list(itertools.chain(*self.table_data))

        self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", "#EEEEEE"],
                              header_color="#601e88",
                              hover_color="#DCDCDC")
        self.table.edit_row(0, font=("Arial Bold", 14))
        self.table.edit_row(0, text_color="#fff", hover_color="#491669")
        self.table.pack(expand=True)

        self.window_count = 2

    def add_employee(self):
        self.main_frame.destroy()
        self.main_frame = CTkFrame(master=self, fg_color="#ffffff", width=780, height=650, corner_radius=0)
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(side="left")

        self.s_pass = IntVar(value=0)
        self.name_entry = CTkEntry(master=self.main_frame, placeholder_text="Enter name of Employee", height=35,
                                   width=330,
                                   fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.name_entry.pack(anchor="n", padx=(25, 25), pady=(80, 0))
        self.profession_entry = CTkComboBox(master=self.main_frame, height=35, width=330, border_color="#601e88",
                                            button_color="#601e88", dropdown_fg_color="#601e88",
                                            dropdown_text_color="#ffffff", dropdown_hover_color="#491669",
                                            button_hover_color="#601e88",
                                            values=["Select Job role", "Administrator", "Engineer", "Management"])
        self.profession_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.date_of_joining_entry = CTkEntry(master=self.main_frame,
                                              placeholder_text="Enter Date of Joining i.e. dd/mm/yyyy",
                                              height=35, width=330, fg_color="#EEEEEE", border_color="#601e88",
                                              font=("Arial", 14))
        self.date_of_joining_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.contact_entry = CTkEntry(master=self.main_frame, placeholder_text="Contact No.", height=35, width=330,
                                      fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.contact_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.emergency_contact_entry = CTkEntry(master=self.main_frame, placeholder_text="Emergency Contact No.",
                                                height=35,
                                                width=330, fg_color="#EEEEEE", border_color="#601e88",
                                                font=("Arial", 14))
        self.emergency_contact_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.username_entry = CTkEntry(master=self.main_frame, placeholder_text="Username", height=35, width=330,
                                       fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.username_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.password_entry = CTkEntry(master=self.main_frame, placeholder_text="Password", height=35, width=330,
                                       fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14), show="●")
        self.password_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))
        self.show_password = CTkCheckBox(master=self.main_frame, checkbox_height=15, checkbox_width=15,
                                         text="Show Password ?",
                                         text_color="#7E7E7E", variable=self.s_pass, onvalue=1, offvalue=0,
                                         command=self.toggle_password).pack(anchor="n", padx=(200, 0), pady=(5, 0))
        self.add_button = CTkButton(master=self.main_frame, text="Add Employee", height=35, fg_color="#601e88",
                                    hover_color="#491669", text_color="#ffffff", font=("Arial", 14),
                                    command=self.get_entries).pack(anchor="n", padx=(25, 25), pady=(25, 0))

    def get_entries(self):
        global username
        employee_name = self.name_entry.get()
        profession = self.profession_entry.get()
        date_of_joining = self.date_of_joining_entry.get()
        contact = self.contact_entry.get()
        emergency_contact = self.emergency_contact_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if (
                employee_name == '' or profession == '' or date_of_joining == '' or contact == '' or username == '' or password == ''):
            messagebox.showinfo("Null Info", "All fields are required to create profile")
        elif contact.isdigit() is not True or emergency_contact.isdigit() is not True:
            messagebox.showinfo("Invalid", "Contact number should contain only digits")
        elif len(contact) != 10 or len(emergency_contact) != 10:
            messagebox.showinfo("Invalid", "Contact number should contain 10 digits")
        elif password.isdigit() is not True:
            messagebox.showinfo("Invalid", "Password should contain digits only")
        elif not self.check_duplicate_user(username):
            if profession == "Select Job role":
                messagebox.showinfo("change", "Please select your Job role")
            elif profession == "Administrator":
                hourly_salary = 300
            elif profession == "Engineer":
                hourly_salary = 400
            elif profession == "Management":
                hourly_salary = 500
            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = "INSERT INTO employee_details (employee_name, profession, date_of_joining, contact_no, emergency_contact_no) VALUES (%s, %s, %s, %s, %s)"
                val = (employee_name, profession, date_of_joining, contact, emergency_contact)
                sql_2 = "INSERT INTO salary (employee_name, profession, hourly_salary) VALUES (%s, %s, %s)"
                val_2 = (employee_name, profession, str(hourly_salary))

                sql_1 = "INSERT INTO user_login (username, password) VALUES (%s, %s)"
                val_1 = (username, password)

                cursor.execute(sql, val)
                cursor.execute(sql_1, val_1)
                cursor.execute(sql_2, val_2)
                print("name")

                db.commit()
                self.main_frame.destroy()
                messagebox.showinfo("Successful", "Employee profile is created successfully")
                self.main_frame.destroy()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error occured: {e}")
        else:
            print("hello")
        self.employees()

    def search(self):
        search_data = self.search_entry.get()
        global data
        if search_data == '':
            messagebox.showinfo("Null Field", "There is Nothing to Search")
        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "SELECT * FROM employee_details WHERE employee_name=%s"
            val = (search_data,)

            cursor.execute(sql, val)
            data_fetch = cursor.fetchall()
            for data in data_fetch:
                print(data)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error Occured: {e}")
            print(e)
        self.main_frame.destroy()

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

        self.search_entry = CTkEntry(master=self.search_container, width=650,
                                     placeholder_text="Search Employee with its ID or Name",
                                     border_color="#70438C", border_width=2)
        self.search_entry.pack(side="left", padx=(13, 0), pady=15)

        self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color="#601e88",
                                       hover_color="#491669", width=28, command=self.search)
        self.search_button.pack(side="left", padx=(13, 0), pady=15)

        self.table_data = [
            [("ID", "Name", "Profession", "Date of Joining", "Contact No.", "Emergency\nContact No.")]
        ]
        self.table_data.append(data_fetch)
        # print(self.table_data)
        self.table_data = list(itertools.chain(*self.table_data))

        self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", "#EEEEEE"],
                              header_color="#601e88",
                              hover_color="#DCDCDC")
        self.table.edit_row(0, font=("Arial Bold", 14))
        self.table.edit_row(0, text_color="#fff", hover_color="#491669")
        self.table.pack(expand=True)

        self.window_count = 2

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
                                            corner_radius=15, command=self.create_new_project)
        self.add_project_button.pack(anchor="ne", side="right", ipady=10)

        self.search_container = CTkFrame(master=self.main_frame, height=50, fg_color="#F0F0F0")
        self.search_container.pack(fill="x", pady=(30, 0), padx=27)

        self.search_entry = CTkEntry(master=self.search_container, width=650,
                                     placeholder_text="Search Project with Unique ID",
                                     border_color="#70438C", border_width=2)
        self.search_entry.pack(side="left", padx=(13, 0), pady=15)

        self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color="#601e88",
                                       hover_color="#491669", width=28, command=self.search_project)
        self.search_button.pack(side="left", padx=(13, 0), pady=15)

        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "SELECT * FROM project"
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                print(result)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error Occured: {e}")
            print(e)

        self.table_data = [
            [("Unique\nID", "Project Name", "Start Date", "Due Date", "Project\nHead", "Number\nof Tasks",
              "Completed\nTasks")]
        ]

        self.table_data.append(results)
        self.table_data = list(itertools.chain(*self.table_data))

        self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", "#EEEEEE"],
                              header_color="#601e88",
                              hover_color="#DCDCDC")
        self.table.edit_row(0, font=("Arial Bold", 14))
        self.table.edit_row(0, text_color="#fff", hover_color="#491669")
        self.table.edit_column(1, width=200)
        self.table.pack(expand=True)

        self.window_count = 3

    def create_new_project(self):
        self.main_frame.destroy()

        self.main_frame = CTkFrame(master=self, fg_color="#ffffff", width=780, height=650, corner_radius=0)
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(side="left")

        self.s_pass = IntVar(value=0)
        self.project_name_entry = CTkEntry(master=self.main_frame, placeholder_text="Enter name of Project", height=35,
                                           width=330,
                                           fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.project_name_entry.pack(anchor="n", padx=(25, 25), pady=(120, 0))
        self.start_date_entry = CTkEntry(master=self.main_frame,
                                         placeholder_text="Enter Start Date of project i.e. dd/mm/yyyy", height=35,
                                         width=330,
                                         fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.start_date_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))

        self.due_date_entry = CTkEntry(master=self.main_frame,
                                       placeholder_text="Enter Due date of project i.e. dd/mm/yyyy", height=35,
                                       width=330,
                                       fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.due_date_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))

        self.assign_task_entry = CTkEntry(master=self.main_frame,
                                          placeholder_text="Enter name of Employee to assign this project", height=35,
                                          width=330,
                                          fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.assign_task_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))

        self.no_of_tasks_entry = CTkEntry(master=self.main_frame, placeholder_text="Enter Number of Tasks", height=35,
                                          width=330,
                                          fg_color="#EEEEEE", border_color="#601e88", font=("Arial", 14))
        self.no_of_tasks_entry.pack(anchor="n", padx=(25, 25), pady=(25, 0))

        self.create_project_button = CTkButton(master=self.main_frame, text="Create Project", height=35,
                                               fg_color="#601e88",
                                               hover_color="#491669", text_color="#ffffff", font=("Arial", 14),
                                               command=self.get_entries_project).pack(anchor="n", padx=(25, 25),
                                                                                      pady=(25, 0))

    def get_entries_project(self):
        project_name = self.project_name_entry.get()
        start_date = self.start_date_entry.get()
        due_date = self.due_date_entry.get()
        assign_task = self.assign_task_entry.get()
        number_of_tasks = self.no_of_tasks_entry.get()

        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "INSERT INTO project (project_name, start_date, due_date, employee_name, total_tasks, tasks_done) VALUES (%s, %s, %s, %s, %s)"
            val = (project_name, start_date, due_date, assign_task, number_of_tasks)

            # sql_1 = "INSERT INTO user_login (username, password) VALUES (%s, %s)"
            # val_1 = (username, password)

            cursor.execute(sql, val)
            # cursor.execute(sql_1, val_1)
            print("name")

            db.commit()
            # self.main_frame.destroy()
            messagebox.showinfo("Successful", "Project is created successfully")
            self.main_frame.destroy()
            self.projects()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error occured: {e}")

    def search_project(self):
        search_project = self.search_entry.get()

        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "SELECT * FROM project WHERE project_name=%s"
            val = (search_project,)
            cursor.execute(sql, val)

            fetch_project = cursor.fetchall()
            for project in fetch_project:
                print(project)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error Occured: {e}")
            print(e)
        self.main_frame.destroy()

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

        self.search_entry = CTkEntry(master=self.search_container, width=650,
                                     placeholder_text="Search Project with Unique ID",
                                     border_color="#70438C", border_width=2)
        self.search_entry.pack(side="left", padx=(13, 0), pady=15)

        self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color="#601e88",
                                       hover_color="#491669", width=28)
        self.search_button.pack(side="left", padx=(13, 0), pady=15)

        self.table_data = [
            [("Unique\nID", "Project Name", "Start Date", "Due Date", "Project\nHead", "Number\nof Tasks",
              "No. of\nCompleted Tasks")]
        ]

        self.table_data.append(fetch_project)
        self.table_data = list(itertools.chain(*self.table_data))

        self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", "#EEEEEE"],
                              header_color="#601e88",
                              hover_color="#DCDCDC")
        self.table.edit_row(0, font=("Arial Bold", 14))
        self.table.edit_row(0, text_color="#fff", hover_color="#491669")
        self.table.edit_column(1, width=200)
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

        self.search_entry = CTkEntry(master=self.search_container, width=650,
                                     placeholder_text="Search Employee with  its ID or Name",
                                     border_color="#70438C", border_width=2)
        self.search_entry.pack(side="left", padx=(13, 0), pady=15)

        self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color="#601e88",
                                       hover_color="#491669", width=28, command=self.salary_search)
        self.search_button.pack(side="left", padx=(13, 0), pady=15)

        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "SELECT employee_id, employee_name, profession, working_hours, salary FROM salary"
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                print(result)
        except mysql.connector.Error as e:
            print(e)

        self.table_data = [
            [("ID", "Name", "Profession", "Working\nHours", "Salary")]
        ]
        self.table_data.append(results)
        self.table_data = list(itertools.chain(*self.table_data))

        self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", "#EEEEEE"],
                              header_color="#601e88",
                              hover_color="#DCDCDC")
        self.table.edit_row(0, font=("Arial Bold", 14))
        self.table.edit_row(0, text_color="#fff", hover_color="#491669")
        self.table.pack(expand=True)

        self.window_count = 4

    def salary_search(self):
        search_data = self.search_entry.get()
        global data
        if search_data == '':
            messagebox.showinfo("Null Field", "There is Nothing to Search")
        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "SELECT employee_id, employee_name, profession, working_hours, salary FROM salary WHERE %s IN (employee_id, employee_name)"
            val = (search_data,)

            cursor.execute(sql, val)
            data_fetch = cursor.fetchall()
            for data in data_fetch:
                print(data)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error Occured: {e}")
            print(e)
        self.main_frame.destroy()

        self.main_frame = CTkFrame(master=self, fg_color="#ffffff", width=780, height=650, corner_radius=0)
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(side="left")

        self.search_container = CTkFrame(master=self.main_frame, height=50, fg_color="#F0F0F0")
        self.search_container.pack(anchor="n", fill="x", pady=(30, 0), padx=27)

        self.search_entry = CTkEntry(master=self.search_container, width=650,
                                     placeholder_text="Search Employee with  its ID or Name",
                                     border_color="#70438C", border_width=2)
        self.search_entry.pack(side="left", padx=(13, 0), pady=15)

        self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color="#601e88",
                                       hover_color="#491669", width=28)
        self.search_button.pack(side="left", padx=(13, 0), pady=15)

        self.table_data = [
            [("ID", "Name", "Profession", "Working\nHours", "Salary")]
        ]
        self.table_data.append(data_fetch)
        self.table_data = list(itertools.chain(*self.table_data))

        self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", "#EEEEEE"],
                              header_color="#601e88",
                              hover_color="#DCDCDC")
        self.table.edit_row(0, font=("Arial Bold", 14))
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

    def logout_listner(self):
        self.destroy()
        import user_login
        app = user_login.Login()
        app.mainloop()

# if __name__ == '__main__':
#     app = DashboardWindow()
#     app.mainloop()
