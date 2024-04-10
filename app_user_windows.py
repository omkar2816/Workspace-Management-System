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
OPEN_IMG_DATA = Image.open("images/open.png")
LOGOUT_IMG2_DATA = Image.open("images/logout_set.png")

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
        self.open_img = CTkImage(dark_image=OPEN_IMG_DATA, light_image=OPEN_IMG_DATA)
        self.logout_img2 = CTkImage(dark_image=LOGOUT_IMG2_DATA, light_image=LOGOUT_IMG2_DATA)

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
                                            corner_radius=15)
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

            sql = "SELECT unique_id, project_name, start_date, due_date, employee_name FROM project"
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

            self.edit_profile_button = CTkButton(master=self.main_frame, image=self.open_img, text="     Edit Profile                                                                                             ", width=620, height=60, fg_color="#601e88", font=("Rockwell", 22), hover_color="#491669", anchor="w", compound="right").pack(anchor="center", fill="x", padx=30, ipadx=10, ipady=10, pady=(70, 0))
            self.theme_button = CTkButton(master=self.main_frame, image=self.open_img, text="     Set appearance mode                                                                         ", height=60, fg_color="#601e88", font=("Rockwell", 22), hover_color="#491669", anchor="w", compound="right").pack(anchor="center", fill="x", padx=30, ipadx=10, ipady=10, pady=(25, 0))
            self.logout_button = CTkButton(master=self.main_frame, image=self.logout_img2, text="     Log out                                                                                                    ", height=60, fg_color="#601e88", font=("Rockwell", 22), hover_color="#491669", anchor="w", compound="right").pack(anchor="center", fill="x", padx=30, ipadx=10, ipady=10, pady=(25, 0))

            self.window_count = 5


    # def update_profile(self):
    #     self.main_frame = CTkFrame(master=self, fg_color="#ffffff", width=780, height=650, corner_radius=0)
    #     self.main_frame.pack_propagate(0)
    #     self.main_frame.pack(side="left")
    #
    #     self.

if __name__ == '__main__':
    app = DashboardWindow()
    app.mainloop()