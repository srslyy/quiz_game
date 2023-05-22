"""Version 2 of Setting up interface for Maori Numbers and Colours Quiz
Setting up the welcome screen"""

from tkinter import *
step = 0


def start_quiz():
    root.destroy()

    win = Tk()
    win.mainloop()


root = Tk()

# Giving the window a title
root.title("Maori Numbers and Colours Quiz")

# Setting the window size
root.geometry("1000x600")
root.maxsize(1200, 650)

heading = Label(root, bg="sky blue", fg="black", text="Maori Quiz", font=("Calibri", 50))
heading.pack()

startButton = Button(root, bg="sky blue", text="START", width=20, command=start_quiz)
startButton.place(x=450, y=450)

root.mainloop()
