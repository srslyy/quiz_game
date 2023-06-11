"""Version 1 of Maori Numbers and Colours Quiz
Combining all components together and making it look nice
"""


from tkinter import *
from tkinter import messagebox

root = Tk()


class MainWindow:
    # This is currently just the second frame
    def __init__(self, frame1, q_n, q, a1, a2, a3):
        self.frame1 = frame1
        self.f1 = Frame(frame1, width=WIDTH, height=HEIGHT, bg="orange")
        self.f1.grid(row=0, column=0, sticky="nsew")
        self.f1.grid_columnconfigure(0, weight=1)
        self.f1.grid_columnconfigure(6, weight=1)

        self.heading = Label(self.f1, bg="dark orange", text="QUIZ_NAME", font=("FONT", 40))
        self.heading.grid(row=1, column=1, columnspan=2, pady=10)

        # Options list for dropdown menu
        self.options = [a1, a2, a3]

        # Score variable
        self.score = 0

        # Question number
        self.q = q
        self.q_n = q_n

        # Question label
        self.question = Label(self.f1, bg="orange", text=q, font=("FONT", REG_FONT_SIZE, "bold"))
        self.question.grid(row=2, column=1, columnspan=2, pady=10)

        # Dropdown menu comes down from here
        self.box = StringVar()
        self.box.set("Select Answer")
        # Sends dropdown menu to 'self.box' above
        self.a_menu = OptionMenu(self.f1, self.box, *self.options)
        self.a_menu.config(bg="dark orange", width=40, font=("FONT", 12))
        self.a_menu.grid(row=3, column=1, columnspan=2, pady=40)
        self.a_menu["menu"].config(bg="dark orange", font=("FONT", 12))

        # Submit button
        self.submit = Button(self.f1, text="SUBMIT", bg="dark orange", width=10, height=1,
                             command=self.check_ans, font=("FONT", 18))
        self.submit.grid(row=4, column=1, pady=30)

        # Next button
        self.next_b = Button(self.f1, text="NEXT", bg="dark orange", width=10, height=1,
                             command=self.next_q, font=("FONT", 18))
        self.next_b.grid(row=4, column=2)

        # Response labels
        self.correct = Label(self.f1, bg="orange",
                             text=f"Congrats! You get a point for getting Question {self.q_n} right!")
        self.prompt = Label(self.f1, bg="orange", text="Press next to continue")
        self.incorrect = Label(self.f1, bg="orange",
                               text=f"*errrhh* You got Question {self.q_n} wrong!")

        self.selected = False

    def check_ans(self):
        selected_ans = self.box.get()
        self.a_menu.config(state="disabled")
        for q in Q_list:
            if q[0] == self.q_n:
                if selected_ans == q[A_list[self.q_n - 1]]:
                    self.correct.config(text=f"Congrats! You get a point for getting Question {self.q_n} right!")
                    self.correct.grid(row=5, column=1, columnspan=2, pady=10)
                    self.prompt.grid(row=6, column=1, columnspan=2, pady=10)
                    self.selected = True
                    self.score += 1
                elif selected_ans == "Select Answer":
                    error()
                    self.selected = False
                else:
                    self.incorrect.config(text=f"*ERRRHH* You got Question {self.q_n} wrong!")
                    self.incorrect.grid(row=5, column=1, columnspan=2, pady=10)
                    self.prompt.grid(row=6, column=1, columnspan=2, pady=10)
                    self.selected = True
                    print("wrong")  # for testing

    # Function that switches from one question to the next
    def next_q(self):
        self.correct.grid_forget()
        self.prompt.grid_forget()
        self.incorrect.grid_forget()

        if self.selected is True:
            self.q_n += 1
            self.a_menu.grid_forget()
            self.box.set("Select Answer")
            self.a_menu.config(state="normal")

            if self.q_n > TOTAL_Q_NUM:
                self.end()
            else:
                # Changing question in label, and answer options in the drop-down menu
                for q in Q_list:
                    if q[0] == self.q_n:
                        self.question.config(text=q[1])
                        self.options = [q[2], q[3], q[4]]
                        self.a_menu = OptionMenu(self.f1, self.box, *self.options)
                        self.a_menu.config(bg="dark orange", width=40, font=("FONT", 12))
                        self.a_menu.grid(row=3, column=1, columnspan=2, pady=40)
                        self.a_menu["menu"].config(bg="dark orange", font=("FONT", 12))
                        self.selected = False
        else:
            error()

    def end(self):
        # Hiding/not displaying the second frame
        self.f1.grid_forget()

        # The third frame
        end = Frame(self.frame1, width="600", height="480", bg="orange")
        end.grid(row=0, column=0, sticky="nsew")
        end.grid_columnconfigure(0, weight=1)
        end.grid_columnconfigure(6, weight=1)

        heading = Label(end, bg="dark orange", text="QUIZ_NAME", font=("FONT", 40))
        heading.grid(row=1, column=1, pady=10)

        # So that the score can be viewed
        stats = Button(end, bg="dark orange", width=20, height=2, text="VIEW SCORE",
                       command=lambda: display_score(end, self.score))
        stats.grid(row=2, column=1, pady=30)

        # Restart button
        restart = Button(end, bg="dark orange", width=20, height=2, text="RESTART", command=lambda: confirm(end))
        restart.grid(row=3, column=1, pady=30)

        # Quit quiz button
        close = Button(end, bg="dark orange", width=20, height=2, text="EXIT PROGRAM", command=lambda: check(end))
        close.grid(row=4, column=1, pady=30)


def display_score(end_frame, score):
    # Displaying the score
    total_score = Label(end_frame, bg="dark orange", text=f"You got a score of {score}/10!", font=30)
    total_score.grid(row=5, column=1, pady=10)


# Makes sure the user does want to end the quiz
def check(end_frame):
    ask = messagebox.askquestion("CONFIRM CLOSE QUIZ", "Are you sure you want to close the quiz?")

    if ask == "yes":
        end_frame.destroy()  # Close the end frame
        exit()


# Makes sure the user does want to restart the quiz
def confirm(end_frame):
    ask = messagebox.askquestion("CONFIRM RESTART QUIZ", "Are you sure you want to restart the quiz?")

    if ask == "yes":
        start_quiz(end_frame)


def error():
    messagebox.showerror("ERROR", "Sorry, you must select an answer and click submit before continuing")


# calls the class
def start_quiz(end_frame):
    end_frame.grid_forget()
    q_num = 1  # Question number
    for Q in Q_list:  # This is so that the right info is displayed
        if Q[0] == q_num:
            MainWindow(root, q_num, Q[1], Q[2], Q[3], Q[4])  # Calls the MainWindow class


# this is the first frame
def intro():
    # this opens the second frame once start button is pressed
    def start():
        print("Start pressed")  # for testing
        if len(name.get()) == 0:
            messagebox.showerror("ERROR", "Please enter your name before continuing")
        else:
            start_quiz(mainframe)

    # this is the first main frame
    master = root
    mainframe = Frame(master, width=WIDTH, height=HEIGHT, bg="orange")
    mainframe.grid(row=0, column=0, sticky="nsew")

    # Creating the design for the welcome screen
    heading = Label(mainframe, bg="dark orange", text="QUIZ_NAME", font=("FONT", 40))
    heading.grid(row=1, column=1, columnspan=2, pady=10)

    welcome = Label(mainframe, bg="orange", text="WELCOME", font=("FONT", 30, "bold"))
    welcome.grid(row=2, column=1, columnspan=2)

    # Start button - calls on function that closes window and opens the next
    start_button = Button(mainframe, bg="dark orange", text="START", width=10,
                          height=1, command=start, font=("FONT", 20))
    start_button.grid(row=5, column=1, columnspan=2, pady=40)

    # Entering player details
    name_label = Label(mainframe, bg="orange", text="Player Name:", font=("FONT", REG_FONT_SIZE))
    name_label.grid(row=3, sticky=W, column=1, padx=10)

    # to ensure the player presses enter before start
    instructions = Label(mainframe, bg="orange", font=("Courier New", REG_FONT_SIZE),
                         text="PRESS ENTER TO CONFIRM NAME")
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
            intro_label = Label(mainframe, bg="orange", font=("FONT", REG_FONT_SIZE),
                                text="Hi " + player_name + ", press start to continue")
            intro_label.grid(row=6, column=1, columnspan=2, pady=15)


# Constants
QUIZ_NAME = "Maori Quiz"
FONT = "Calibri"
REG_FONT_SIZE = 15
WIDTH = "600"
HEIGHT = "480"

TOTAL_Q_NUM = 10


# Questions and Answer options list
Q_list = [(1, "Question 1 - What is the Maori word for green?", "KOWHAI", "KAKARIKI", "KARAKA"),
          (2, "Question 2 - What is the Maori word for two?", "RIMA", "TORU", "RUA"),
          (3, "Question 3 - What number is ono?", "FOUR", "EIGHT", "SEVEN"),
          (4, "Question 4 - What is the Maori word for blue?", "KAHURANGI", "KARAKA", "KIWIKIWI"),
          (5, "Question 5 - What colour is whero?", "YELLOW", "ORANGE", "RED"),
          (6, "Question 6 - What is the Maori word for five?", "TAHI", "WHA", "RIMA"),
          (7, "Question 7 - What number is tahi?", "ONE", "TEN", "SIX"),
          (8, "Question 8 - What is the Maori word for pink?", "WHERO", "MAWHERO", "MA"),
          (9, "Question 9 - What is rua + rima = ?", "WHITU", "IWA", "TEKAU"),
          (10, "Question 10 - What colour does whero and kowhai make?", "PURPLE", "ORANGE", "LIGHT BLUE")]

A_list = [3, 4, 3, 2, 4, 4, 2, 3, 2, 3]

# Set up of the main window
root.title("Maori Numbers and Colours Quiz")
root.geometry("600x480")
root.maxsize(1200, 650)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

intro()

root.mainloop()
