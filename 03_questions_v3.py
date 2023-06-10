"""Version 2 of Questions for Maori Numbers and Colours Quiz
Using only needed code to save time
Switching from one question to the next
"""


from tkinter import *

root = Tk()


class MainWindow:
    # This is currently just the second frame
    def __init__(self, frame1, q_n, q):
        self.frame1 = frame1
        f1 = Frame(frame1, width="600", height="120", bg="orange")
        f1.pack(fill=BOTH)

        self.q = q
        self.q_n = q_n  # Question number

        self.question = Label(f1, text=q, fg="black", font=("Calibri", 15))  # Question label
        self.question.pack()

        self.next_b = Button(f1, text="NEXT", command=self.next_q, fg="black", font=("Calibri", 15))  # Next button
        self.next_b.pack()

    def next_q(self):
        print("next")
        self.q_n += 1

        for q in Q_list:
            if q[0] == self.q_n:
                self.question.config(text=q[1])


# calls the class
def start_quiz():
    q_num = 1  # Question number
    for Q in Q_list:
        if Q[0] == q_num:
            MainWindow(root, q_num, Q[1])  # Calls the MainWindow class


Q_list = [(1, "Question 1 - What is the Maori word for green?"),
          (2, "Question 2 - What is the Maori word for two?"),
          (3, "Question 3 - What number is ono?"),
          (4, "Question 4 - What is the Maori word for blue?"),
          (5, "Question 5 - What colour is whero?"),
          (6, "Question 6 - What is the Maori word for five?"),
          (7, "Question 7 - What number is tahi?"),
          (8, "Question 8 - What is the Maori word for pink?"),
          (9, "Question 9 - What is rua + rima = ?"),
          (10, "Question 10 - What colour does whero and kowhai make?")]


# Set up of the main window
root.title("Maori Numbers and Colours Quiz")
root.geometry("600x70")
root.maxsize(1200, 650)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

start_quiz()

root.mainloop()
