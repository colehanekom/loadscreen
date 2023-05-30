from tkinter import *

window = Tk()

window.geometry("800x550")
window.config(bg="#ffffff")

welcome_label = Label(text="Home Page", bg="#2F6C60",  font=("Trebuchet Ms", 15, "bold"), fg="#ffffff")
welcome_label.place(x=130, y=25)

window.mainloop()
