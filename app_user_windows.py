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
from demo import TimerApp

LOGO_IMG_DATA = Image.open("images/logo.png")
DASHBOARD_IMG_DATA = Image.open("images/dashboard_icon.png")
EMPLOYEE_IMG_DATA = Image.open("images/employee_icon.png")
PROJECT_IMG_DATA = Image.open("images/project.png")
SALARY_IMG_DATA = Image.open("images/salary_icon.png")
SETTINGS_IMG_DATA = Image.open("images/settings_icon.png")
LOGOUT_IMG_DATA = Image.open("images/log-out.png")
SEARCH_IMG_DATA = Image.open("images/search-icon.png")
OPEN_IMG_DATA = Image.open("images/open.png")
LOGOUT_IMG2_DATA = Image.open("images/logout_set.png")
USER_IMG_DATA = Image.open("images/user_icon.png")

COLORS = ["#D60000", "#FF9700", "#005DFF", "#42F200", "#DAE801"]


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
        self.open_img = CTkImage(dark_image=OPEN_IMG_DATA, light_image=OPEN_IMG_DATA)
        self.logout_img2 = CTkImage(dark_image=LOGOUT_IMG2_DATA, light_image=LOGOUT_IMG2_DATA)
        self.user_img = CTkImage(dark_image=USER_IMG_DATA, light_image=USER_IMG_DATA)

        # Frame creation
        self.side_frame = CTkFrame(master=self, fg_color="#601e88", width=176, height=650, corner_radius=0)
        self.side_frame.pack_propagate(0)
        self.side_frame.pack(fill="y", anchor="w", side="left")

        CTkLabel(master=self.side_frame, text="", image=self.logo_img).pack(pady=(38, 0), anchor="center")

        self.dashboard_button = CTkButton(master=self.side_frame, image=self.dashboard_img, text="Dashboard", fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669", anchor="w", command=self.dashboard)
        self.dashboard_button.pack(anchor="center", ipady=5, pady=(60, 0))

        self.employee_button = CTkButton(master=self.side_frame, image=self.employee_img, text="Colleagues", fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669", anchor="w", command=self.employees)
        self.employee_button.pack(anchor="center", ipady=5, pady=(16, 0))

        self.project_button = CTkButton(master=self.side_frame, image=self.project_img, text="Projects", fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669", anchor="w", command=self.projects)
        self.project_button.pack(anchor="center", ipady=5, pady=(16, 0))

        # self.salary_button = CTkButton(master=self.side_frame, image=self.salary_img, text="Salary", fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669", anchor="w", command=self.salary)
        # self.salary_button.pack(anchor="center", ipady=5, pady=(16, 0))

        self.settings_button = CTkButton(master=self.side_frame, image=self.settings_img, text="Settings", fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669", anchor="w", command=self.settings)
        self.settings_button.pack(anchor="center", ipady=5, pady=(16, 0))

        self.logout_button = CTkButton(master=self.side_frame, image=self.logout_img, text="Log Out", fg_color="transparent", font=("Arial Bold", 14), hover_color="#491669", anchor="w", command=self.logout_listner)
        self.logout_button.pack(anchor="center", ipady=5, pady=(160, 0))

        self.window_count = 1
        if self.window_count == 1:
            self.dashboard()

        self.counter = 0
        self.timer_running = False

        self.protocol("WM_DELETE_WINDOW", self.stop_timer)

        self.start_timer()

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def stop_timer(self):
        global time
        self.timer_running = False
        time = round(float(self.counter))
        print(time)
        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "UPDATE salary SET working_hours = working_hours + %s WHERE username=%s"
            val = (time, self.username, )

            cursor.execute(sql, val)
            db.commit()
        except mysql.connector.Error as e:
            print(e)
            messagebox.showerror("Database Error", f"Error Occured: {e}")
        self.destroy()

    def update_timer(self):
        if self.timer_running:
            self.counter += 1
            # self.config(text=str(self.counter))
            self.after(1000, self.update_timer)

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

        # self.user_button = CTkButton(master=self.main_frame, text="username", fg_color="transparent", font=("Arial Bold", 14), hover_color="#ffffff", anchor="ne")
        self.profile_button = CTkButton(master=self.main_frame, image=self.user_img, text=f"{username}", text_color="#000000", fg_color="transparent", width=200, height=35, font=("Arial Bold", 16), hover_color="#ffffff", compound="left")
        self.profile_button.pack(anchor="n", ipady=5, padx=(600, 0), pady=(15, 0))

        self.graph_frame = CTkFrame(master=self.main_frame, fg_color="#F0F0F0", width=720, height=280, corner_radius=13)
        self.graph_frame.pack(anchor="center", padx=27, pady=(15, 0))

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
        self.task_progress_frame = CTkScrollableFrame(master=self.main_frame, fg_color="#F0F0F0", width=345, height=210, corner_radius=13)
        self.task_progress_frame.pack(anchor="n", side="left", padx=(27, 0), pady=(20, 0))

        self.description_frame = CTkScrollableFrame(master=self.main_frame, fg_color="#F0F0F0", width=310, height=210,
                                                    corner_radius=13)
        self.description_frame.pack(anchor="n", side="right", padx=(0, 27), pady=(20, 0))

        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "SELECT working_task , total_task,project_id FROM project_details WHERE username=%s"
            val = (self.username, )
            cursor.execute(sql, val)
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

                sql = "SELECT project_name FROM project WHERE unique_id=%s"
                val = (self.project,)
                cursor.execute(sql, val)
                project_name = cursor.fetchall()
                print(project_name)
                sql2 = "SELECT project_name, description FROM project WHERE unique_id=%s"
                # val2 = (self.username,)
                cursor.execute(sql2, val)
                result = cursor.fetchall()
                print(result)
            except mysql.connector.Error as e:
                print(e)
            index += 1
            progress = self.task_number/self.complete_task
            print(i,progress)

            self.name_frame = CTkFrame(master=self.task_progress_frame, width=50, fg_color="transparent")
            self.name_frame.pack(anchor="n", fill="x", pady=(10, 0))
            self.label2 = (CTkLabel(master=self.name_frame, text=f"{project_name[0][0]}",
                                    width=30, fg_color="#F0F0F0").pack(anchor="w", side="left", padx=(25, 25), pady=(5, 0)))
            self.label1 = (CTkLabel(master=self.name_frame, text=f"{self.task_number}/{self.complete_task}",
                                    width=30, fg_color="#F0F0F0").pack(anchor="w", side="right", padx=(25, 25), pady=(5, 0)))
            self.progress_bar1 = CTkProgressBar(master=self.task_progress_frame, fg_color="#F0F0F0",
                                                width=self.progress_bar_width, height=20, corner_radius=8,
                                                progress_color=COLORS[0], border_color="#491669", border_width=2)
            self.progress_bar1.pack(anchor="n", padx=10, pady=(5, 0))

            self.progress_bar1.set(progress)

            self.p_name = result[0][0]
            self.p_description = result[0][1]

            self.project_name = CTkTextbox(master=self.description_frame, height=35, fg_color="#DCDCDC",
                                           text_color="#491669", font=("Arial Bold", 14))
            self.project_name.pack(anchor="n", fill="x", padx=(5, 0), pady=(5, 0))
            self.project_name.insert('1.0', self.p_name)

            self.description_label = CTkTextbox(master=self.description_frame, fg_color="#DCDCDC", height=100,
                                                text_color="#000000", font=("Arial", 13))
            self.description_label.pack(anchor="n", fill="x", padx=(5, 0), pady=(5, 0))
            self.description_label.insert('1.0', self.p_description)

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

        self.label = CTkLabel(master=title_frame, text="Your Colleagues", font=("Arial Black", 23),
                              text_color="#601e88")
        self.label.pack(anchor="nw", side="left", pady=(8, 0))

        self.search_container = CTkFrame(master=self.main_frame, height=50, fg_color="#F0F0F0")
        self.search_container.pack(fill="x", pady=(30, 0), padx=27)

        self.search_entry = CTkEntry(master=self.search_container, width=650, placeholder_text="Search Colleague with its ID or Name",
                                     border_color="#70438C", border_width=2)
        self.search_entry.pack(side="left", padx=(13, 0), pady=15)

        self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color="#601e88", hover_color="#491669", width=28, command=self.search)
        self.search_button.pack(side="left", padx=(13, 0), pady=15)

        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "SELECT employee_id, employee_name, profession, contact_no FROM employee_details"
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                print(result)
        except mysql.connector.Error as e:
            print(e)

        self.table_data = [
            [("ID", "Name", "Profession", "Contact No.")]
        ]
        self.table_data.append(results)
        self.table_data = list(itertools.chain(*self.table_data))

        self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#601e88",
                              hover_color="#DCDCDC")
        self.table.edit_row(0, font=("Arial Bold", 14))
        self.table.edit_row(0, text_color="#fff", hover_color="#491669")
        self.table.pack(expand=True, fill="x")

        self.window_count = 2

    def search(self):
        search_data = self.search_entry.get()
        global data
        if search_data == '':
            messagebox.showinfo("Null", "Their is nothing to search")
        else:
            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = "SELECT employee_id, employee_name, profession, contact_no FROM employee_details WHERE employee_name=%s"
                val = (search_data, )

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

            self.label = CTkLabel(master=title_frame, text="Your Colleagues", font=("Arial Black", 23),
                                  text_color="#601e88")
            self.label.pack(anchor="nw", side="left", pady=(8, 0))

            # self.add_employee_button = CTkButton(master=title_frame, text="+ New Employee", font=("Arial Black", 15),
            #                                      text_color="#fff", fg_color="#601e88", hover_color="#491669",
            #                                      corner_radius=15, command=self.add_employee)
            # self.add_employee_button.pack(anchor="ne", side="right", ipady=10)

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
                [("ID", "Name", "Profession", "Contact No.")]
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
            self.table.pack(expand=True, fill="x")

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
        self.main_frame.destroy()
        self.main_frame = CTkFrame(master=self, fg_color="#ffffff", width=780, height=650, corner_radius=0)
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(side="left")

        title_frame = CTkFrame(master=self.main_frame, fg_color="transparent")
        title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        self.label = CTkLabel(master=title_frame, text="Project Details", font=("Arial Black", 23),
                              text_color="#601e88")
        self.label.pack(anchor="nw", side="left", pady=(8, 0))

        self.tasks_button = CTkButton(master=title_frame, text="My Tasks", font=("Arial Black", 15),
                                            text_color="#fff", fg_color="#601e88", hover_color="#491669",
                                            corner_radius=15, command=self.task_manager)
        self.tasks_button.pack(anchor="ne", side="right", ipady=10)

        self.search_container = CTkFrame(master=self.main_frame, height=50, fg_color="#F0F0F0")
        self.search_container.pack(fill="x", pady=(30, 0), padx=27)

        self.search_entry = CTkEntry(master=self.search_container, width=650, placeholder_text="Search Project with Unique ID",
                                     border_color="#70438C", border_width=2)
        self.search_entry.pack(side="left", padx=(13, 0), pady=15)

        self.search_button = CTkButton(master=self.search_container, text="", image=self.search_img, fg_color="#601e88",
                                       hover_color="#491669", width=28, command=self.search_project)
        self.search_button.pack(side="left", padx=(13, 0), pady=15)

        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "SELECT unique_id, project_name, start_date, due_date, username FROM project"
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                print(result)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error Occured: {e}")
            print(e)

        self.table_data = [
            [("Unique\nID", "Project Name", "Start Date", "Due Date", "Project\nHead")]
        ]

        self.table_data.append(results)
        self.table_data = list(itertools.chain(*self.table_data))

        self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#601e88",
                              hover_color="#DCDCDC")
        self.table.edit_row(0, font=("Arial Bold", 14))
        self.table.edit_row(0, text_color="#fff", hover_color="#491669")
        self.table.edit_column(1, width=200)
        self.table.pack(expand=True, fill="x")

        self.window_count = 3

    def search_project(self):
        search_project = self.search_entry.get()
        if search_project == '':
            messagebox.showinfo("Null", "Their is nothing to search")
        else:
            try:
                db = connection.Connection().get_connection()
                cursor = db.cursor()

                sql = "SELECT unique_id, project_name, start_date, due_date, employee_name FROM project WHERE %s IN (unique_id, project_name, start_date, due_date, employee_name)"
                val = (search_project, )
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

            self.tasks_button = CTkButton(master=title_frame, text="My Tasks", font=("Arial Black", 15),
                                                text_color="#fff", fg_color="#601e88", hover_color="#491669",
                                                corner_radius=15)
            self.tasks_button.pack(anchor="ne", side="right", ipady=10)

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
                [("Unique\nID", "Project Name", "Start Date", "Due Date", "Project\nHead")]
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
            self.table.pack(expand=True, fill="x")

            self.window_count = 3

    def task_manager(self):
        self.main_frame.destroy()
        self.main_frame = CTkFrame(master=self, fg_color="#ffffff", width=780, height=650, corner_radius=0)
        self.main_frame.pack_propagate(0)
        self.main_frame.pack(side="left")

        title_frame = CTkFrame(master=self.main_frame, fg_color="transparent")
        title_frame.pack(anchor="n", fill="x", padx=27, pady=(10, 0))

        self.label = CTkLabel(master=title_frame, text="Your Tasks", font=("Arial Black", 23),
                              text_color="#601e88")
        self.label.pack(anchor="nw", side="left", pady=(8, 0))

        for frame in range(2):
            self.project_name_container = CTkFrame(master=self.main_frame, height=50, fg_color="transparent")
            self.project_name_container.pack(fill="x", pady=(15, 0), padx=27)

            self.project_name = CTkLabel(master=self.project_name_container, text=f"{frame+1}. PROJECT_NAME", font=("Arial Bold", 14))
            self.project_name.pack(anchor="nw", padx=(5, 0))

            self.tasks_frame = CTkScrollableFrame(master=self.main_frame, fg_color="#EEEEEE")
            self.tasks_frame.pack(expand=True, fill="both", padx=27, pady=(0, 21))

            for task in range(10):
                self.task_checkbox = CTkCheckBox(master=self.tasks_frame, checkbox_height=15, checkbox_width=15, text=f"Task {task+1}", text_color="#7E7E7E", onvalue=1, offvalue=0)
                self.task_checkbox.pack(anchor="nw", padx=(15, 0), pady=(15, 0))


        # self.project_name_container = CTkFrame(master=self.main_frame, height=50, fg_color="#F0F0F0")
        # self.project_name_container.pack(fill="x", pady=(10, 0), padx=27)
        #
        # self.tasks_frame2 = CTkScrollableFrame(master=self.main_frame, fg_color="#EEEEEE")
        # self.tasks_frame2.pack(expand=True, fill="both", padx=27, pady=21)

        # self.project_label_frame = CTkFrame(master=self.tasks_frame1, fg_color="transparent")
        # self.project_label_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        # self.task1 = CTkCheckBox(master=self.tasks_frame1)

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
        self.main_frame.destroy()
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

        self.table_data = [
            [("Unique\nID", "Project Name", "Start Date", "Due Date", "Project\nHead")]
        ]

        # self.table_data.append(results)
        # self.table_data = list(itertools.chain(*self.table_data))

        self.table_frame = CTkScrollableFrame(master=self.main_frame, fg_color="transparent")
        self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        self.table = CTkTable(master=self.table_frame, colors=["#E6E6E6", "#EEEEEE"],
                              header_color="#601e88",
                              hover_color="#DCDCDC")
        self.table.edit_row(0, font=("Arial Bold", 14))
        self.table.edit_row(0, text_color="#fff", hover_color="#491669")
        self.table.edit_column(1, width=200)
        self.table.pack(expand=True, fill="x")

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
        if self.window_count == 5:
            pass
        else:
            self.main_frame.destroy()
            self.main_frame = CTkFrame(master=self, fg_color="#ffffff", width=780, height=650, corner_radius=0)
            self.main_frame.pack_propagate(0)
            self.main_frame.pack(side="left")

            self.edit_profile_button = CTkButton(master=self.main_frame, image=self.open_img, text="     Edit Profile                                                                                             ", width=620, height=60, fg_color="#601e88", font=("Rockwell", 22), hover_color="#491669", anchor="w", compound="right", command=self.update_profile).pack(anchor="center", fill="x", padx=30, ipadx=10, ipady=10, pady=(70, 0))
            self.theme_button = CTkButton(master=self.main_frame, image=self.open_img, text="     Set appearance mode                                                                         ", height=60, fg_color="#601e88", font=("Rockwell", 22), hover_color="#491669", anchor="w", compound="right").pack(anchor="center", fill="x", padx=30, ipadx=10, ipady=10, pady=(25, 0))
            self.logout_button = CTkButton(master=self.main_frame, image=self.logout_img2, text="     Log out                                                                                                    ", height=60, fg_color="#601e88", font=("Rockwell", 22), hover_color="#491669", anchor="w", compound="right", command=self.logout_listner).pack(anchor="center", fill="x", padx=30, ipadx=10, ipady=10, pady=(25, 0))

            self.window_count = 5

    def update_profile(self):
        self.main_frame.destroy()

        self.main_frame = CTkFrame(master=self, fg_color="#ffffff", width=780, height=650, corner_radius=0)
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

        self.id_label = CTkLabel(master=self.main_frame, text="Employee ID:", width=350, font=("Arial Bold", 14), text_color="#601e88")
        self.id_label.pack(anchor="nw", padx=(100, 25), pady=(60, 0))
        self.employee_id = CTkEntry(master=self.main_frame, width=330, height=35, border_color="#601e88", fg_color="#EEEEEE", font=("Arial Bold", 14))
        self.employee_id.pack(anchor="n", padx=(25, 25), pady=(5, 0))
        self.employee_id.insert(0, id)

        self.name_label = CTkLabel(master=self.main_frame, text="Name:", width=350, font=("Arial Bold", 14), text_color="#601e88")
        self.name_label.pack(anchor="nw", padx=(77, 25), pady=(10, 0))
        self.employee_name = CTkEntry(master=self.main_frame, width=330, height=35, border_color="#601e88", fg_color="#EEEEEE", font=("Arial Bold", 14))
        self.employee_name.pack(anchor="n", padx=(25, 25), pady=(5, 0))
        self.employee_name.insert(0, name)

        self.doj_label = CTkLabel(master=self.main_frame, text="Date of Joining:", width=350, font=("Arial Bold", 14),
                                   text_color="#601e88")
        self.doj_label.pack(anchor="nw", padx=(107, 25), pady=(10, 0))
        self.date_of_joining = CTkEntry(master=self.main_frame, width=330, height=35, border_color="#601e88", fg_color="#EEEEEE", font=("Arial Bold", 14))
        self.date_of_joining.pack(anchor="n", padx=(25, 25), pady=(5, 0))
        self.date_of_joining.insert(0, doj)

        self.contact_label = CTkLabel(master=self.main_frame, text="Contact No.:", width=350, font=("Arial Bold", 14),
                                   text_color="#601e88")
        self.contact_label.pack(anchor="nw", padx=(97, 25), pady=(10, 0))
        self.contact_no = CTkEntry(master=self.main_frame, width=330, height=35, border_color="#601e88", fg_color="#EEEEEE", font=("Arial Bold", 14))
        self.contact_no.pack(anchor="n", padx=(25, 25), pady=(5, 0))
        self.contact_no.insert(0, contact)

        self.e_contact_label = CTkLabel(master=self.main_frame, text="Emergency Contact No.:", width=350, font=("Arial Bold", 14),
                                   text_color="#601e88")
        self.e_contact_label.pack(anchor="nw", padx=(140, 25), pady=(10, 0))
        self.emergency_contact = CTkEntry(master=self.main_frame, width=330, height=35, border_color="#601e88", fg_color="#EEEEEE", font=("Arial Bold", 14))
        self.emergency_contact.pack(anchor="n", padx=(25, 25), pady=(5, 0))
        self.emergency_contact.insert(0, e_contact)

        # self.username_label = CTkLabel(master=self.main_frame, text="Username:", width=350, font=("Arial Bold", 14),
        #                            text_color="#601e88")
        # self.username_label.pack(anchor="nw", padx=(93, 25), pady=(10, 0))
        # self.username_entry = CTkEntry(master=self.main_frame, width=330, height=35, border_color="#601e88", fg_color="#EEEEEE", font=("Arial Bold", 14))
        # self.username_entry.pack(anchor="n", padx=(25, 25), pady=(5, 0))
        # self.username.insert(0, username)
        # self.password = CTkEntry(master=self.main_frame)
        # self.password.pack()
        # self.show_password = CTkCheckBox(master=self.main_frame)
        # self.show_password.pack()

        self.save_changes = CTkButton(master=self.main_frame, height=40, width=150, fg_color="#601e88", hover_color="#491669", text="Save Changes", font=("Arial Bold", 14), command=self.save_changes)
        self.save_changes.pack(anchor="n", padx=(25, 25), pady=(25, 0))

    def save_changes(self):
        e_id = self.employee_id.get()
        e_name = self.employee_name.get()
        e_doj = self.date_of_joining.get()
        e_contact = self.contact_no.get()
        e_emer_contact = self.emergency_contact.get()
        # e_username = self.username_entry.get()
        try:
            db = connection.Connection().get_connection()
            cursor = db.cursor()

            sql = "UPDATE employee_details SET employee_id = %s, employee_name = %s, date_of_joining = %s, contact_no = %s, emergency_contact_no = %s WHERE username=%s"
            val = (e_id, e_name, e_doj, e_contact, e_emer_contact, self.username)
            cursor.execute(sql, val)
            db.commit()
            messagebox.showinfo("Successful", "Data has been updated successfully")
            self.main_frame.destroy()
            self.settings()
        except mysql.connector.Error as e:
            print(e)
            messagebox.showerror("Database Error", f"Error Occured:{e}")

    def logout_listner(self):
        self.destroy()
        import user_login
        login = user_login.Login()
        login.mainloop()

# if __name__ == '__main__':
#     app = DashboardWindow()
#     app.mainloop()