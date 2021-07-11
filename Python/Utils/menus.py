from tkinter import *
from tkinter import ttk
from math import floor
from time import sleep
from random import randint

def welcome_menu(directory, voice_over, bg = '#fafafa', fg = '#fafafa'):
    global progressBar
    window_welcome = Tk()

    width = 420
    height = 170
    width_screen = window_welcome.winfo_screenwidth()
    height_screen = window_welcome.winfo_screenheight()
    pos_x = int(width_screen / 2 - width / 2)
    pos_y = int(height_screen / 2 - height / 2)

    root = Frame(window_welcome, bd = 1, relief = 'sunken', bg = bg)
    root.place(x = 10, y = 10, width = width - 20, height = height - 20)

    window_welcome.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
    window_welcome.title('Configurações Iniciais')
    window_welcome.iconbitmap(directory + '/Images/Icons/icon_01.ico')
    window_welcome.resizable(False,False)
    window_welcome.configure(background = '#000')

    def loading():
        global user
        lbl_name.place_forget()
        btn_entry.place_forget()
        entry_user.place_forget()

        user = var_user.get()

        window_welcome.title('Iniciando o jogo, aguarde!')
        pb_loading.place(x = 10 , y = 100, width = width - 40, height = 40)

        progress = 0
        while progress < 100:
            sleep(0.01)
            window_welcome.update()
            progress += randint(0, 100)/100

            var_progressBar_loading.set(progress)
            
            lbl_progress.configure(text = f'{floor(progress)}%')
            lbl_progress.place(x = 210, y = 65, width = 180, height = 30)

            if progress >= 100:
                window_welcome.title('Seja bem-vindo(a)')
                lbl_progress.configure(text = f'100%')
                lbl_welcome.place(x = 10, y = 10, width = width - 40, height = 50)
                lbl_welcome.configure(text = f'Seja bem-vindo(a)!\n{user}')
                window_welcome.update()
                voice_over(directory, f'Olá, {user}, Seja bem-vindo ou bem-vinda!')
                window_welcome.destroy()

    var_progressBar_loading = DoubleVar()
    var_progressBar_loading.set(0)

    pb_loading = ttk.Progressbar(root, variable = var_progressBar_loading, maximum = 100)

    lbl_progress = Label(root, text = '', font = 'courier 16 bold', bg=bg, anchor = E)
    lbl_welcome = Label(root, text = '', font = 'courier 18 bold', bg=bg)

    lbl_name = Label(root, text = 'Insira seu nome:', font = 'courier 22 bold', bg=bg, anchor = W)
    lbl_name.place(x = 10, y = 10, width = width - 40, height = 70)

    var_user = StringVar()

    entry_user = Entry(root, bg=bg, bd = 2, relief = "ridge", font = "courier 18 bold",
                        textvariable = var_user, justify=CENTER)
    entry_user.place(x = 10, y = 90, width = 280, height = 50)

    btn_entry = Button(root, text= "Jogar", bg=bg, bd = 2, relief = "ridge", command= lambda : loading(),
                cursor="hand2", font = "courier 16 bold", activebackground="#ccc", activeforeground=fg)
    btn_entry.place(x = 300, y = 90, width = 90, height = 50)

    window_welcome.mainloop()
