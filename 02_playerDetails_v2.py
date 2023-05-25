"""Version 2 of Player details for Maori Numbers and Colours Quiz
Making it so that only an integer can be entered as an 'age' input"""


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
root.geometry("600x450")
root.maxsize(1200, 650)

# Creating the design for the welcome screen
root.configure(bg="orange")
heading = Label(root, bg="dark orange", fg="black", text="Maori Quiz", font=("Calibri", 40))
heading.grid(row=1, column=1, columnspan=2, pady=10)

welcome = Label(root, bg="orange", fg="black", text="WELCOME", font=("Calibri", 30, "bold"))
welcome.grid(row=2, column=1, columnspan=2, pady=20)

# Start button - calls on function that closes window and opens the next
startButton = Button(root, bg="dark orange", fg="black", text="START", width=10, height=1, command=comment,
                     font=("Calibri", 20))
startButton.grid(row=5, column=1, columnspan=2, pady=70)

# Entering player details
name_label = Label(root, bg="orange", text="Player Name:", font=("Calibri", 15))
name_label.grid(row=3, sticky=W, column=1, padx=10)

age_label = Label(root, bg="orange", text="Player Age:", font=("Calibri", 15))
age_label.grid(row=4, sticky=W, column=1, padx=10)

name = Entry(root, width=45)
name.grid(row=3, column=2, pady=15)

age = Entry(root, width=45)
age.grid(row=4, column=2, pady=15)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(6, weight=1)


root.mainloop()
