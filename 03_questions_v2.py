"""Version 2 of Questions for Maori Numbers and Colours Quiz
Switching from the first frame to second frame
"""


from tkinter import *
from tkinter import messagebox

root = Tk()


class MainWindow:
    # This is currently just the second frame
    def __init__(self, frame1):
        self.frame1 = frame1
        f1 = Frame(frame1, width=600, height=480, bg="pink")
        f1.grid(row=0, column=0, sticky="nsew")


# calls the class
def start_quiz():
    MainWindow(root)  # Calls the MainWindow class


# this is the first, main frame
def intro():
    # this opens the second frame once start button is pressed
    def start():
        print("Start pressed")
        if len(name.get()) == 0:
            messagebox.showerror("ERROR", "Please enter your name before continuing")
        else:
            mainframe.forget()
            start_quiz()

    # this is the first main frame
    master = root
    mainframe = Frame(master, width=600, height=480, bg="orange")
    mainframe.grid(row=0, column=0, sticky="nsew")

    # Creating the design for the welcome screen
    heading = Label(mainframe, bg="dark orange", fg="black", text="Maori Quiz", font=("Calibri", 40))
    heading.grid(row=1, column=1, columnspan=2, pady=10)

    welcome = Label(mainframe, bg="orange", fg="black", text="WELCOME", font=("Calibri", 30, "bold"))
    welcome.grid(row=2, column=1, columnspan=2)

    # Start button - calls on function that closes window and opens the next
    start_button = Button(mainframe, bg="dark orange", fg="black", text="START", width=10,
                          height=1, command=start, font=("Calibri", 20))
    start_button.grid(row=5, column=1, columnspan=2, pady=40)

    # Entering player details
    name_label = Label(mainframe, bg="orange", text="Player Name:", font=("Calibri", 15))
    name_label.grid(row=3, sticky=W, column=1, padx=10)

    # to ensure the player presses enter before start
    instructions = Label(mainframe, bg="orange", font=("Courier New", 15), text="PRESS ENTER TO CONFIRM NAME")
    instructions.grid(row=4, column=1, columnspan=2)

    name = Entry(mainframe, width=45)
    name.grid(row=3, column=2, pady=30)
    name.bind("<Return>", lambda event: on_return())

    mainframe.grid_columnconfigure(0, weight=1)
    mainframe.grid_columnconfigure(6, weight=1)

    # this is just a regular function for entering the player's name
    def on_return():
        player_name = name.get()

        if len(player_name) == 0:
            messagebox.showerror("ERROR", "Please enter your name before continuing")
        else:
            intro_label = Label(mainframe, bg="orange", font=("Calibri", 15),
                                text="Hi " + player_name + ", press start to continue")
            intro_label.grid(row=6, column=1, columnspan=2, pady=15)


Q_list = [(1, "Q1 - What is the Maori word for green?"),
          (2, "Q2 - What is the Maori word for two?"),
          (3, "Q3 - What number is ono?"),
          (4, "Q4 - What is the Maori word for blue?"),
          (5, "Q5 - What colour is whero?"),
          (6, "Q6 - What is the Maori word for five?"),
          (7, "Q7 - What number is tahi?"),
          (8, "Q8 - What is the Maori word for pink?"),
          (9, "Q9 - What is rua + rima = ?"),
          (10, "Q10 - What colour does whero and kowhai make?")]


# Set up of the main window
root.title("Maori Numbers and Colours Quiz")
root.geometry("600x480")
root.maxsize(1200, 650)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

intro()

root.mainloop()
