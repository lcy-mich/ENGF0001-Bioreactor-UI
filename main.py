from tkinter import *
from tkinter import ttk
import ttkwidgets as ttkw
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from random import randint

class Main:

    def __init__(self, root):

        FIG_SIZE = 2
        BUTTON_PADDING = (50, 20, 50, 20)

        root.title("bioreactor ui")
        root.resizeable = (False, False)
        root.tk.call('source', './yaru/yaru.tcl')

        self.style = ttk.Style()
        self.style.theme_use("yaru")
        font = ("Century Gothic", 30)
        self.style.configure("TButton", font=font)
        self.style.configure("TEntry", font=font)
        self.style.configure("TScale", font=font)
        # self.style.configure("selected.TButton", )


        plt.style.use("seaborn-v0_8")

        mainframe = ttk.Frame(root, padding=(30,30,30,30))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.stirringbutton = ttk.Button(mainframe, text="stirring", padding=BUTTON_PADDING)
        self.stirringbutton.grid(column=0, row=0)

        self.stirringfig, self.stirringaxes = plt.subplots(1,1)
        self.stirringfig.set_dpi(100)
        self.stirringfig.set_figwidth = 10
        self.stirringfig.set_figheight = 10
        self.stirringdata = [randint(-100, 100)+i**2 for i in range(11)]
        self.stirringplot = self.stirringfig.add_subplot(self.stirringaxes)
        self.stirringplot.plot(self.stirringdata)
        self.stirringcanvas = FigureCanvasTkAgg(self.stirringfig, mainframe)
        self.stirringcanvas.draw()
        self.stirringcanvas.get_tk_widget().grid(column=0, row=3, sticky=(W))



        self.heatingbutton = ttk.Button(mainframe, text="heating", padding=BUTTON_PADDING)
        self.heatingbutton.grid(column=1, row=0)

        self.heatingfig, self.heatingaxes = plt.subplots(1,1)
        self.heatingfig.set_dpi(100)
        self.heatingfig.set_figwidth = 10
        self.heatingfig.set_figheight = 10
        self.heatingdata = [randint(-100, 100)+i**2 for i in range(11)]
        self.heatingplot = self.heatingfig.add_subplot(self.heatingaxes)
        self.heatingplot.plot(self.heatingdata)
        self.heatingcanvas = FigureCanvasTkAgg(self.heatingfig, mainframe)
        self.heatingcanvas.draw()
        self.heatingcanvas.get_tk_widget().grid(column=1, row=3, sticky=(E,W))



        self.phbutton = ttk.Button(mainframe, text="ph", padding=BUTTON_PADDING)
        self.phbutton.grid(column=2, row=0)

        self.phfig = Figure(figsize=(FIG_SIZE, FIG_SIZE))
        
        self.phfig, self.phaxes = plt.subplots(1,1)
        self.phfig.set_dpi(100)
        self.phfig.set_figwidth = 10
        self.phfig.set_figheight = 10
        self.phdata = [randint(-100, 100)+i**2 for i in range(11)]
        self.phplot = self.phfig.add_subplot(self.phaxes)
        self.phplot.plot(self.phdata)
        self.phcanvas = FigureCanvasTkAgg(self.phfig, mainframe)
        self.phcanvas.draw()
        self.phcanvas.get_tk_widget().grid(column=2, row=3, sticky=(E))


        self.value = DoubleVar(mainframe, 0)
        self.scalebar = ttkw.TickScale(mainframe, orient=HORIZONTAL, length=200, from_=0.0, to=100.0, variable=self.value, digits=1, showvalue=False, tickinterval = 10, resolution=0.1)
        self.scalebar.grid(row=2, columnspan=3, sticky=(N,E,W))

        self.ValueLabel = ttk.Entry(mainframe, justify="center", textvariable=self.value, validatecommand=self.validate)
        self.ValueLabel.grid(column=1, row=1, sticky=(S))


        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe.rowconfigure(2, weight=1)
        mainframe.columnconfigure(2, weight=1)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=2, pady=2)
            
    def validate(self, text):
        try:
            float(text)
            return True
        except:
            return False


if __name__ == "__main__":
    root = Tk()

    Main(root)
    
    root.mainloop()
