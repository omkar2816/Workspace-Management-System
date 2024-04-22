import tkinter as tk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.counter = 0
        self.timer_running = False

        self.root.protocol("WM_DELETE_WINDOW", self.stop_timer)

        self.timer_label = tk.Label(self.root, text="0")
        self.timer_label.pack()

        self.start_timer()

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def stop_timer(self):
        global time
        self.timer_running = False
        time = self.counter
        print(time)
        root.destroy()

    def update_timer(self):
        if self.timer_running:
            self.counter += 1
            self.timer_label.config(text=str(self.counter))
            self.root.after(1000, self.update_timer)

root = tk.Tk()
app = TimerApp(root)
root.mainloop()