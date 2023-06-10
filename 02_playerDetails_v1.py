"""Version 1 of Player details for Maori Numbers and Colours Quiz
Setting up the welcome screen to include the design and inputs for the player's details
"""

from tkinter import *


# For testing purposes
def comment():
    global name
    global age
    string1 = name.get()
    string2 = age.get()
    print(string1)
    print(string2)


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

# Creating the design for the welcome screen
root.configure(bg="orange")
heading = Label(root, bg="dark orange", fg="black", text="Maori Quiz", font=("Calibri", 50))
heading.place(x=350, y=30)

welcome = Label(root, bg="orange", fg="black", text="WELCOME", font=("Calibri", 30, "bold"))
welcome.place(x=410, y=140)

# Start button - calls on function that closes window and opens the next
startButton = Button(root, bg="dark orange", fg="black", text="START", width=10, height=1, command=comment,
                     font=("Calibri", 20))
startButton.place(x=425, y=450)

# Entering player details
name_label = Label(root, bg="orange", text="Player Name:", font=("Calibri", 15))
name_label.place(x=200, y=250)

age_label = Label(root, bg="orange", text="Player Age:", font=("Calibri", 15))
age_label.place(x=200, y=330)

name = Entry(root)
name.place(x=325, y=255, width=350, height=30)

age = Entry(root)
age.place(x=325, y=335, width=350, height=30)

root.mainloop()
