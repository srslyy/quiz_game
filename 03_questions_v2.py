"""Version 2 of Questions for Maori Numbers and Colours Quiz
Creating the questions, and adding the details and answers into lists"""


from tkinter import *
from tkinter import messagebox

root = Tk()


class MainWindow:
    def __init__(self, frame1, q, ans1, ans2, ans3, qn_num):
        self.frame1 = frame1
        f1 = Frame(root, width=600, height=480, bg="orange")
        f1.grid(row=0, column=0, sticky="nsew")
        self.qn_num = qn_num

        # Question label
        self.question = Label(f1, text=q)
        self.question.grid(row=1)

        # First answer button
        self.bn1 = Button(f1, text=ans1, command=lambda: self.mark(ans1))
        self.bn1.grid(row=2)

        # Second answer button
        self.bn2 = Button(f1, text=ans2, command=lambda: self.mark(ans2))
        self.bn2.grid(row=3)

        # Third answer button
        self.bn3 = Button(f1, text=ans3, command=lambda: self.mark(ans3))
        self.bn3.grid(row=4)

        # Continue button
        self.cont_bn = Button(f1, text="CONTINUE", command=self.next)
        self.cont_bn.grid(row=5)

        self.response = Label(f1, text="")
        self.response.grid(row=6)
        self.chosen = False

    def mark(self, chosen_ans):
        self.chosen = True
        for ans in A_list:
            if ans[0] == self.qn_num:
                if chosen_ans == ans[1]:
                    self.response.config(text="That's right!")
                else:
                    self.response.config(text="Sorry that's wrong!")

    def next_bn(self, bn, ans):
        bn.config(text=ans, command=lambda: self.mark(ans))

    def next(self):
        if self.chosen is True:
            self.response.grid_forget()
            self.qn_num += 1

            for qn in Q_list:
                if qn[0] == self.qn_num:
                    self.question.config(text=qn[1])
                    ans1 = qn[2]
                    ans2 = qn[3]
                    ans3 = qn[4]
                    self.next_bn(self.bn1, ans1)
                    self.next_bn(self.bn2, ans2)
                    self.next_bn(self.bn3, ans3)
            self.chosen = False
        else:
            messagebox.showerror("ERROR", "Please choose an answer")


def start_quiz():
    q_num = 1
    for qn in Q_list:
        if qn[0] == q_num:
            MainWindow(root, qn[1], qn[2], qn[3], qn[4], q_num)


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


Q_list = [(1, "Q1 - What is the Maori word for green?", "KOWHAI", "KAKARIKI", "KARAKA"),
          (2, "Q2 - What is the Maori word for two?", "RIMA", "TORU", "RUA"),
          (3, "Q3 - What number is ono?", "FOUR", "EIGHT", "SEVEN"),
          (4, "Q4 - What is the Maori word for blue?", "KAHURANGI", "KARAKA", "KIWIKIWI"),
          (5, "Q5 - What colour is whero?", "YELLOW", "ORANGE", "RED"),
          (6, "Q6 - What is the Maori word for five?", "TAHI, WHA, RIMA"),
          (7, "Q7 - What number is tahi?", "ONE", "TEN", "SIX"),
          (8, "Q8 - What is the Maori word for pink?", "WHERO", "MAWHERO", "MA"),
          (9, "Q9 - What is rua + rima = ?", "WHITU", "IWA", "TEKAU"),
          (10, "Q10 - What colour does whero and kowhai make?", "PURPLE", "ORANGE", "CYAN")]

A_list = [(1, "KAKARIKI"), (2, "RUA"), (3, "EIGHT"), (4, "KAHURANGI"), (5, "RED"),
          (6, "RIMA"), (7, "ONE"), (8, "MAWHERO"), (9, "WHITU"), (10, "ORANGE")]


# Set up of the main window
root.title("Maori Numbers and Colours Quiz")
root.geometry("600x480")
root.maxsize(1200, 650)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

intro()

root.mainloop()
