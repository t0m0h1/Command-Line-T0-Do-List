import tkinter as tk 

class UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do-List App")
        self.geometry("600x600")
        self.label = tk.Label(self, text="Hello, World!")
        self.label.pack()

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    app = UI()
    app.run()


    