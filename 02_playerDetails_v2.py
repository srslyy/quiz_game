"""Version 2 of Player details for Maori Numbers and Colours Quiz
Making it so that a name has to be given and if not an error message is given
"""


from tkinter import *
from tkinter import messagebox

root = Tk()


def on_return():
    # For testing
    print("Return pressed")

    player_name = name.get()

    if len(player_name) == 0:
        messagebox.showerror("ERROR", "Please enter your name before continuing")
    else:
        intro_label = Label(root, bg="orange", font=("Calibri", 15), text="Hi " + player_name +
                                                                          ", press start to continue")
        intro_label.grid(row=6, column=1, columnspan=2, pady=15)


def start_quiz():
    # For testing
    print("Start pressed")
    if len(name.get()) == 0:
        messagebox.showerror("ERROR", "Please enter your name before continuing")
    else:
        root.destroy()
        win = Tk()
        win.mainloop()


# Giving the window a title
root.title("Maori Numbers and Colours Quiz")

# Setting the window size
root.geometry("600x480")
root.maxsize(1200, 650)

# Creating the design for the welcome screen
root.configure(bg="orange")
heading = Label(root, bg="dark orange", fg="black", text="Maori Quiz", font=("Calibri", 40))
heading.grid(row=1, column=1, columnspan=2, pady=10)

welcome = Label(root, bg="orange", fg="black", text="WELCOME", font=("Calibri", 30, "bold"))
welcome.grid(row=2, column=1, columnspan=2)

# Start button - calls on function that closes window and opens the next
startButton = Button(root, bg="dark orange", fg="black", text="START", width=10, height=1, command=start_quiz,
                     font=("Calibri", 20))
startButton.grid(row=5, column=1, columnspan=2, pady=40)

# Entering player details
name_label = Label(root, bg="orange", text="Player Name:", font=("Calibri", 15))
name_label.grid(row=3, sticky=W, column=1, padx=10)

# to ensure the player presses enter before start
instructions = Label(root, bg="orange", font=("Courier New", 15), text="PRESS ENTER TO CONFIRM NAME")
instructions.grid(row=4, column=1, columnspan=2)

name = Entry(root, width=45)
name.grid(row=3, column=2, pady=30)
name.bind("<Return>", lambda event: on_return())

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(6, weight=1)

root.mainloop()
