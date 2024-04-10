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
        plt.figure(figsize=(10,8))
        plt.bar(df['employee_name'], df['working_hours'])
        plt.xlabel('employee name')
        plt.ylabel('time (in hrs)')
        plt.title('analytics')
        # plt.show()
        self.add = plt.gcf()
        canvas = FigureCanvasTkAgg(self.add, master=self.frame)
        canvas.get_tk_widget().configure(width=680, height=200)
        ctk_canvas = canvas.get_tk_widget()
        ctk_canvas.place(relx=0.1, rely=0, anchor="nw")

if __name__ == '__main__':
    app =Graph()
    app.mainloop()