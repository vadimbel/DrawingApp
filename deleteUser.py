
from tkinter import *
from tkinter import messagebox

import sqlite3

con = sqlite3.connect("loginDrawingApp.db")
cur = con.cursor()

class DeleteUser(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+350+200")
        self.title("Delete User")
        self.resizable(False, False)

    # create 'main_frame' -> on the whole screen .
        self.main_frame = Frame(self)
        self.main_frame.pack(fill=BOTH)

    # create a left frame and place 'delete_button' , 'users_list_scrollBar' and 'users_list' on it .
        self.left_frame = Frame(self.main_frame, width=400, relief=SUNKEN, borderwidth=2)
        self.left_frame.pack(side=LEFT, anchor=W)

    # delete button to delete a user from db .
        self.delete_button = Button(self.left_frame, text='DELETE', font='Times 14 bold', bd=5, width=21,
                                    command=self.delete_user)
        self.delete_button.pack(side=TOP, anchor=W, pady=10, padx=5)

    # a list bar and a scroll bar to display all the users from db .
        self.users_list_scrollBar = Scrollbar(self.left_frame, orient=VERTICAL)
        self.users_list = Listbox(self.left_frame, width=45, height=30, yscrollcommand=self.users_list_scrollBar.set)
        self.users_list_scrollBar.config(command=self.users_list.yview)
        self.users_list_scrollBar.pack(side=LEFT, fill=Y)
        self.users_list.pack(side=LEFT)

    # insert all the users from db to 'users_list' box .
        users = cur.execute("SELECT * FROM user_info").fetchall()
        count = 0
        for user in users:
            self.users_list.insert(count, "User name :      {}".format(str(user[0])))
            count += 1

    # create a right frame on 'main_frame' and place 'delete_icon' on ot .
        self.right_frame = Frame(self.main_frame, width=300, relief=SUNKEN)
        self.right_frame.pack(fill=BOTH)

        self.delete_icon = PhotoImage(file='icons/delete_icon.png')
        self.delete_icon_label = Label(self.right_frame, image=self.delete_icon)
        self.delete_icon_label.pack(fill=BOTH, pady=100)

    def delete_user(self):
        # check if the user selected something from the 'user_list' box -> 'selected_item' is a tuple ->
        # if the user did not select anything -> the tuple is empty -> the if statement will be activated .
        # if the user did select something -> the tuple contains somthing -> len(selected_item) > 0 .
        selected_item = self.users_list.curselection()

    #   the user did not select anything from 'user_list' box -> len(selected_item) == 0.
        if len(selected_item) == 0:
            messagebox.showerror("Error", "User did not select any item from users list !", icon='warning')
            self.destroy()
            return None

    # the user selected something from 'user_list' -> len(selected_item) > 0 -> do this code :
        # get the selected item (string) .
        user_to_delete = self.users_list.get(selected_item)

        # i want to get the user name out of the string in the list box .
        user_name = ""

        # so i run a for loop from the end -> when i reach a white char -> the last word in the string is over ->
        # i got the last word in 'user_name' variable -> this is the user name -> end the for loop .
        for i in range(len(user_to_delete)-1, 0, -1):
            if user_to_delete[i].isspace():
                break
            user_name += user_to_delete[i]

        # then i ask the user if he sure that he wants to delete this user .
        mbox = messagebox.askquestion("Warning", "Are you sure to delete this contact ?", icon='warning')

        # if the answer is yes -> i delete the user from table .
        if mbox == 'yes':
            try:
                cur.execute("DELETE FROM user_info WHERE user_user_name=?", (user_name,))
                con.commit()
                messagebox.showinfo("Success", "User has been deleted !")
                self.destroy()
            except:
                messagebox.showinfo("Info", "User has not been deleted ..")
                self.destroy()
        else:
            messagebox.showinfo("Info", "User has not been deleted ...")
            self.destroy()





















