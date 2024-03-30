import mysql.connector

import connection
from tkinter import messagebox
from user_login import Login

window = Login()

window.create_window()
window.create_user_frames()
# window.create_admin_frames()


window.login_window.mainloop()