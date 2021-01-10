
from tkinter import *
from tkinter import messagebox

import sqlite3

con = sqlite3.connect("loginDrawingApp.db")
cur = con.cursor()

class AddNewUser(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("450x300")
        self.title("Add User")
        self.resizable(False, False)

        self.background = PhotoImage(file='backgrounds/—Pngtree—business background white style_3630980.png')
        self.background_label = Label(self, image=self.background)
        self.background_label.pack()

    # new user icon .
        self.new_user_icon = PhotoImage(file='icons/new-user.png')
        self.new_user_icon_label = Label(self, image=self.new_user_icon)
        self.new_user_icon_label.place(x=60, y=10)

    # new user title .
        self.title_label = Label(self, text='New User', font='Times 20 bold')
        self.title_label.place(x=160, y=30)

    # new user label and entry .
        self.new_user_name_label = Label(self, text='User Name :', font='Times 13 bold')
        self.new_user_name_label.place(x=15, y=100)

        self.new_user_entry = Entry(self, bd=5, width=40)
        self.new_user_entry.insert(0, "Enter new user name")
        self.new_user_entry.place(x=150, y=100)

    # new password label and entry .
        self.new_password_label = Label(self, text='User Password :', font='Times 13 bold')
        self.new_password_label.place(x=15, y=140)

        self.new_password_entry = Entry(self, bd=5, width=40)
        self.new_password_entry.insert(0, "Enter new password")
        self.new_password_entry.place(x=150, y=140)

    # submit button to create new user .
        self.submit_button = Button(self, text='Submit', font='Times 13 bold', width=30, bd=5, command=self.add_user)
        self.submit_button.place(x=60, y=190)

    # cancel button .
        self.cancel_button = Button(self, text='Cancel', font='Times 13 bold', width=30, bd=5, command=self.cancel)
        self.cancel_button.place(x=60, y=230)

        def click_on_user_name_entry(evt):
            """
            This fucntion will be activated when the user click on 'new_user_entry' box .
            the text was entered before will be deleted .
            :param evt: on click .
            :return: None .
            """
            self.new_user_entry.delete(0, END)

        def click_on_user_password_entry(evt):
            """
            This function will be activated when the user click on the text in the 'new_password_entry' box ->
            the text will be deleted .
            :param evt: on click .
            :return: None .
            """
            self.new_password_entry.delete(0, END)

        # when the user click on one the those entries -> text will be deleted using one of the functions above .
        self.new_user_entry.bind('<Button-1>', click_on_user_name_entry)
        self.new_password_entry.bind('<Button-1>', click_on_user_password_entry)

    def add_user(self):
        """
        this function will be activated when the user click on 'Create User' button .
        the function will check if the entries boxes arent empty , and if the user name was entered doesnt exist in db .
        :return: None .
        """
        # het the new user name was entered .
        new_user_name = self.new_user_entry.get()
        new_user_password = self.new_password_entry.get()

        # the user name must not contain a space inside -> so i check that -> if there is a space inside -> i print
        # a message to the user then close the window .
        for i in new_user_name:
            if i.isspace():
                messagebox.showinfo("Error", "User name cannot contain space !!", icon='warning')
                self.destroy()

        # i check if the user name was entered is exists in db .
        check_user_name = cur.execute("SELECT * FROM user_info WHERE user_user_name=?", (new_user_name,)).fetchall()

        # if the user name exist -> i print this message and close the window .
        if len(check_user_name) > 0:
            messagebox.showinfo("Error", "User name exist in the system .\nplease choose other user name .",
                                icon='warning')
            self.destroy()

        # if the user name doesnt exists in db and the values entered to the entries boxes arent empty then i add new
        # user to db .
        if new_user_name and new_user_password != "":
            try:
                query = "INSERT INTO 'user_info' (user_user_name, user_password) VALUES(?, ?)"
                cur.execute(query, (new_user_name, new_user_password))
                con.commit()
                messagebox.showinfo("Success", "Successfully added to database!", icon='info')
                self.destroy()

            except:
                messagebox.showerror("Error", "Cant add to database!", icon='warning')
                self.destroy()
        else:
            messagebox.showerror("Error", "Fields cant be empty!", icon='warning')
            self.destroy()

    def cancel(self):
        """
        function will be activated when the user click on cancel button .
        :return:
        """
        self.destroy()



