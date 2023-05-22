from tkinter import *

# root window
root = Tk()
root.geometry("400x250")
root.title('Login form using .place')
root.resizable(False, False)

# set up and position labels - left
username_label = Label(root, text="Username:")
username_label.place(x=30, y=50)

email_label = Label(root, text="Email:")
email_label.place(x=30, y=90)

password_label= Label(root, text="Password:")
password_label.place(x=30, y=130)

# set up and position entry boxes - to the right of labels
username = Entry(root)
username.place(x=95, y=50, width=200)

email = Entry(root)
email.place(x=95, y=90, width=200)

password = Entry(root)
password.place(x=95, y=130, width=200)

# set up and position button at bottom right
login_button = Button(root, text="Login", width=10)
login_button.place(x=300, y=180)


root.mainloop()
