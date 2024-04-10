# import customtkinter
# import mysql.connector
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from customtkinter import *
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
# from screentime import canvas
#
#
# # Establish a connection to the database
# class Graph(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()
#         try:
#             connection = mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 password="Omkar@2802",
#                 database="w_m_s"
#             )
#
#             # Create a cursor object
#             cursor = connection.cursor()
#
#             # Execute a SQL query to fetch data
#             query = "SELECT employee, time FROM w_m_s.time_graph"
#             cursor.execute(query)
#
#             # Fetch all the rows from the result
#             rows = cursor.fetchall()
#
#             # Convert the rows into a list of lists
#             data_list = []
#             for row in rows:
#                 data_list.append(list(row))
#
#             # Close the cursor and connection
#             cursor.close()
#         except mysql.connector.Error as e:
#             print(e)
#         # Create a pandas dataframe from the list of lists
#         df = pd.DataFrame(data_list, columns=['employee', 'time'])
#
#         # Print the dataframe
#         print(df)
#
#         self.title("Graphh")
#         self.geometry('800x600')
#         self.mainframe = CTkFrame(master=self, width=500, height=500)
#         self.mainframe.pack(anchor='n')
#
#         # Create a seaborn scatterplot
#         fg = sns.lineplot(x='employee', y='time', data=df)
#
#         # Create a matplotlib figure object
#         fig = plt.gcf()
#
#         # Create a FigureCanvasTkAgg object and add it to the mainframe
#         self.canvas = FigureCanvasTkAgg(fig, master=self)
#         self.ctk_canvas = canvas.get_tk_widget()
#         self.ctk_canvas.place(relx=1, rely=0, anchor="ne")
#
#     # Show the plot and start the tkinter event loop
#     # plt.show()
# if __name__ == '__main__':
#     app = Graph()
#     app.mainloop()
# import customtkinter
# import mysql.connector
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from customtkinter import *
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
# class Graph(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()
        # Establish a connection to the database
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="Omkar@2802",
#             database="w_m_s"
#         )
#
#         # Create a cursor object
#         cursor = connection.cursor()
#
#         # Execute a SQL query to fetch data
#         query = "SELECT days, time FROM w_m_s.time_graph"
#         cursor.execute(query)
#
#         # Fetch all the rows from the result
#         rows = cursor.fetchall()
#
#         # Convert the rows into a list of lists
#         data_list = []
#         for row in rows:
#             data_list.append(list(row))
#
#         # Close the cursor and connection
#         cursor.close()
#         connection.close()
#
#         # Create a pandas dataframe from the list of lists
#         df = pd.DataFrame(data_list, columns=['days', 'time'])
#
#         # Print the dataframe
#         print(df)
#
#         self.geometry('800x600')
#         self.mainframe = CTkFrame(master=self, width=720, height=200)
#         self.mainframe.pack(anchor='n')
#
#         # Create a seaborn scatterplot
#         # fg = sns.displot(x='days', y='time', data=df, bins=[0, 70, 80, 90, 100])
#             fg = sns.displot(data_list, x="days", color="time").add(sns.Bar(), sns.Hist())
#
#         # Create a matplotlib figure object
#         fig = plt.gcf()
#
#         # Create a FigureCanvasTkAgg object and add it to the mainframe
#         canvas = FigureCanvasTkAgg(fig, master=self.mainframe)
#         canvas.get_tk_widget().configure(width=720, height=200)
#         ctk_canvas = canvas.get_tk_widget()
#         ctk_canvas.place(relx=1, rely=0, anchor="ne")
#
#         # Show the plot and start the tkinter event loop
#         # plt.show()
#
# if __name__ == '__main__':
#     app = Graph()
#     app.mainloop( )
import customtkinter
import mysql.connector
from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import connection
import pandas as pd
import matplotlib.pyplot as plt

class Graph(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("720x200")
        self.title("graph")

        self.frame = CTkFrame(master=self, width=700, height=180)
        self.frame.pack(anchor="n")


        # create a connection to the database
        db = connection.Connection().get_connection()

        # read the data from the database
        query = 'SELECT employee_name, working_hours  FROM salary'
        df = pd.read_sql(query, con=db)
        print(df)

        # plot the data as a bar graph
        plt.figure(figsize=(10,6))
        plt.bar(df['employee_name'], df['working_hours'])
        plt.xlabel('employee name')
        plt.ylabel('time (in hrs)')
        plt.title('analytics')
        # plt.show()
        self.fig = plt.gcf()
        canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        canvas.get_tk_widget().configure(width=720, height=200)
        ctk_canvas = canvas.get_tk_widget()
        ctk_canvas.place(relx=0, rely=0, anchor="nw")

if __name__ == '__main__':
    app =Graph()
    app.mainloop()