
from tkinter import *

import addNewUser, deleteUser


class OpenCreateDeleteWindow(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("400x250")
        self.title("Options")
        self.resizable(False, False)

    # title for this window .
        self.title_label = Label(self, text='Options :', font='Times 20 bold')
        self.title_label.place(x=135, y=10)

    # 3 buttons :
        # 1. create button .
        self.create_user_button = Button(self, text='Create User', font='Times 13 bold', width=30, bd=5,
                                         command=self.create_user)
        self.create_user_button.place(x=35, y=60)

        # 2. delete button .
        self.delete_user_button = Button(self, text='Delete User', font='Times 13 bold', width=30, bd=5,
                                         command=self.delete_user)
        self.delete_user_button.place(x=35, y=110)

        # 3. cancel button .
        self.cancel_button = Button(self, text='Cancel', font='Times 13 bold', width=30, bd=5,
                                    command=self.cancel)
        self.cancel_button.place(x=35, y=160)


    def create_user(self):
        new_user = addNewUser.AddNewUser()
        self.destroy()

    def delete_user(self):
        delete_user = deleteUser.DeleteUser()
        self.destroy()

    def cancel(self):
        self.destroy()




