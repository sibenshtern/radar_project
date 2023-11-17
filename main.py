import tkinter as tk

from window import Window
from objects.aircraft import Aircraft

from model import *


if __name__ == '__main__':
    root = tk.Tk()
    app = Window((root.winfo_screenwidth(), root.winfo_screenheight()))
    app.run()