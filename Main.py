#_____________________________________________________________________________________
#Import

from tkinter import *
import os

#_____________________________________________________________________________________
#Functions and Variables

game_over = bronze_key = silver_key = golden_key = False
bronze_key = silver_key = golden_key = True
bg_frames = "#f1f1f1"
hearts = 3
foods = 2.5

def show_heart():
    #Heart - 1
    if hearts >= 1:
        lbl_heart_01.config(image = heart_11_dic)
    elif hearts == 0.5:
        lbl_heart_01.config(image = heart_01_dic)
    elif hearts < 0.5:
        lbl_heart_01.config(image = heart_00_dic)
        game_over = True

    #Heart - 2
    if hearts >= 2:
        lbl_heart_02.config(image = heart_11_dic)
    elif hearts == 1.5:
        lbl_heart_02.config(image = heart_01_dic)
    elif hearts < 1.5:
        lbl_heart_02.config(image = heart_00_dic)

    #Heart - 3
    if hearts >= 3:
        lbl_heart_03.config(image = heart_11_dic)
    elif hearts == 2.5:
        lbl_heart_03.config(image = heart_01_dic)
    elif hearts < 2.5:
        lbl_heart_03.config(image = heart_00_dic)

    #Heart - 4
    if hearts >= 4:
        lbl_heart_04.config(image = heart_11_dic)
    elif hearts == 3.5:
        lbl_heart_04.config(image = heart_01_dic)
    elif hearts < 3.5:
        lbl_heart_04.config(image = heart_00_dic)

    #Heart - 5
    if hearts >= 5:
        lbl_heart_05.config(image = heart_11_dic)
    elif hearts == 4.5:
        lbl_heart_05.config(image = heart_01_dic)
    elif hearts < 4.5:
        lbl_heart_05.config(image = heart_00_dic)

def show_food():
    #Food - 1
    if foods >= 1:
        lbl_food_01.config(image = food_11_dic)
    elif foods == 0.5:
        lbl_food_01.config(image = food_01_dic)
    elif foods < 0.5:
        lbl_food_01.config(image = food_00_dic)
        game_over = True

    #Food - 2
    if foods >= 2:
        lbl_food_02.config(image = food_11_dic)
    elif foods == 1.5:
        lbl_food_02.config(image = food_01_dic)
    elif foods < 1.5:
        lbl_food_02.config(image = food_00_dic)

    #Food - 3
    if foods >= 3:
        lbl_food_03.config(image = food_11_dic)
    elif foods == 2.5:
        lbl_food_03.config(image = food_01_dic)
    elif foods < 2.5:
        lbl_food_03.config(image = food_00_dic)

    #Food - 4
    if foods >= 4:
        lbl_food_04.config(image = food_11_dic)
    elif foods == 3.5:
        lbl_food_04.config(image = food_01_dic)
    elif foods < 3.5:
        lbl_food_04.config(image = food_00_dic)

    #Food - 5
    if foods >= 5:
        lbl_food_05.config(image = food_11_dic)
    elif foods == 4.5:
        lbl_food_05.config(image = food_01_dic)
    elif foods < 4.5:
        lbl_food_05.config(image = food_00_dic)

def show_key():
    #Key - B
    if bronze_key == True:
        lbl_key_B.config(image = key_B_dic)
    elif bronze_key == False:
        lbl_key_B.config(image = key_E_dic)

    #Key - S
    if silver_key == True:
        lbl_key_S.config(image = key_S_dic)
    elif silver_key == False:
        lbl_key_S.config(image = key_E_dic)

    #Key - G
    if golden_key == True:
        lbl_key_G.config(image = key_G_dic)
    elif golden_key == False:
        lbl_key_G.config(image = key_E_dic)




def show_main_menu():
    window.title("Main Menu")

    lbl_01.place(x = 10, y = 10, width = width - 40, height = 65)
    lbl_02.place(x = 10, y = 75, width = width - 40, height = 65)
    btn_start.place(x = 225, y = 140, width = 250, height = 60)
    btn_tutorial.place(x = 225, y = 215, width = 250, height = 60)
    btn_credits.place(x = 225, y = 290, width = 250, height = 60)
    btn_quit.place(x = 225, y = 365, width = 250, height = 60)

def clear_main_menu():
    lbl_01.place_forget()
    lbl_02.place_forget()
    btn_start.place_forget()
    btn_tutorial.place_forget()
    btn_credits.place_forget()
    btn_quit.place_forget()

def back():
    lbl_01.place_forget()
    lbl_02.place_forget()
    lbl_credits.place_forget()
    lbl_tutorial_01.place_forget()
    btn_back.place_forget()
    btn_back_start.place_forget()
    root_status.place_forget()
    root_narrative.place_forget()
    show_main_menu()

#_____________________________________________________________________________________
#Tkinter

directory = os.path.dirname(__file__)

window = Tk()

bg = "#fafafa"
fg = "#000"
width = 720 #700
height = 470 #450
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
pos_x = int(width_screen / 2 - width / 2)
pos_y = int(height_screen / 2 - height / 2)

window.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
window.title("Main Menu")
window.iconbitmap(directory + "/Arts/icon.ico")
window.resizable(False,False)
window.configure(background = bg)

#_____________________________________________________________________________________
#Main Menu 

#Frame
root = Frame(window, bd = 1, relief = "sunken", bg = bg)
root.place(x = 10, y = 10, width = width - 20, height = height - 20)

#Labels
lbl_01 = Label(root, text = " - Lost - ", bg=bg, font = "courier 40 bold")
lbl_02 = Label(root, text = "a tale of choices", bg=bg, font = "courier 32 bold", anchor = N)

#Buttons

btn_start = Button(root, text= "Start", bg=bg, bd = 2, relief = "ridge", command = lambda: start(), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground="#fafafa")
btn_tutorial = Button(root, text= "Tutorial", bg=bg, bd = 2, relief = "ridge", command = lambda: tutorial(), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground="#fafafa")
btn_credits = Button(root, text= "Credits", bg=bg, bd = 2, relief = "ridge", command = lambda: credits(), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground="#fafafa")
btn_quit = Button(root, text= "Quit", bg=bg, bd = 2, relief = "ridge", command = lambda: window.quit(), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground="#fafafa")

show_main_menu()

#_____________________________________________________________________________________
#Tutorial

def tutorial():
    window.title("Tutorial")

    clear_main_menu()

    btn_back.place(x = 225, y = 365, width = 250, height = 60)
    lbl_tutorial_01.place(x = 225, y = 150, width = 250, height = 60)

lbl_tutorial_01 = Label(root, text="By: Arthur V.B.S.", bg=bg, font = "courier 18 italic")
btn_back = Button(root, text= "Back", bg=bg, bd = 2, relief = "ridge", command = lambda: back(), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground="#fafafa")

#_____________________________________________________________________________________
#Credits

def credits():
    window.title("Credits")

    btn_start.place_forget()
    btn_tutorial.place_forget()
    btn_credits.place_forget()
    btn_quit.place_forget()

    btn_back.place(x = 225, y = 365, width = 250, height = 60)
    lbl_credits.place(x = 225, y = 150, width = 250, height = 60)

lbl_credits = Label(root, text="By: Arthur V.B.S.", bg=bg, font = "courier 18 italic")

btn_back = Button(root, text= "Back", bg=bg, bd = 2, relief = "ridge", command = lambda: back(), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground="#fafafa")

#_____________________________________________________________________________________
#Levels

def start():
    window.title("Level 01")

    root_status.place(x = 0, y = 280, width = width - 20, height = 175)#168
    root_narrative.place(x = 0, y = 0, width = width - 20, height = 280)

    btn_back_start.place(x = 610, y = 120, width = 80, height = 40)

    clear_main_menu()

#Frame
root_status = Frame(root, bd = 1, relief = "sunken", bg = bg)
#root_status.place(x = 0, y = 280, width = width - 20, height = 175)#168

root_narrative = Frame(root, bd = 1, relief = "sunken", bg = "#222")
#root_narrative.place(x = 0, y = 0, width = width - 20, height = 280)

root_hearts = Frame(root_status, bd = 1, relief = "sunken", bg = bg_frames)
root_hearts.place(x = 10, y = 10, width = 160, height = 40)

root_foods = Frame(root_status, bd = 1, relief = "sunken", bg = bg_frames)
root_foods.place(x = 180, y = 10, width = 160, height = 40)

root_keys = Frame(root_status, bd = 1, relief = "sunken", bg = bg_frames)
root_keys.place(x = 10, y = 60, width = 50, height = 100)

#buttons

btn_back_start = Button(root_status, text= "Menu", bg=bg, bd = 2, relief = "ridge", command = lambda: back(), cursor="hand2",
                    font = "courier 12 bold", activebackground="#ccc", activeforeground="#fafafa")








#Hearts, Foods and Keys - PhotoImage

empty_00_dic = PhotoImage(file= directory + "/Arts/empty.png")

heart_11_dic = PhotoImage(file= directory + "/Arts/H_and_F/heart_11.png")
heart_01_dic = PhotoImage(file= directory + "/Arts/H_and_F/heart_01.png")
heart_00_dic = PhotoImage(file= directory + "/Arts/H_and_F/heart_00.png")

food_11_dic = PhotoImage(file= directory + "/Arts/H_and_F/food_11.png")
food_01_dic = PhotoImage(file= directory + "/Arts/H_and_F/food_01.png")
food_00_dic = PhotoImage(file= directory + "/Arts/H_and_F/food_00.png")

key_E_dic = PhotoImage(file= directory + "/Arts/K_and_PL/Key_E.png")
key_B_dic = PhotoImage(file= directory + "/Arts/K_and_PL/Key_B.png")
key_S_dic = PhotoImage(file= directory + "/Arts/K_and_PL/Key_S.png")
key_G_dic = PhotoImage(file= directory + "/Arts/K_and_PL/Key_G.png")

padlock_B_closed_dic = PhotoImage(file= directory + "/Arts/K_and_PL/Pl_B_closed.png")
padlock_S_closed_dic = PhotoImage(file= directory + "/Arts/K_and_PL/Pl_S_closed.png")
padlock_G_closed_dic = PhotoImage(file= directory + "/Arts/K_and_PL/Pl_G_closed.png")

padlock_B_open_dic = PhotoImage(file= directory + "/Arts/K_and_PL/PL_B_open.png")
padlock_S_open_dic = PhotoImage(file= directory + "/Arts/K_and_PL/PL_S_open.png")
padlock_G_open_dic = PhotoImage(file= directory + "/Arts/K_and_PL/PL_G_open.png")

#Hearts, Foods and Keys - Labels

lbl_heart_01 = Label(root_hearts, image = empty_00_dic, bg = bg_frames)
lbl_heart_01.place(x = 5, y = 5, width = 30, height = 30)
lbl_heart_02 = Label(root_hearts, image = empty_00_dic, bg = bg_frames)
lbl_heart_02.place(x = 35, y = 5, width = 30, height = 30)
lbl_heart_03 = Label(root_hearts, image = empty_00_dic, bg = bg_frames)
lbl_heart_03.place(x = 65, y = 5, width = 30, height = 30)
lbl_heart_04 = Label(root_hearts, image = empty_00_dic, bg = bg_frames)
lbl_heart_04.place(x = 95, y = 5, width = 30, height = 30)
lbl_heart_05 = Label(root_hearts, image = empty_00_dic, bg = bg_frames)
lbl_heart_05.place(x = 125, y = 5, width = 30, height = 30)

lbl_food_01 = Label(root_foods, image = empty_00_dic, bg = bg_frames)
lbl_food_01.place(x = 5, y = 5, width = 30, height = 30)
lbl_food_02 = Label(root_foods, image = empty_00_dic, bg = bg_frames)
lbl_food_02.place(x = 35, y = 5, width = 30, height = 30)
lbl_food_03 = Label(root_foods, image = empty_00_dic, bg = bg_frames)
lbl_food_03.place(x = 65, y = 5, width = 30, height = 30)
lbl_food_04 = Label(root_foods, image = empty_00_dic, bg = bg_frames)
lbl_food_04.place(x = 95, y = 5, width = 30, height = 30)
lbl_food_05 = Label(root_foods, image = empty_00_dic, bg = bg_frames)
lbl_food_05.place(x = 125, y = 5, width = 30, height = 30)

lbl_key_B = Label(root_keys, image = empty_00_dic, bg = bg_frames)
lbl_key_B.place(x = 10, y = 5, width = 30, height = 30)
lbl_key_S = Label(root_keys, image = empty_00_dic, bg = bg_frames)
lbl_key_S.place(x = 10, y = 35, width = 30, height = 30)
lbl_key_G = Label(root_keys, image = empty_00_dic, bg = bg_frames)
lbl_key_G.place(x = 10, y = 65, width = 30, height = 30)

main_dic = PhotoImage(file= directory + "/Arts/main.png")
lbl_main = Label(root_status, image = main_dic, bg = bg)
lbl_main.place(x = 70, y = 60)

show_heart()
show_food()
show_key()

window.mainloop()
