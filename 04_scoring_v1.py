"""Version 1 of Scoring for Maori Numbers and Colours Quiz
Using only needed code to save time
Including a score /10 for each correct answer
"""


from tkinter import *
from tkinter import messagebox

root = Tk()


class MainWindow:
    # This is currently just the second frame
    def __init__(self, frame1, q_n, q, a1, a2, a3):
        self.frame1 = frame1
        self.f1 = Frame(frame1, width="600", height="120", bg="orange")
        self.f1.pack(fill=BOTH)

        self.options = [a1, a2, a3]

        self.score = 0

        # Question number
        self.q = q
        self.q_n = q_n

        # Question label
        self.question = Label(self.f1, text=q, fg="black", font=("Calibri", 15))
        self.question.pack()

        # Submit button
        self.submit = Button(self.f1, text="SUBMIT", command=self.check_ans, fg="black", font=("Calibri", 13))
        self.submit.pack()

        # Next button
        self.next_b = Button(self.f1, text="NEXT", command=self.next_q, fg="black", font=("Calibri", 13))
        self.next_b.pack()

        # Dropdown menu comes down from here
        self.box = StringVar()
        self.box.set("Select Answer")
        # Sends dropdown menu to 'self.box' above
        self.a_menu = OptionMenu(self.f1, self.box, *self.options)
        self.a_menu.pack()

        # Response labels
        self.correct = Label(self.f1, text=f"Congrats! You get a point for getting Question {self.q_n} right!")
        self.prompt = Label(self.f1, text="Press next to continue")
        self.incorrect = Label(self.f1, text=f"*errrhh* You got Question {self.q_n} wrong!")

        self.selected = False

    def check_ans(self):
        selected_ans = self.box.get()
        for q in Q_list:
            if q[0] == self.q_n:
                if selected_ans == q[A_list[self.q_n - 1]]:
                    self.correct.config(text=f"Congrats! You get a point for getting Question {self.q_n} right!")
                    self.correct.pack()
                    self.prompt.pack()
                    self.selected = True
                    self.score += 1
                    print("right")  # for testing
                elif selected_ans == "Select Answer":
                    error()
                    self.selected = False
                else:
                    self.incorrect.config(text=f"*errrhh* You got Question {self.q_n} wrong!")
                    self.incorrect.pack()
                    self.prompt.pack()
                    self.selected = True
                    print("wrong")  # for testing

    def next_q(self):
        self.correct.forget()
        self.prompt.forget()
        self.incorrect.forget()

        if self.selected is True:
            self.q_n += 1
            self.a_menu.forget()
            self.box.set("Select Answer")

            if self.q_n == 11:
                print("end", self.score)
            else:
                # Changing question in label, and answer options in the drop-down menu
                for q in Q_list:
                    if q[0] == self.q_n:
                        self.question.config(text=q[1])
                        self.options = [q[2], q[3], q[4]]
                        self.a_menu = OptionMenu(self.f1, self.box, *self.options)
                        self.a_menu.pack()
                        self.selected = False
        else:
            error()


# calls the class
def start_quiz():
    q_num = 1  # Question number
    for Q in Q_list:  # This is so that the right info is displayed
        if Q[0] == q_num:
            MainWindow(root, q_num, Q[1], Q[2], Q[3], Q[4])  # Calls the MainWindow class


# Constants
def error():
    messagebox.showerror("ERROR", "Sorry, you must select an answer and click submit before continuing")


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
root.geometry("600x180")
root.maxsize(1200, 650)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

start_quiz()

root.mainloop()
