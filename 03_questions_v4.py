"""Version 4 of Questions for Maori Numbers and Colours Quiz
Using only needed code to save time
Including the drop-down menu for answers and ensuring the answer options are right for each question
"""


from tkinter import *

root = Tk()


class MainWindow:
    # This is currently just the second frame
    def __init__(self, frame1, q_n, q, a1, a2, a3):
        self.frame1 = frame1
        self.f1 = Frame(frame1, width="600", height="120", bg="orange")
        self.f1.pack(fill=BOTH)

        self.options = [a1, a2, a3]

        self.q = q
        self.q_n = q_n  # Question number

        self.question = Label(self.f1, text=q, fg="black", font=("Calibri", 15))  # Question label
        self.question.pack()

        self.next_b = Button(self.f1, text="NEXT", command=self.next_q, fg="black", font=("Calibri", 15))  # Next button
        self.next_b.pack()

        self.box = StringVar()
        self.box.set("Select Answer")
        self.a_menu = OptionMenu(self.f1, self.box, *self.options)  # Answer options
        self.a_menu.pack()

    def next_q(self):
        print("next")  # for testing
        self.q_n += 1
        print(self.q_n)
        self.a_menu.forget()

        # Changing question in label, and answer options in the drop-down menu
        for q in Q_list:
            if q[0] == self.q_n:
                self.question.config(text=q[1])
                self.options = [q[2], q[3], q[4]]
                self.a_menu = OptionMenu(self.f1, self.box, *self.options)
                self.a_menu.pack()


# calls the class
def start_quiz():
    q_num = 1  # Question number
    for Q in Q_list:  # This is so that the right info is displayed
        if Q[0] == q_num:
            MainWindow(root, q_num, Q[1], Q[2], Q[3], Q[4])  # Calls the MainWindow class


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


# Set up of the main window
root.title("Maori Numbers and Colours Quiz")
root.geometry("600x90")
root.maxsize(1200, 650)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

start_quiz()

root.mainloop()
