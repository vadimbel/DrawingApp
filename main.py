
from tkinter import *
from tkinter import messagebox

import sqlite3, openDrawingApp, openCreateDeleteWindow, creatorInfo

con = sqlite3.connect("loginDrawingApp.db")
cur = con.cursor()

class LoginWindow(object):
    def __init__(self, parent):
        self.parent = parent

    # background for the 'login' window .
        self.user_background = PhotoImage(file='backgrounds/login_background.png')
        self.user_background_label = Label(self.parent, image=self.user_background)
        self.user_background_label.pack()

    # icon at the top of 'login' window .
        self.user_icon = PhotoImage(file='icons/login_icon.png')
        self.user_icon_label = Label(self.parent, image=self.user_icon, bg='white')
        self.user_icon_label.place(x=110, y=10)

    # a title at the top of 'login' window .
        self.title_label = Label(self.parent, text='LOGIN :', font='Times 20 bold', bg='white', fg='green')
        self.title_label.place(x=270, y=60)

    # name label and entry next to it -> for the user to enter his user name .
        self.name_label = Label(self.parent, text='User Name :', font='Times 16 bold', bg='white', fg='green')
        self.name_label.place(x=30, y=158)

        self.name_entry = Entry(self.parent, bd=5, bg='white', width=50, font='times 12 bold')
        self.name_entry.insert(0, "Please enter your user name here")
        self.name_entry.place(x=160, y=158)

    # password label an entry next to it -> for the user to enter his password .
        self.password_label = Label(self.parent, text='Password :', font='Times 16 bold', bg='white', fg='green')
        self.password_label.place(x=30, y=208)

        self.password_entry = Entry(self.parent, bd=5, bg='white', width=50, font='times 12 bold')
        self.password_entry.insert(0, "Please enter your password here")
        self.password_entry.place(x=160, y=208)

    # 3 buttons :
        # 1. login button .
        self.login_button = Button(self.parent, text='Login', bd=5, width=35, height=1, font='Times 13 bold',
                                   command=self.login_user)
        self.login_button.place(x=160, y=255)

        # 2. create/delete user .
        self.create_delete_button = Button(self.parent, text='Options', bd=5, width=35, height=1, font='Times 13 bold',
                                           command=self.create_delete_user)
        self.create_delete_button.place(x=160, y=295)

        # 3. ABOUT US button .
        self.about_button = Button(self.parent, text='About Us', bd=5, width=35, height=1, font='Times 13 bold',
                                   command=self.show_creator_info)
        self.about_button.place(x=160, y=335)

        def click_on_name_entry(evt):
            """
            This function will be activated when the user click on the text in the 'name_entry' box -> the text
                will be deleted .
            :param evt: on click -> action activated .
            :return: None
            """
            self.name_entry.delete(0, END)

        def click_on_password_entry(evt):
            """
            This function will be activated when the user click on the text in the 'password_entry' box -> the text
                will be deleted .
            :param evt: on click -> action activated .
            :return: None
            """
            self.password_entry.delete(0, END)


    # when the user click on one the those entries -> text will be deleted using one of the functions above .
        self.name_entry.bind('<Button-1>', click_on_name_entry)
        self.password_entry.bind('<Button-1>', click_on_password_entry)

    def login_user(self):
        """
        This function will be activated when the user click on 'login' button .
        the function will check if there is a user with the 'user_name' and 'user_password' was entered .
        if so -> a new window will be open .
        if not -> right message will be printed .
        :return: open new window / right message .
        """
        user_name = self.name_entry.get()
        user_password = self.password_entry.get()

    # check if there is a user with the user_name and user_password was entered to the entries .
        user = cur.execute("SELECT * FROM user_info WHERE user_user_name=? and user_password=?",
                           (user_name, user_password)).fetchall()

    # if there is no such user -> print this error using message box . else open new window .
        if len(user) == 0:
            messagebox.showinfo("Error", "There is no such user name !", icon="warning")
        else:
            open_login_user_window = openDrawingApp.OpenDrawingApp()


    def create_delete_user(self):
        """
        this function will be activated when the user click on 'Options' button .
        :return: None .
        """
        open_create_delete_window = openCreateDeleteWindow.OpenCreateDeleteWindow()

    def show_creator_info(self):
        open_creator_info = creatorInfo.CreatorInfo()



def main():
    root = Tk()
    app = LoginWindow(root)
    root.title("Login Window")
    root.geometry("650x550+350+200")
    root.resizable(False, False)
    root.mainloop()



if __name__ == '__main__':
    main()
