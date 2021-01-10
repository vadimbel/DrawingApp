
from tkinter import *

import webbrowser

class CreatorInfo(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+350+200")
        self.title("About Us")
        self.resizable(False, False)

    # background .
        self.about_us_background = PhotoImage(file='backgrounds/output-onlinepngtools.png')
        self.about_us_background_label = Label(self, image=self.about_us_background)
        self.about_us_background_label.pack()

    # title .
        self.title_label = Label(self, text='About Us :', font='Times 20 bold', fg='blue', bg='white')
        self.title_label.place(x=270, y=55)

    # icon next to the title .
        self.about_us_icon = PhotoImage(file='icons/monitor.png')
        self.about_us_icon_label = Label(self, image=self.about_us_icon, bg='white')
        self.about_us_icon_label.place(x=170, y=40)

    # label 1 .
        self.creator_label = Label(self, text='NAME :   Vadim Beletsker', font='Times 16 bold', fg='blue', bg='white')
        self.creator_label.place(x=170, y=120)

    # facebook .
        self.creator_facebook_button = Button(self, text='https://www.facebook.com/profile.php?id=100002074177617',
                                              command=self.open_facebook, width=50, font='Times 13 bold', fg='blue')
        self.creator_facebook_button.place(x=50, y=160)

    # github .
        self.creator_gitHub_page = Button(self, text='https://github.com/vadimbel',
                                          command=self.open_gitHub, width=50, font='Times 13 bold', fg='blue')
        self.creator_gitHub_page.place(x=50, y=200)

    # linkedin .
        self.creator_linkedin_page = Button(self, text='https://www.linkedin.com/in/vadim-beletsker-56103615a/',
                                            command=self.open_linkedin, width=50, font='Times 13 bold', fg='blue')
        self.creator_linkedin_page.place(x=50, y=240)


    def open_facebook(self):
        webbrowser.open("https://www.facebook.com/profile.php?id=100002074177617")

    def open_gitHub(self):
        webbrowser.open("https://github.com/vadimbel")

    def open_linkedin(self):
        webbrowser.open("https://www.linkedin.com/in/vadim-beletsker-56103615a/")
