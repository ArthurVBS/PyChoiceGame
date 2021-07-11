from tkinter import *

def window_tk(directory, title = 'TKINTER', bg = '#fafafa', width = 720, height = 470):
    window = Tk()

    width_screen = window.winfo_screenwidth()
    height_screen = window.winfo_screenheight()
    pos_x = int(width_screen / 2 - width / 2)
    pos_y = int(height_screen / 2 - height / 2)

    root = Frame(window, bd = 1, relief = 'sunken', bg = bg)
    root.place(x = 10, y = 10, width = width - 20, height = height - 20)

    window.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
    window.title(title)
    window.iconbitmap(directory + '/Images/Icons/icon_01.ico')
    window.resizable(False,False)
    window.configure(background = '#000')

    tk = {
        'bg' : bg,
        'fg' : bg,
        'root' : root,
        'pos_x' : pos_x,
        'pos_y' : pos_y,
        'width' : width,
        'height' : height,
        'window' : window}

    return tk
