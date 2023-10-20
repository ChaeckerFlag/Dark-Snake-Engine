import tkinter

class GUI:
    def __init__(self):
        self.root = tkinter.Tk()

        self.root.geometry("1920x1080")
        self.root.title("Spritesheet Animator")

        self.label = tkinter.Label(self.root, text="Spritesheet Animator", font=('Comic Sans', 60))
        self.label.pack()

        self.button = tkinter.Button(self.root, text="Start", font=('Comic Sans', 35), command=self.change_page)
        self.button.pack(pady=350)

        self.root.mainloop()

    def change_page(self):
        print("hello world")

GUI()