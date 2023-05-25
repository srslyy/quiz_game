"""Version 2 of Setting up interface for Maori Numbers and Colours Quiz
Setting up the welcome screen to include the design and inputs for the player's details
In this version the widgets are placed using .grid()"""


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
heading.grid(row=1, column=1, columnspan=2, pady=30)

welcome = Label(root, bg="orange", fg="black", text="WELCOME", font=("Calibri", 30, "bold"))
welcome.grid(row=2, column=1, columnspan=2, pady=40)

# Start button - calls on function that closes window and opens the next
startButton = Button(root, bg="dark orange", fg="black", text="START", width=10, height=1, command=comment,
                     font=("Calibri", 20))
startButton.grid(row=5, column=1, columnspan=2, pady=90)

# Entering player details
name_label = Label(root, bg="orange", text="Player Name:", font=("Calibri", 15))
name_label.grid(row=3, sticky=E, column=1)

age_label = Label(root, bg="orange", text="Player Age:", font=("Calibri", 15))
age_label.grid(row=4, sticky=E, column=1)

name = Entry(root)
name.grid(row=3, column=2, pady=20)

age = Entry(root)
age.grid(row=4, column=2, pady=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(6, weight=1)


root.mainloop()
