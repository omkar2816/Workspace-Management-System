import datetime
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
USER_IMG_DATA = Image.open("images/user_icon.png")
OPEN_IMG_DATA = Image.open("images/open.png")
LOGOUT_IMG2_DATA = Image.open("images/logout_set.png")

COLORS = ["#FFFFFF", "#601E88", "#491669", "#DCDCDC", "#F0F0F0", "#70438C", "#EEEEEE"]
PROGRESS_COLORS = ["#D60000", "#FF9700", "#005DFF", "#42F200", "#DAE801"]
ANCHORS = ["nw", "n", "ne", "w", "center", "e"]
FONTS = ["Arial", "Arial Bold", "Rockwell"]

Engineer_salary = 400
Management_salary = 500
Administrative_salary = 300


class DashboardWindow(customtkinter.CTk):
    def __init__(self, username, password):
        super().__init__()
        self.title("Dashboard")
        set_appearance_mode("Light")
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
        self.user_img = CTkImage(dark_image=USER_IMG_DATA, light_image=USER_IMG_DATA)
        self.open_img = CTkImage(dark_image=OPEN_IMG_DATA, light_image=OPEN_IMG_DATA)
        self.logout_img2 = CTkImage(dark_image=LOGOUT_IMG2_DATA, light_image=LOGOUT_IMG2_DATA)

        # Frame creation
        self.side_frame = CTkFrame(master=self, fg_color= COLORS[1], width=176, height=650, corner_radius=0)
        self.side_frame.pack_propagate(0)
        self.side_frame.pack(fill="y", anchor=ANCHORS[3], side="left")

        CTkLabel(master=self.side_frame, text="", image=self.logo_img).pack(pady=(38, 0), anchor=ANCHORS[4])

        self.dashboard_button = CTkButton(master=self.side_frame, image=self.dashboard_img, text="Dashboard", fg_color="transparent", font=(FONTS[1], 14), hover_color=COLORS[2], anchor=ANCHORS[3], command=self.dashboard)
        self.dashboard_button.pack(anchor=ANCHORS[4], ipady=5, pady=(60, 0))

        self.employee_button = CTkButton(master=self.side_frame, image=self.employee_img, text="Employees", fg_color="transparent", font=(FONTS[1], 14), hover_color=COLORS[2], anchor=ANCHORS[3], command=self.employees)
        self.employee_button.pack(anchor=ANCHORS[4], ipady=5, pady=(16, 0))


        self.project_button = CTkButton(master=self.side_frame, image=self.project_img, text="Projects", fg_color="transparent", font=(FONTS[1], 14), hover_color=COLORS[2], anchor=ANCHORS[3], command=self.projects)
        self.project_button.pack(anchor=ANCHORS[4], ipady=5, pady=(16, 0))

        self.salary_button = CTkButton(master=self.side_frame, image=self.salary_img, text="Salary", fg_color="transparent", font=(FONTS[1], 14), hover_color=COLORS[2], anchor=ANCHORS[3], command=self.salary)
        self.salary_button.pack(anchor=ANCHORS[4], ipady=5, pady=(16, 0))

        self.settings_button = CTkButton(master=self.side_frame, image=self.settings_img, text="Settings", fg_color="transparent", font=(FONTS[1], 14), hover_color=COLORS[2], anchor=ANCHORS[3], command=self.settings)
        self.settings_button.pack(anchor=ANCHORS[4], ipady=5, pady=(16, 0))

        self.logout_button = CTkButton(master=self.side_frame, image=self.logout_img, text="Log Out", fg_color="transparent", font=(FONTS[1], 14), hover_color=COLORS[2], anchor=ANCHORS[3], command=self.logout_listner)
        self.logout_button.pack(anchor=ANCHORS[4], ipady=5, pady=(160, 0))

        self.window_count = 0
        if self.window_count == 0:
            self.dashboard()
            global job
        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "SELECT * FROM employee_details WHERE username=%s"
            val = (username, )

            cursor.execute(sql, val)
            job = cursor.fetchall()
            print(job)
            job = job[0][2]

        except mysql.connector.Error as e:
            print(e)
            messagebox.showerror("Database Error", f"Error Occured :{e}")

    def dashboard(self):
        if self.window_count == 2 or self.window_count == 3 or self.window_count == 3 or self.window_count == 4 or self.window_count == 5 or self.window_count == 6 or self.window_count == 7 or self.window_count == 8 or self.window_count == 9 or self.window_count == 10 or self.window_count == 11 or self.window_count == 12:
            self.main_frame.destroy()
        if self.window_count == 1:
            pass
        else:
            self.main_frame = CTkFrame(master=self, fg_color=COLORS[0], width=780, height=650, corner_radius=0)
            self.main_frame.pack_propagate(0)
            self.main_frame.pack(side="left")

            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = "SELECT employee_name FROM employee_details WHERE username=%s"
                val = (self.username, )
                cursor.execute(sql, val)
                result = cursor.fetchall()
                username = result[0][0]
            except mysql.connector.Error as e:
                print(e)
                messagebox.showerror("Database Error", f"Error Occured:{e}")

            self.profile_button = CTkButton(master=self.main_frame, image=self.user_img, text=f"{username}",
                                            text_color="#000000", fg_color="transparent", width=200, height=35,
                                            font=(FONTS[1], 16), hover_color=COLORS[0], compound="left")
            self.profile_button.pack(anchor=ANCHORS[1], ipady=5, padx=(600, 0), pady=(15, 0))

            # self.user_button = CTkButton(master=self.main_frame, text="username", fg_color="transparent", font=(FONTS[1], 14), hover_color=COLORS[0], anchor=ANCHORS[2])

            self.graph_frame = CTkFrame(master=self.main_frame, fg_color=COLORS[4], width=720, height=280, corner_radius=13)
            self.graph_frame.pack(anchor=ANCHORS[4], padx=27, pady=(20, 0))

            global df, data_fetch
            # create a connection to the database
            try:
                db = connection.Connection().get_connection()

                # read the data from the database
                query = 'SELECT employee_name, working_hours FROM salary ORDER BY working_hours ASC'
                df = pd.read_sql(query, con=db)
                dt = pd.DataFrame(df.sort_values(by="working_hours"))
                print(dt)
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error Occured: {e}")
                print(e)
            # plot the data as a bar graph
            plt.figure(figsize=(12, 9))
            plt.bar(dt['employee_name'], dt['working_hours'])
            plt.xlabel('employee name')
            plt.ylabel('time (in hrs)')
            plt.title('analytics')
            # plt.subplots(facecolor=COLORS[4])
            # plt.style.use("Solarize_light2")


            # plt.show()
            self.add = plt.gcf()
            canvas = FigureCanvasTkAgg(self.add, master=self.graph_frame)
            canvas.get_tk_widget().configure(width=900, height=360)
            ctk_canvas = canvas.get_tk_widget()
            ctk_canvas.place(relx=0, rely=0, anchor=ANCHORS[0])

            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()
                sql = "SELECT unique_id, project_name, total_tasks, tasks_done FROM project WHERE username = %s"
                val = (self.username, )
                cursor.execute(sql, val)
                result = cursor.fetchall()
                print(result)
            except mysql.connector.Error as e:
                print(e)

            self.task_number = int(result[0][2])
            self.complete_task = int(result[0][3])
            self.task_progress_frame = CTkScrollableFrame(master=self.main_frame, fg_color=COLORS[4], width=345, height=210, corner_radius=13)
            self.task_progress_frame.pack(anchor=ANCHORS[1], side="left", padx=(27, 0), pady=(20, 0))

            self.description_frame = CTkScrollableFrame(master=self.main_frame, fg_color=COLORS[4], width=310, height=210,
                                                        corner_radius=13)
            self.description_frame.pack(anchor=ANCHORS[1], side="right", padx=(0, 27), pady=(20, 0))

            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = "SELECT working_task , total_task,project_id FROM project_details"
                # val = (self.username, )
                cursor.execute(sql)
                data_fetch = cursor.fetchall()
                print(data_fetch)
            except mysql.connector.Error as e:
                print(e)
                messagebox.showerror("Database Error", f"Error Occured: {e}")

            self.progress_bar_width = 310
            index = 0
            task_index = 0
            prjt = 0
            for i in range(len(data_fetch)):
                self.task_number = data_fetch[index][task_index]
                self.complete_task = data_fetch[index][task_index+1]
                self.project = data_fetch[index][prjt+2]

                try:
                    db = connection.Connection().get_connection()
                    cursor = db.cursor()

                    sql = "SELECT project_name FROM project"
                    # val = (self.project,)
                    cursor.execute(sql)
                    project_name = cursor.fetchall()
                    project_name = project_name[index][0]
                    print(project_name)
                    sql2 = "SELECT project_name, description FROM project"
                    # val2 = (self.username,)
                    cursor.execute(sql2)
                    result = cursor.fetchall()
                    print(result)
                except mysql.connector.Error as e:
                    print(e)

                progress = self.task_number/self.complete_task
                print(i,progress)

                self.name_frame = CTkFrame(master=self.task_progress_frame, width=50, fg_color="transparent")
                self.name_frame.pack(anchor=ANCHORS[1], fill="x", pady=(10, 0))

                self.label2 = (CTkLabel(master=self.name_frame, text=f"{project_name}",
                                        width=30, fg_color=COLORS[4]).pack(anchor=ANCHORS[3], side="left", padx=(25, 25), pady=(5, 0)))
                self.label1 = (CTkLabel(master=self.name_frame, text=f"{self.task_number}/{self.complete_task}",
                                        width=30, fg_color=COLORS[4]).pack(anchor=ANCHORS[3], side="right", padx=(25, 25), pady=(5, 0)))
                self.progress_bar1 = CTkProgressBar(master=self.task_progress_frame, fg_color=COLORS[4],
                                                    width=self.progress_bar_width, height=20, corner_radius=8,
                                                    progress_color=PROGRESS_COLORS[0], border_color=COLORS[2], border_width=2)
                self.progress_bar1.pack(anchor=ANCHORS[1], padx=10, pady=(5, 0))

                self.progress_bar1.set(progress)

                self.p_name = result[index][0]
                self.p_description = result[index][1]

                self.project_name = CTkTextbox(master=self.description_frame, height=35, fg_color=COLORS[3],
                                               text_color=COLORS[2], font=(FONTS[1], 14))
                self.project_name.pack(anchor=ANCHORS[1], fill="x", padx=(5, 0), pady=(5, 0))
                self.project_name.insert('1.0', self.p_name)

                self.description_label = CTkTextbox(master=self.description_frame, fg_color=COLORS[3], height=100,
                                                    text_color="#000000", font=(FONTS[0], 13))
                self.description_label.pack(anchor=ANCHORS[1], fill="x", padx=(5, 0), pady=(5, 0))
                self.description_label.insert('1.0', self.p_description)

                index += 1
            # self.label1 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}", width=30).pack(anchor=ANCHORS[2], padx=(0, 25), pady=(5,0))
            # self.progress_bar1 = CTkProgressBar(master=self.task_progress_frame, fg_color=COLORS[4], width=self.progress_bar_width, height=20, corner_radius=8, progress_color=COLORS[0], border_color=COLORS[2], border_width=2)
            # self.progress_bar1.pack(anchor=ANCHORS[1], padx=10, pady=(5, 0))
            # self.progress_bar1.set(self.current)
            #
            # self.label2 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}", width=30).pack(
            #     anchor=ANCHORS[2], padx=(0, 25), pady=(35, 0))
            # self.progress_bar2 = CTkProgressBar(master=self.task_progress_frame, fg_color=COLORS[4], width=self.progress_bar_width, height=20,
            #                                     corner_radius=8, progress_color=COLORS[1], border_color=COLORS[2], border_width=2)
            # self.progress_bar2.pack(anchor=ANCHORS[1], padx=10, pady=(5, 0))
            #
            # self.label3 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}", width=30).pack(
            #     anchor=ANCHORS[2], padx=(0, 25), pady=(35, 0))
            # self.progress_bar3 = CTkProgressBar(master=self.task_progress_frame, fg_color=COLORS[4], width=self.progress_bar_width, height=20,
            #                                     corner_radius=8, progress_color=COLORS[4], border_color=COLORS[2], border_width=2)
            # self.progress_bar3.pack(anchor=ANCHORS[1], padx=10, pady=(5, 0))

            # self.label4 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}", width=30).pack(
            #     anchor=ANCHORS[2], padx=(0, 25), pady=(35, 0))
            # self.progress_bar4 = CTkProgressBar(master=self.task_progress_frame, fg_color=COLORS[4], width=self.progress_bar_width, height=20,
            #                                     corner_radius=8, progress_color=COLORS[2], border_color=COLORS[2], border_width=2)
            # self.progress_bar4.pack(anchor=ANCHORS[1], padx=10, pady=(5, 0))
            #
            # self.label5 = CTkLabel(master=self.task_progress_frame, text=f"{self.task_number}/{self.complete_task}", width=30).pack(
            #     anchor=ANCHORS[2], padx=(0, 25), pady=(35, 0))
            # self.progress_bar5 = CTkProgressBar(master=self.task_progress_frame, fg_color=COLORS[4], width=self.progress_bar_width, height=20,
            #                                     corner_radius=8, progress_color=COLORS[3], border_color=COLORS[2], border_width=2)
            # self.progress_bar5.pack(anchor=ANCHORS[1], padx=10, pady=(5, 0))


            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = "SELECT project_name, description FROM project WHERE username=%s"
                val = (self.username, )
                cursor.execute(sql, val)
                result = cursor.fetchall()
                print(result)
            except mysql.connector.Error as e:
                print(e)
                messagebox.showerror("Database Error", f"Error Occured: {e}")

            # for project_name in result:

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
                val = (final_time, salary, self.username, )
                cursor.execute(sql, val)

                db.commit()
            except mysql.connector.Error as e:
                messagebox.showinfo("Database Error", f"Error Occured: {e}")
                print(e)

    def employees(self):
        if self.window_count != 2:
            self.main_frame.destroy()
        if self.window_count == 2:
            pass
        else:
            self.main_frame = CTkFrame(master=self, fg_color=COLORS[0], width=780, height=650, corner_radius=0)
            self.main_frame.pack_propagate(0)
            self.main_frame.pack(side="left")

            title_frame = CTkFrame(master=self.main_frame, fg_color="transparent")
            title_frame.pack(anchor=ANCHORS[1], fill="x", padx=27, pady=(29, 0))

            self.label = CTkLabel(master=title_frame, text="Employee & their details", font=("Arial Black", 23),
                                  text_color=COLORS[1])
            self.label.pack(anchor=ANCHORS[0], side="left", pady=(8, 0))

            self.add_employee_button = CTkButton(master=title_frame, text="+ New Employee", font=("Arial Black", 15),
                                                 text_color="#fff", fg_color=COLORS[1], hover_color=COLORS[2],
                                                 corner_radius=15, command=self.add_employee)
            self.add_employee_button.pack(anchor=ANCHORS[2], side="right", ipady=10)

            self.search_container = CTkFrame(master=self.main_frame, height=50, fg_color=COLORS[4])
            self.search_container.pack(fill="x", pady=(30, 0), padx=27)

            self.search_entry = CTkEntry(master=self.search_container, width=650, placeholder_text="Search Employee with its ID or Name",
                                         border_color=COLORS[5], border_width=2)
            self.search_entry.pack(side="left", padx=(13, 0), pady=15)

            self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color=COLORS[1], hover_color=COLORS[2], width=28, command=self.search)
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
            self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", COLORS[6]], header_color=COLORS[1],
                                  hover_color=COLORS[3])
            self.table.edit_row(0, font=(FONTS[1], 14))
            self.table.edit_row(0, text_color="#fff", hover_color=COLORS[2])
            self.table.pack(expand=True)

            self.window_count = 2

    def add_employee(self):
        if self.window_count != 3:
            self.main_frame.destroy()
        if self.window_count == 3:
            pass
        else:
            self.main_frame.destroy()
            self.main_frame = CTkFrame(master=self, fg_color=COLORS[0], width=780, height=650, corner_radius=0)
            self.main_frame.pack_propagate(0)
            self.main_frame.pack(side="left")

            title_frame = CTkFrame(master=self.main_frame, fg_color="transparent")
            title_frame.pack(anchor=ANCHORS[1], fill="x", padx=27, pady=(29, 0))

            self.label = CTkLabel(master=title_frame, text="Applicant & their details", font=("Arial Black", 23),
                                  text_color=COLORS[1])
            self.label.pack(anchor=ANCHORS[0], side="left", pady=(8, 0))

            self.search_container = CTkFrame(master=self.main_frame, height=50, fg_color=COLORS[4])
            self.search_container.pack(fill="x", pady=(30, 0), padx=27)

            self.request_entry = CTkEntry(master=self.search_container, width=650,
                                          placeholder_text="Search Employee with its ID or Name",
                                          border_color=COLORS[5], border_width=2)
            self.request_entry.pack(side="left", padx=(13, 0), pady=15)

            self.request_button = CTkButton(master=self.search_container, text="", image=self.search_img,
                                            fg_color=COLORS[1],
                                            hover_color=COLORS[2], width=28, command=self.request_to_accept)
            self.request_button.pack(side="left", padx=(13, 0), pady=15)

            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = "SELECT * FROM requests"
                cursor.execute(sql)
                results = cursor.fetchall()
                for result in results:
                    print(result)
            except mysql.connector.Error as e:
                print(e)

            self.table_data = [
                [("Request ID", "Applicants Name", "Profession", "Contact No.", "Emergency\nContact No.")]
            ]
            self.table_data.append(results)
            self.table_data = list(itertools.chain(*self.table_data))

            self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
            self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
            self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", COLORS[6]],
                                  header_color=COLORS[1],
                                  hover_color=COLORS[3])
            self.table.edit_row(0, font=(FONTS[1], 14))
            self.table.edit_row(0, text_color="#fff", hover_color=COLORS[2])
            self.table.pack(expand=True)

            self.window_count = 3

    def request_to_accept(self):
        request_id = self.request_entry.get()
        now = datetime.datetime.now()
        today = now.date()
        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "select  employee_name, profession, contact_no, emergency_contact_no,username from requests where request_id = %s"
            values = (request_id,)

            cursor.execute(sql, values)
            result = cursor.fetchall()
            print(result)

            print(today)
            today = f"{today}"
            result = result[0]
            print(result)
            results = result + (today,)
            sql2 = ("insert into employee_details ( employee_name, profession, "
                    "contact_no, emergency_contact_no, username,date_of_joining) values(%s,%s,%s,%s,%s,%s)")
            values2 = results
            cursor.execute(sql2, values2, )

            sql3 = "delete from requests where request_id =%s"
            values3 = (request_id,)
            cursor.execute(sql3, values3, )

            sql4 = "select * from request_login where username = %s"
            values4 = (result[4],)
            cursor.execute(sql4, values4)
            cred = cursor.fetchall()
            print(cred)

            sql5 = "Insert into user_login(username, password) values(%s,%s)"
            values5 = (cred[0][0], cred[0][1])
            cursor.execute(sql5, values5, )

            sql6 = "delete from request_login where username = %s"
            values6 = (cred[0][0],)
            cursor.execute(sql6, values6)
            db.commit()
            print(result)
            self.main_frame.destroy()
            self.employees()
        except mysql.connector.Error as e:
            print(e)
            
    def get_entries(self):
        global username
        employee_name = self.name_entry.get()
        profession = self.profession_entry.get()
        date_of_joining = self.date_of_joining_entry.get()
        contact = self.contact_entry.get()
        emergency_contact = self.emergency_contact_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if (employee_name == '' or profession == '' or date_of_joining == '' or contact == '' or username == '' or password == ''):
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
        if self.window_count != 4:
            self.main_frame.destroy()
        if self.window_count == 4:
            pass
        else:
            search_data = self.search_entry.get()
            global data
            if search_data == '':
                messagebox.showinfo("Null Field", "There is Nothing to Search")
            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = "SELECT * FROM employee_details WHERE employee_name=%s"
                val = (search_data, )

                cursor.execute(sql, val)
                data_fetch = cursor.fetchall()
                for data in data_fetch:
                    print(data)
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error Occured: {e}")
                print(e)
            self.main_frame.destroy()

            self.main_frame = CTkFrame(master=self, fg_color=COLORS[0], width=780, height=650, corner_radius=0)
            self.main_frame.pack_propagate(0)
            self.main_frame.pack(side="left")

            title_frame = CTkFrame(master=self.main_frame, fg_color="transparent")
            title_frame.pack(anchor=ANCHORS[1], fill="x", padx=27, pady=(29, 0))

            self.label = CTkLabel(master=title_frame, text="Employee & their details", font=("Arial Black", 23),
                                  text_color=COLORS[1])
            self.label.pack(anchor=ANCHORS[0], side="left", pady=(8, 0))

            self.add_employee_button = CTkButton(master=title_frame, text="+ New Employee", font=("Arial Black", 15),
                                                 text_color="#fff", fg_color=COLORS[1], hover_color=COLORS[2],
                                                 corner_radius=15, command=self.add_employee)
            self.add_employee_button.pack(anchor=ANCHORS[2], side="right", ipady=10)

            self.search_container = CTkFrame(master=self.main_frame, height=50, fg_color=COLORS[4])
            self.search_container.pack(fill="x", pady=(30, 0), padx=27)

            self.search_entry = CTkEntry(master=self.search_container, width=650,
                                         placeholder_text="Search Employee with its ID or Name",
                                         border_color=COLORS[5], border_width=2)
            self.search_entry.pack(side="left", padx=(13, 0), pady=15)

            self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color=COLORS[1],
                                           hover_color=COLORS[2], width=28, command=self.search)
            self.search_button.pack(side="left", padx=(13, 0), pady=15)

            self.table_data = [
                [("ID", "Name", "Profession", "Date of Joining", "Contact No.", "Emergency\nContact No.")]
            ]
            self.table_data.append(data_fetch)
            # print(self.table_data)
            self.table_data = list(itertools.chain(*self.table_data))

            self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
            self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
            self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", COLORS[6]],
                                  header_color=COLORS[1],
                                  hover_color=COLORS[3])
            self.table.edit_row(0, font=(FONTS[1], 14))
            self.table.edit_row(0, text_color="#fff", hover_color=COLORS[2])
            self.table.pack(expand=True)

            self.window_count = 4

    def projects(self):
        if self.window_count != 5:
            self.main_frame.destroy()
        if self.window_count == 5:
            pass
        else:
            self.main_frame = CTkFrame(master=self, fg_color=COLORS[0], width=780, height=650, corner_radius=0)
            self.main_frame.pack_propagate(0)
            self.main_frame.pack(side="left")

            title_frame = CTkFrame(master=self.main_frame, fg_color="transparent")
            title_frame.pack(anchor=ANCHORS[1], fill="x", padx=27, pady=(29, 0))

            self.label = CTkLabel(master=title_frame, text="Project Details", font=("Arial Black", 23),
                                  text_color=COLORS[1])
            self.label.pack(anchor=ANCHORS[0], side="left", pady=(8, 0))

            self.add_project_button = CTkButton(master=title_frame, text="Create New Project", font=("Arial Black", 15),
                                                text_color="#fff", fg_color=COLORS[1], hover_color=COLORS[2],
                                                corner_radius=15, command=self.create_new_project)
            self.add_project_button.pack(anchor=ANCHORS[2], side="right", ipady=10)

            self.search_container = CTkFrame(master=self.main_frame, height=50, fg_color=COLORS[4])
            self.search_container.pack(fill="x", pady=(30, 0), padx=27)

            self.search_entry = CTkEntry(master=self.search_container, width=650, placeholder_text="Search Project with Unique ID",
                                         border_color=COLORS[5], border_width=2)
            self.search_entry.pack(side="left", padx=(13, 0), pady=15)

            self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color=COLORS[1],
                                           hover_color=COLORS[2], width=28, command=self.search_project)
            self.search_button.pack(side="left", padx=(13, 0), pady=15)

            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = "SELECT unique_id, project_name, start_date, due_date, total_tasks, tasks_done FROM project"
                cursor.execute(sql)
                results = cursor.fetchall()
                for result in results:
                    print(result)
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error Occured: {e}")
                print(e)

            self.table_data = [
                [("Unique\nID", "Project Name", "Start Date", "Due Date", "Number\nof Tasks", "Completed\nTasks")]
            ]

            self.table_data.append(results)
            self.table_data = list(itertools.chain(*self.table_data))

            self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
            self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
            self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", COLORS[6]], header_color=COLORS[1],
                                  hover_color=COLORS[3])
            self.table.edit_row(0, font=(FONTS[1], 14))
            self.table.edit_row(0, text_color="#fff", hover_color=COLORS[2])
            self.table.edit_column(1, width=200)
            self.table.pack(expand=True)

            self.window_count = 5

    def create_new_project(self):
        if self.window_count != 6:
            self.main_frame.destroy()
        if self.window_count == 6:
            pass
        else:
            self.main_frame.destroy()

            self.main_frame = CTkFrame(master=self, fg_color=COLORS[0], width=780, height=650, corner_radius=0)
            self.main_frame.pack_propagate(0)
            self.main_frame.pack(side="left")

            self.s_pass = IntVar(value=0)
            self.label = CTkLabel(master=self.main_frame, text="Creating New Project....", fg_color="transparent", text_color=COLORS[1], font=(FONTS[1], 25))
            self.label.pack(anchor=ANCHORS[0], padx=(25, 25), pady=(40, 0))

            self.project_name_entry = CTkEntry(master=self.main_frame, placeholder_text="Enter name of Project", height=35, width=330,
                                       fg_color=COLORS[6], border_color=COLORS[1], font=(FONTS[0], 14))
            self.project_name_entry.pack(anchor=ANCHORS[1], padx=(25, 25), pady=(60, 0))
            # self.start_date_entry = CTkEntry(master=self.main_frame, placeholder_text="Enter Start Date of project i.e. dd/mm/yyyy", height=35, width=330,
            #                            fg_color=COLORS[6], border_color=COLORS[1], font=(FONTS[0], 14))
            # self.start_date_entry.pack(anchor=ANCHORS[1], padx=(25, 25), pady=(25, 0))

            self.due_date_entry = CTkEntry(master=self.main_frame, placeholder_text="Enter Due date of project i.e. dd/mm/yyyy", height=35, width=330,
                                       fg_color=COLORS[6], border_color=COLORS[1], font=(FONTS[0], 14))
            self.due_date_entry.pack(anchor=ANCHORS[1], padx=(25, 25), pady=(25, 0))

            # self.number_of_participants = CTkEntry(master=self.main_frame, placeholder_text="Enter Number of Participants", height=35, width=330,
            #                            fg_color=COLORS[6], border_color=COLORS[1], font=(FONTS[0], 14))
            # self.number_of_participants.pack(anchor=ANCHORS[1], padx=(25, 25), pady=(25, 0))
            self.assign_task_entry = CTkEntry(master=self.main_frame, placeholder_text="Enter name of Employee to assign this project", height=35, width=330,
                                               fg_color=COLORS[6], border_color=COLORS[1], font=(FONTS[0], 14))
            self.assign_task_entry.pack(anchor=ANCHORS[1], padx=(25, 25), pady=(25, 0))

            self.no_of_tasks_entry = CTkEntry(master=self.main_frame, placeholder_text="Enter Number of Tasks", height=35, width=330,
                                               fg_color=COLORS[6], border_color=COLORS[1], font=(FONTS[0], 14))
            self.no_of_tasks_entry.pack(anchor=ANCHORS[1], padx=(25, 25), pady=(25, 0))

            self.description_entry = CTkTextbox(master=self.main_frame, height=100, width=330, fg_color=COLORS[6], border_width=2, border_color=COLORS[1], font=(FONTS[0], 14))
            self.description_entry.pack(anchor=ANCHORS[1], padx=(25, 25), pady=(25, 0))

            self.create_project_button = CTkButton(master=self.main_frame, text="Create Project", height=35, fg_color=COLORS[1],
                                        hover_color=COLORS[2], text_color=COLORS[0], font=(FONTS[0], 14),
                                        command=self.get_entries_project).pack(anchor=ANCHORS[1], padx=(25, 25), pady=(25, 0))

            self.assign_project_button = CTkButton(master=self.main_frame, text="Assign existing Project", height=35,
                                                   fg_color="transparent",
                                                   hover_color=COLORS[0], text_color="#7E7E7E", font=(FONTS[0], 13, "underline"),
                                                   command=self.assign_project).pack(anchor=ANCHORS[1], padx=(25, 25),
                                                                                          pady=(20, 0))

            self.window_count = 6

    def get_entries_project(self):

        project_name = self.project_name_entry.get()
        start_date = datetime.datetime.now().date()
        due_date = self.due_date_entry.get()
        assign_task = self.assign_task_entry.get()
        assign_task = [int(x) for x in assign_task.split(',')]
        project_description = self.description_entry.get('0.0', "end")
        number_of_tasks = self.no_of_tasks_entry.get()
        number_of_tasks = [int(x) for x in number_of_tasks.split(',')]

        if len(assign_task) < len(number_of_tasks):
            messagebox.showinfo("", "Number of Employees and Number of tasks should be same")
        elif len(assign_task) > len(number_of_tasks):
            messagebox.showinfo("", "Number of Employees and Number of tasks should be same")
        else:
            print(f"assign tasks:{assign_task}, datatype={type(assign_task)}")
            print(f"number_of tasks:{number_of_tasks}, datatype={type(number_of_tasks)}")

            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = ("INSERT INTO project (project_name, start_date, due_date, participants, tasks, description) "
                       "VALUES (%s, %s, %s, %s, %s, %s)")
                val = (project_name, start_date, due_date, str(assign_task), str(number_of_tasks), project_description)

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


            try:
                pass
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error Occured:{e}")


            index = 0
            for i in range(len(assign_task)):
                try:
                    db = connection.Connection().get_connection()
                    cursor = db.cursor()

                    sql = "SELECT * FROM project"
                    cursor.execute(sql)

                    result = cursor.fetchall()
                    project_details = result[-1]
                    id = project_details[0]
                    print(id)
                    print(project_details)

                    db = connection.Connection().get_connection()
                    cursor = db.cursor()

                    sql4 = "SELECT username FROM employee_details WHERE employee_id=%s"
                    val4 = (assign_task[index], )

                    cursor.execute(sql4, val4)
                    user = cursor.fetchall()
                    print(user)
                    user = user[0][0]
                    print(user)

                    sql1 = "SELECT project FROM employee_details WHERE username=%s"
                    val1 = (user, )
                    cursor.execute(sql1, val1)
                    result1 = cursor.fetchall()
                    result1 = result1[0][0]

                    import ast
                    result1 = ast.literal_eval(result1)
                    # print(type(result1))
                    print(result1)
                    result1.append(id)
                    sql2 = "UPDATE employee_details SET project = %s WHERE username = %s"
                    val2 = (str(result1), user)
                    cursor.execute(sql2, val2)
                    db.commit()

                    starting_working_task = 0
                    sql3 = "INSERT INTO project_details (project_id, username, total_task, working_task) VALUES(%s,%s,%s,%s)"
                    val3 = (id, user, number_of_tasks[index], starting_working_task)

                    cursor.execute(sql3, val3)
                    db.commit()

                    index += 1

                except mysql.connector.Error as e:
                    messagebox.showerror("Database Error", f"Error Occured: {e}")
    def final_task_list(self,a,b):
        c = a+b
        return c


    def search_project(self):
        if self.window_count != 7:
            self.main_frame.destroy()
        if self.window_count == 7:
            pass
        else:
            search_project = self.search_entry.get()

            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = "SELECT * FROM project WHERE project_name=%s"
                val = (search_project, )
                cursor.execute(sql, val)

                fetch_project = cursor.fetchall()
                for project in fetch_project:
                    print(project)
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error Occured: {e}")
                print(e)
            self.main_frame.destroy()

            self.main_frame = CTkFrame(master=self, fg_color=COLORS[0], width=780, height=650, corner_radius=0)
            self.main_frame.pack_propagate(0)
            self.main_frame.pack(side="left")

            title_frame = CTkFrame(master=self.main_frame, fg_color="transparent")
            title_frame.pack(anchor=ANCHORS[1], fill="x", padx=27, pady=(29, 0))

            self.label = CTkLabel(master=title_frame, text="Project Details", font=("Arial Black", 23),
                                  text_color=COLORS[1])
            self.label.pack(anchor=ANCHORS[0], side="left", pady=(8, 0))

            self.add_project_button = CTkButton(master=title_frame, text="Create New Project", font=("Arial Black", 15),
                                                text_color="#fff", fg_color=COLORS[1], hover_color=COLORS[2],
                                                corner_radius=15)
            self.add_project_button.pack(anchor=ANCHORS[2], side="right", ipady=10)

            self.search_container = CTkFrame(master=self.main_frame, height=50, fg_color=COLORS[4])
            self.search_container.pack(fill="x", pady=(30, 0), padx=27)

            self.search_entry = CTkEntry(master=self.search_container, width=650,
                                         placeholder_text="Search Project with Unique ID",
                                         border_color=COLORS[5], border_width=2)
            self.search_entry.pack(side="left", padx=(13, 0), pady=15)

            self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color=COLORS[1],
                                           hover_color=COLORS[2], width=28)
            self.search_button.pack(side="left", padx=(13, 0), pady=15)

            self.table_data = [
                [("Unique\nID", "Project Name", "Start Date", "Due Date", "Project\nHead", "Number\nof Tasks", "No. of\nCompleted Tasks")]
            ]

            self.table_data.append(fetch_project)
            self.table_data = list(itertools.chain(*self.table_data))

            self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
            self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
            self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", COLORS[6]],
                                  header_color=COLORS[1],
                                  hover_color=COLORS[3])
            self.table.edit_row(0, font=(FONTS[1], 14))
            self.table.edit_row(0, text_color="#fff", hover_color=COLORS[2])
            self.table.edit_column(1, width=200)
            self.table.pack(expand=True)

            self.window_count = 7

    def assign_project(self):
        if self.window_count != 8:
            self.main_frame.destroy()
        if self.window_count == 8:
            pass
        else:
            self.main_frame.destroy()

            self.main_frame = CTkFrame(master=self, fg_color=COLORS[0], width=780, height=650, corner_radius=0)
            self.main_frame.pack_propagate(0)
            self.main_frame.pack(side="left", fill="y")

            title_frame = CTkFrame(master=self.main_frame, fg_color="transparent")
            title_frame.pack(anchor=ANCHORS[1], fill="x", padx=27, pady=(29, 0))

            self.label = CTkLabel(master=title_frame, text="Project Details", font=("Arial Black", 23),
                                  text_color=COLORS[1])
            self.label.pack(anchor=ANCHORS[0], side="left", pady=(8, 0))

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
            self.table_frame.pack(expand=True, fill="both", padx=27, pady=(21, 0))
            self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", COLORS[6]],
                                  header_color=COLORS[1],
                                  hover_color=COLORS[3])
            self.table.edit_row(0, font=(FONTS[1], 14))
            self.table.edit_row(0, text_color="#fff", hover_color=COLORS[2])
            self.table.edit_column(1, width=200)
            self.table.pack(expand=True)

            entry_frame = CTkFrame(master=self.main_frame, fg_color="transparent")
            entry_frame.pack(anchor=ANCHORS[1], fill="x", padx=27, pady=(10, 0))

            self.employee_id_entry = CTkEntry(master=entry_frame, placeholder_text="Enter Employee_ID", width=290, height=35, border_color=COLORS[1], font=(FONTS[1], 14))
            self.employee_id_entry.pack(anchor=ANCHORS[0], side="left", padx=(55, 25), pady=(10, 0))

            self.project_id_entry = CTkEntry(master=entry_frame, placeholder_text="Enter Project_ID", width=290, height=35, border_color=COLORS[1], font=(FONTS[1], 14))
            self.project_id_entry.pack(anchor=ANCHORS[0], side="right", padx=(25, 55), pady=(10, 0))

            self.assign_button = CTkButton(master=self.main_frame, text="Assign Project", height=35, fg_color=COLORS[1], hover_color=COLORS[2], font=(FONTS[1], 14))
            self.assign_button.pack(anchor=ANCHORS[4], padx=(25, 25), pady=10)

            self.window_count = 8

    def salary(self):
        if self.window_count != 9:
            self.main_frame.destroy()
        if self.window_count == 9:
            pass
        else:
            self.main_frame = CTkFrame(master=self, fg_color=COLORS[0], width=780, height=650, corner_radius=0)
            self.main_frame.pack_propagate(0)
            self.main_frame.pack(side="left")

            # title_frame = CTkFrame(master=self.main_frame, fg_color="transparent")
            # title_frame.pack(anchor=ANCHORS[1], fill="x", padx=27, pady=(29, 0))

            # self.label = CTkLabel(master=title_frame, text="Projects History", font=("Arial Black", 23),
            #                       text_color=COLORS[1])
            # self.label.pack(anchor=ANCHORS[0], side="left", pady=(8, 0))

            self.search_container = CTkFrame(master=self.main_frame, height=50, fg_color=COLORS[4])
            self.search_container.pack(anchor=ANCHORS[1], fill="x", pady=(30, 0), padx=27)

            self.search_entry = CTkEntry(master=self.search_container, width=650, placeholder_text="Search Employee with  its ID or Name",
                                         border_color=COLORS[5], border_width=2)
            self.search_entry.pack(side="left", padx=(13, 0), pady=15)

            self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color=COLORS[1],
                                           hover_color=COLORS[2], width=28, command=self.salary_search)
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
            self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", COLORS[6]], header_color=COLORS[1],
                                  hover_color=COLORS[3])
            self.table.edit_row(0, font=(FONTS[1], 14))
            self.table.edit_row(0, text_color="#fff", hover_color=COLORS[2])
            self.table.pack(expand=True)

            self.window_count = 9

    def salary_search(self):
        if self.window_count != 10:
            self.main_frame.destroy()
        if self.window_count == 10:
            pass
        else:
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

            self.main_frame = CTkFrame(master=self, fg_color=COLORS[0], width=780, height=650, corner_radius=0)
            self.main_frame.pack_propagate(0)
            self.main_frame.pack(side="left")

            self.search_container = CTkFrame(master=self.main_frame, height=50, fg_color=COLORS[4])
            self.search_container.pack(anchor=ANCHORS[1], fill="x", pady=(30, 0), padx=27)

            self.search_entry = CTkEntry(master=self.search_container, width=650,
                                         placeholder_text="Search Employee with  its ID or Name",
                                         border_color=COLORS[5], border_width=2)
            self.search_entry.pack(side="left", padx=(13, 0), pady=15)

            self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color=COLORS[1],
                                           hover_color=COLORS[2], width=28)
            self.search_button.pack(side="left", padx=(13, 0), pady=15)

            self.table_data = [
                [("ID", "Name", "Profession", "Working\nHours", "Salary")]
            ]
            self.table_data.append(data_fetch)
            self.table_data = list(itertools.chain(*self.table_data))

            self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
            self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
            self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", COLORS[6]],
                                  header_color=COLORS[1],
                                  hover_color=COLORS[3])
            self.table.edit_row(0, font=(FONTS[1], 14))
            self.table.edit_row(0, text_color="#fff", hover_color=COLORS[2])
            self.table.pack(expand=True)

            self.window_count = 10

    def settings(self):
        if self.window_count != 11:
            self.main_frame.destroy()
        if self.window_count == 11:
            pass
        else:
            self.main_frame.destroy()

            self.main_frame = CTkFrame(master=self, fg_color=COLORS[0], width=780, height=650, corner_radius=0)
            self.main_frame.pack_propagate(0)
            self.main_frame.pack(side="left")

            self.edit_profile_button = CTkButton(master=self.main_frame, image=self.open_img,
                                                 text="     Edit Profile                                                                                             ",
                                                 width=620, height=60, fg_color=COLORS[1], font=(FONTS[2], 22),
                                                 hover_color=COLORS[2], anchor=ANCHORS[3], compound="right",
                                                 command=self.update_profile).pack(anchor=ANCHORS[4], fill="x", padx=30,
                                                                                   ipadx=10, ipady=10, pady=(70, 0))
            self.theme_button = CTkButton(master=self.main_frame, image=self.open_img,
                                          text="     Set appearance mode                                                                         ",
                                          height=60, fg_color=COLORS[1], font=(FONTS[2], 22), hover_color=COLORS[2],
                                          anchor=ANCHORS[3], compound="right").pack(anchor=ANCHORS[4], fill="x", padx=30, ipadx=10,
                                                                             ipady=10, pady=(25, 0))
            self.logout_button = CTkButton(master=self.main_frame, image=self.logout_img2,
                                           text="     Log out                                                                                                    ",
                                           height=60, fg_color=COLORS[1], font=(FONTS[2], 22), hover_color=COLORS[2],
                                           anchor=ANCHORS[3], compound="right", command=self.logout_listner).pack(anchor=ANCHORS[4], fill="x", padx=30, ipadx=10,
                                                                              ipady=10, pady=(25, 0))

            self.window_count = 11

    def save_changes(self):
        e_id = self.employee_id.get()
        e_name = self.employee_name.get()
        e_doj = self.date_of_joining.get()
        e_contact = self.contact_no.get()
        e_emer_conatct = self.emergency_contact.get()
        # e_username = self.username_entry.get()
        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "UPDATE employee_details SET employee_id = %s, employee_name = %s, date_of_joining = %s, contact_no = %s, emergency_contact_no = %s WHERE username=%s"
            val = (e_id, e_name, e_doj, e_contact, e_emer_conatct, self.username)
            cursor.execute(sql, val)
            db.commit()
            messagebox.showinfo("Successful", "Data has been updated successfully")
            self.main_frame.destroy()
            self.settings()
        except mysql.connector.Error as e:
            print(e)
            messagebox.showerror("Database Error", f"Error Occured:{e}")

    def update_profile(self):
        if self.window_count != 12:
            self.main_frame.destroy()
        if self.window_count == 12:
            pass
        else:
            self.main_frame.destroy()

            self.main_frame = CTkFrame(master=self, fg_color=COLORS[0], width=780, height=650, corner_radius=0)
            self.main_frame.pack_propagate(0)
            self.main_frame.pack(side="left")

            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = "SELECT employee_id, employee_name, date_of_joining, contact_no, emergency_contact_no, username FROM employee_details WHERE username=%s"
                val = (self.username, )
                cursor.execute(sql, val)
                results = cursor.fetchall()
                print(results)
            except mysql.connector.Error as e:
                print(e)
                messagebox.showerror("Database Error", f"Error Occured: {e}")

            global id, name, doj, contact, e_contact, username
            for result in results:
                id = result[0]
                name = result[1]
                doj = result[2]
                contact = result[3]
                e_contact = result[4]
                username = result[5]

            self.id_label = CTkLabel(master=self.main_frame, text="Employee ID:", width=350, font=(FONTS[1], 14), text_color=COLORS[1])
            self.id_label.pack(anchor=ANCHORS[0], padx=(100, 25), pady=(60, 0))
            self.employee_id = CTkEntry(master=self.main_frame, width=330, height=35, border_color=COLORS[1], fg_color=COLORS[6], font=(FONTS[1], 14))
            self.employee_id.pack(anchor=ANCHORS[1], padx=(25, 25), pady=(5, 0))
            self.employee_id.insert(0, id)

            self.name_label = CTkLabel(master=self.main_frame, text="Name:", width=350, font=(FONTS[1], 14), text_color=COLORS[1])
            self.name_label.pack(anchor=ANCHORS[0], padx=(77, 25), pady=(10, 0))
            self.employee_name = CTkEntry(master=self.main_frame, width=330, height=35, border_color=COLORS[1], fg_color=COLORS[6], font=(FONTS[1], 14))
            self.employee_name.pack(anchor=ANCHORS[1], padx=(25, 25), pady=(5, 0))
            self.employee_name.insert(0, name)

            self.doj_label = CTkLabel(master=self.main_frame, text="Date of Joining:", width=350, font=(FONTS[1], 14),
                                       text_color=COLORS[1])
            self.doj_label.pack(anchor=ANCHORS[0], padx=(107, 25), pady=(10, 0))
            self.date_of_joining = CTkEntry(master=self.main_frame, width=330, height=35, border_color=COLORS[1], fg_color=COLORS[6], font=(FONTS[1], 14))
            self.date_of_joining.pack(anchor=ANCHORS[1], padx=(25, 25), pady=(5, 0))
            self.date_of_joining.insert(0, doj)

            self.contact_label = CTkLabel(master=self.main_frame, text="Contact No.:", width=350, font=(FONTS[1], 14),
                                       text_color=COLORS[1])
            self.contact_label.pack(anchor=ANCHORS[0], padx=(97, 25), pady=(10, 0))
            self.contact_no = CTkEntry(master=self.main_frame, width=330, height=35, border_color=COLORS[1], fg_color=COLORS[6], font=(FONTS[1], 14))
            self.contact_no.pack(anchor=ANCHORS[1], padx=(25, 25), pady=(5, 0))
            self.contact_no.insert(0, contact)

            self.e_contact_label = CTkLabel(master=self.main_frame, text="Emergency Contact No.:", width=350, font=(FONTS[1], 14),
                                       text_color=COLORS[1])
            self.e_contact_label.pack(anchor=ANCHORS[0], padx=(140, 25), pady=(10, 0))
            self.emergency_contact = CTkEntry(master=self.main_frame, width=330, height=35, border_color=COLORS[1], fg_color=COLORS[6], font=(FONTS[1], 14))
            self.emergency_contact.pack(anchor=ANCHORS[1], padx=(25, 25), pady=(5, 0))
            self.emergency_contact.insert(0, e_contact)

            # self.username_label = CTkLabel(master=self.main_frame, text="Username:", width=350, font=(FONTS[1], 14),
            #                            text_color=COLORS[1])
            # self.username_label.pack(anchor=ANCHORS[0], padx=(93, 25), pady=(10, 0))
            # self.username_entry = CTkEntry(master=self.main_frame, width=330, height=35, border_color=COLORS[1], fg_color=COLORS[6], font=(FONTS[1], 14))
            # self.username_entry.pack(anchor=ANCHORS[1], padx=(25, 25), pady=(5, 0))
            # self.username_entry.insert(0, username)
            # self.password = CTkEntry(master=self.main_frame)
            # self.password.pack()
            # self.show_password = CTkCheckBox(master=self.main_frame)
            # self.show_password.pack()

            self.save_changes = CTkButton(master=self.main_frame, height=40, width=150, fg_color=COLORS[1], hover_color=COLORS[2], text="Save Changes", font=(FONTS[1], 14), command=self.save_changes)
            self.save_changes.pack(anchor=ANCHORS[1], padx=(25, 25), pady=(25, 0))

            self.window_count = 12

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
        import admin_login
        login = admin_login.Starter()
        login.mainloop()


# if __name__ == '__main__':
#     app = DashboardWindow()
#     app.mainloop()