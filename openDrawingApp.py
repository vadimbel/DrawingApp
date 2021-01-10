
from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox

from PIL import Image, ImageDraw, ImageGrab, ImageTk

brush_color = 'black'
bg_color = 'black'

class OpenDrawingApp(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("750x750+650+200")
        self.title("Drawing App")
        self.resizable(False, False)

        def paint(evt):
            """
            this fucntion will be activated when the user starts to paint on 'my_canvas' .
            :param evt:
            :return:
            """
        # Brush Parameters :
            brush_width = '%0.0f' % float(self.my_slider.get())  # the size of the brush is the size on the size slider

        # Brush Type : BUTT , ROUND , PROJECTING
            brush_t = brush_type.get()              # the selected brush type , 1 of the 3 radio buttons under .

        # starting position :
            x1 = evt.x - 1
            y1 = evt.y - 1

        # Ending position :
            x2 = evt.x + 1
            y2 = evt.y + 1

        # 'brush_color' -> is a global variable defined at the top of the file -> the brush color .
        # width -> is the brush width -> defined in the size slider .
        # capstyle -> is the type style defined by one of the three radio buttons .
            self.my_canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=brush_width, capstyle=brush_t,
                                       smooth=True)

        def change_brush_size(evt):
            """
            this function will be activated when the user move the 'brush_size' slider .
            it will change the label located under the slider , shows the current size .
            :param evt:
            :return:
            """
            self.slider_label.config(text='%0.0f' % float(self.my_slider.get()))

        def change_brush_color():
            """
            this function will be activated when the user click on the 'brush color' button .
            brush_color = is a global variable defined at the top of the file .
            :return:
            """
            # default color is black .
            global brush_color
            brush_color = 'black'
            # open color chooser -> returns a list of two items -> that is why i choose [1] .
            # change the brush_color -> then use it in 'paint' function as 'fill' .
            brush_color = colorchooser.askcolor(color=brush_color)[1]

        def change_canvas_color():
            """
            this function will be activated when the user press on 'canvas_color' button .
            :return:
            """
        # global variable defined at the top of the file .
            global bg_color
            bg_color = 'black'
        # choose the color from the color chooser .
            bg_color = colorchooser.askcolor(color=bg_color)[1]
        # then change the background of the canvas (the frame that the user draw on it) .
            self.my_canvas.config(bg=bg_color)

        def clear_screen():
            """
            this function will be activated when the user click on 'clear screen' button .
            the function will clear the screen and restore the default background color (white) .
            :return:
            """
            # delete everything from canvas .
            self.my_canvas.delete(ALL)
            # restore the color of the background .
            self.my_canvas.config(bg='white')

        def save_as_png():
            """
            this function will be activated when the user click on the 'Save to PNG' button .
            the function will open filedialog and the user will choose where he wants to save the new png file .
            :return: None
            """
            result = filedialog.asksaveasfilename(filetypes=(("png files", "*.png"), ("all files", "*.*")))

            if result.endswith('.png'):
                pass
            else:
                result = result + '.png'

            if result:
                x = self.winfo_rootx()+self.my_canvas.winfo_x()
                y = self.winfo_rooty()+self.my_canvas.winfo_y()
                x1 = x+self.my_canvas.winfo_width()
                y1 = y+self.my_canvas.winfo_height()
                ImageGrab.grab().crop((x, y, x1, y1)).save(result)

                messagebox.showinfo("Image Saved", "Your image is saved successfully")

        # show where the file was save at the bottom of the window .
            result_label = Label(self, text=result)
            result_label.pack()

    # the place where the user going to paint .
        self.my_canvas = Canvas(self, width=600, height=400, bg='white')
        self.my_canvas.pack(pady=20)

    # when the user place the mouse on the canvas and click the mouse -> user start draw .
        self.my_canvas.bind('<B1-Motion>', paint)

    # Create Brush Options Frame -> (a frame that other stuff will be on it .)
        self.brush_options_frame = Frame(self)
        self.brush_options_frame.pack(pady=20)

    # 'brush_size_frame' -> 'my_slider' and 'slider_label' will be placed on it .
        self.brush_size_frame = LabelFrame(self.brush_options_frame, text='Brush Size')
        self.brush_size_frame.grid(row=0, column=0, padx=50)
        # Brush Slider (a scale located on the 'brush_options_frame' -> slider to change brush size .)
        self.my_slider = ttk.Scale(self.brush_size_frame, from_=1, to=100, orient=VERTICAL, value=10,
                                   command=change_brush_size)
        self.my_slider.pack(pady=10, padx=10)
        # Brush Slider Label : (a label (number of brush size) located on the 'brush_options_frame' -> under the slider)
        self.slider_label = Label(self.brush_size_frame, text=self.my_slider.get())
        self.slider_label.pack(pady=5)

    # Brush Type (a label with a frame located on the 'brush_options_frame')
        self.brush_type_frame = LabelFrame(self.brush_options_frame, text="Brush Type", height=400)
        self.brush_type_frame.grid(row=0, column=1, padx=50)

        # 'brush_type' is 1 of the 3 types selected from the 3 radio buttons under .
        brush_type = StringVar()
        brush_type.set("round")
        # create 3 radio buttons on the 'brush_options_frame' -> the radio buttons will change the brush type .
        self.brush_type_radio1 = Radiobutton(self.brush_type_frame, text="Round", variable=brush_type, value="round")
        self.brush_type_radio2 = Radiobutton(self.brush_type_frame, text="Slash", variable=brush_type, value="butt")
        self.brush_type_radio3 = Radiobutton(self.brush_type_frame, text="Diamond", variable=brush_type, value="projecting")
        # anchor = W -> is to move all buttons to the west -> make them straight .
        self.brush_type_radio1.pack(anchor=W)
        self.brush_type_radio2.pack(anchor=W)
        self.brush_type_radio3.pack(anchor=W)

    # change colors (a label with a frame placed on the 'brush_options_frame') -> two buttons will be on it :
        self.change_colors_frame = LabelFrame(self.brush_options_frame, text='Change Color')
        self.change_colors_frame.grid(row=0, column=2)

        # on the 'change_colors_frame' i create two buttons :
        # change brush color .
        self.brush_color_button = Button(self.change_colors_frame, text='Brush Color', command=change_brush_color)
        self.brush_color_button.pack(pady=10, padx=10)
        # change canvas background color
        self.canvas_color_button = Button(self.change_colors_frame, text='Canvas Color', command=change_canvas_color)
        self.canvas_color_button.pack(pady=10, padx=10)

    # program options frame ( on the 'brush_options_frame' i create a new label with a frame)
        self.options_frame = LabelFrame(self.brush_options_frame, text='Program Options')
        self.options_frame.grid(row=0, column=3, padx=50)

        # clear screen button  ( on the 'options_frame' label frame i create those two buttons :)
        self.clear_button = Button(self.options_frame, text='Clear Screen', command=clear_screen)
        self.clear_button.pack(padx=10, pady=10)
        # save image
        self.save_image_button = Button(self.options_frame, text="Save to PNG", command=save_as_png)
        self.save_image_button.pack(pady=10, padx=10)






