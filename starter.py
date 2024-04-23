import customtkinter
from PIL import Image
from customtkinter import *

WORKSPACE_IMG_DATA = Image.open("images/WORKSPACE MANAGEMENT SYSTEM.png")


class Starter(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Starter")
        self.geometry("800x600+500+150")
        set_appearance_mode("system")
        self.workspace_img = CTkImage(dark_image=WORKSPACE_IMG_DATA, light_image=WORKSPACE_IMG_DATA, size=(800, 530))

        # self.starter_img = CTkLabel(master=self, image=self.workspace_img, text="", width=800, height=530)
        # self.starter_img.pack(anchor="n", expand=True)

        self.main_frame = CTkFrame(master=self, width=800, height=100, fg_color="#DCDCDC")
        self.main_frame.pack(anchor="n", expand=True, fill="x")
        self.button = CTkButton(master=self.main_frame, text="Get Started", height=35, width=200, font=("Arial Bold", 14), command=self.get_started)
        self.button.pack(anchor="n", padx=(25, 25), pady=(560, 0))

    def get_started(self):
        self.destroy()
        import user_login
        start = user_login.Login()
        start.mainloop()


if __name__ == '__main__':
    starter = Starter()
    starter.mainloop()