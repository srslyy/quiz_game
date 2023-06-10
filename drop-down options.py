from tkinter import *


# Change the label text
def show():
    label.config(text=f"You chose {clicked.get()}")


def destroy():
    root.destroy()


# Set up the interface
root = Tk()
root.title("Dropdown menu")
root.geometry("300x90")

# Dropdown menu options
options = ["Cheese", "Beef", "Chicken", "Egg", "Lettuce", "Tomato", "Avocado"]

clicked = StringVar()

# Initial menu text - dropdown comes from here
clicked.set("Choose filling...?")

# Send dropdown menu to 'clicked' button above
choice = OptionMenu(root, clicked, *options)  # includes whole options list
choice.config(bg="orange", width=30, font=("Calibri", 15))
choice["menu"].config(bg="orange")

choice.pack()

# Create button, to change label text
select_button = Button(root, text="click to confirm", command=show)
select_button.pack()

# Create Label to hold the day chosen
label = Label(root, text="Choice will appear here")
label.pack()

# Create button to exit program
exit = Button(root, text="exit", command=destroy)
exit.pack()

root.mainloop()