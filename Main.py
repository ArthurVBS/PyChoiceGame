#_____________________________________________________________________________________
#Import

from tkinter import *
import os

#_____________________________________________________________________________________
#Functions and Variables

game_over = False
hearts = 3
foods = 2.5

def show_heart_and_food():
    #Heart - 1
    if hearts >= 1:
        lbl_heart_01.config(image = heart_11_dic), lbl_heart_01.place_configure(x=10)
    elif hearts == 0.5:
        lbl_heart_01.config(image = heart_01_dic), lbl_heart_01.place_configure(x=10)
    elif hearts < 0.5:
        lbl_heart_01.config(image = heart_00_dic), lbl_heart_01.place_configure(x=10)
        game_over = True

    #Heart - 2
    if hearts >= 2:
        lbl_heart_02.config(image = heart_11_dic), lbl_heart_02.place_configure(x=40)
    elif hearts == 1.5:
        lbl_heart_02.config(image = heart_01_dic), lbl_heart_02.place_configure(x=40)
    elif hearts < 1.5:
        lbl_heart_02.config(image = heart_00_dic), lbl_heart_02.place_configure(x=40)

    #Heart - 3
    if hearts >= 3:
        lbl_heart_03.config(image = heart_11_dic), lbl_heart_03.place_configure(x=70)
    elif hearts == 2.5:
        lbl_heart_03.config(image = heart_01_dic), lbl_heart_03.place_configure(x=70)
    elif hearts < 2.5:
        lbl_heart_03.config(image = heart_00_dic), lbl_heart_03.place_configure(x=70)

    #Heart - 4
    if hearts >= 4:
        lbl_heart_04.config(image = heart_11_dic), lbl_heart_04.place_configure(x=100)
    elif hearts == 3.5:
        lbl_heart_04.config(image = heart_01_dic), lbl_heart_04.place_configure(x=100)
    elif hearts < 3.5:
        lbl_heart_04.config(image = heart_00_dic), lbl_heart_04.place_configure(x=100)

    #Heart - 5
    if hearts >= 5:
        lbl_heart_05.config(image = heart_11_dic), lbl_heart_05.place_configure(x=130)
    elif hearts == 4.5:
        lbl_heart_05.config(image = heart_01_dic), lbl_heart_05.place_configure(x=130)
    elif hearts < 4.5:
        lbl_heart_05.config(image = heart_00_dic), lbl_heart_05.place_configure(x=130)

    #Food - 1
    if foods >= 1:
        lbl_food_01.config(image = food_11_dic), lbl_food_01.place_configure(x=10)
    elif foods == 0.5:
        lbl_food_01.config(image = food_01_dic), lbl_food_01.place_configure(x=10)
    elif foods < 0.5:
        lbl_food_01.config(image = food_00_dic), lbl_food_01.place_configure(x=10)
        game_over = True

    #Food - 2
    if foods >= 2:
        lbl_food_02.config(image = food_11_dic), lbl_food_02.place_configure(x=40)
    elif foods == 1.5:
        lbl_food_02.config(image = food_01_dic), lbl_food_02.place_configure(x=40)
    elif foods < 1.5:
        lbl_food_02.config(image = food_00_dic), lbl_food_02.place_configure(x=40)

    #Food - 3
    if foods >= 3:
        lbl_food_03.config(image = food_11_dic), lbl_food_03.place_configure(x=70)
    elif foods == 2.5:
        lbl_food_03.config(image = food_01_dic), lbl_food_03.place_configure(x=70)
    elif foods < 2.5:
        lbl_food_03.config(image = food_00_dic), lbl_food_03.place_configure(x=70)

    #Food - 4
    if foods >= 4:
        lbl_food_04.config(image = food_11_dic), lbl_food_04.place_configure(x=100)
    elif foods == 3.5:
        lbl_food_04.config(image = food_01_dic), lbl_food_04.place_configure(x=100)
    elif foods < 3.5:
        lbl_food_04.config(image = food_00_dic), lbl_food_04.place_configure(x=100)

    #Food - 5
    if foods >= 5:
        lbl_food_05.config(image = food_11_dic), lbl_food_05.place_configure(x=130)
    elif foods == 4.5:
        lbl_food_05.config(image = food_01_dic), lbl_food_05.place_configure(x=130)
    elif foods < 4.5:
        lbl_food_05.config(image = food_00_dic), lbl_food_05.place_configure(x=130)

#_____________________________________________________________________________________
#Tkinter

directory = os.path.dirname(__file__)

window = Tk()

bg = "#fafafa"
fg = "#000"
width = 740 #700
height = 490 #450
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
pos_x = int(width_screen / 2 - width / 2)
pos_y = int(height_screen / 2 - height / 2)

window.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
window.title("Innocence")
window.iconbitmap(directory + "/Arts/icon.ico")
window.resizable(False,False)
window.configure(background = bg)

#Frame

root = Frame(window, bd = 1, relief = "sunken", bg = bg,)
root.place(x = 10, y = 10, width = width - 20, height = height - 20)

#Label

lbl_01 = Label(root, text = "Menu Principal", bg=bg, font = "times 40 bold")
lbl_01.place(x = 10, y = 10, width = width - 40, height = 65)

#Heart & Food

empty_00_dic = PhotoImage(file= directory + "/Arts/empty.png")

heart_11_dic = PhotoImage(file= directory + "/Arts/heart_11.png")
heart_01_dic = PhotoImage(file= directory + "/Arts/heart_01.png")
heart_00_dic = PhotoImage(file= directory + "/Arts/heart_00.png")

food_11_dic = PhotoImage(file= directory + "/Arts/food_11.png")
food_01_dic = PhotoImage(file= directory + "/Arts/food_01.png")
food_00_dic = PhotoImage(file= directory + "/Arts/food_00.png")

lbl_heart_01 = Label(root, image = empty_00_dic, bg = bg)
lbl_heart_01.place(x = 0, y = 10, width = 30, height = 30)
lbl_heart_02 = Label(root, image = empty_00_dic, bg = bg)
lbl_heart_02.place(x = 0, y = 10, width = 30, height = 30)
lbl_heart_03 = Label(root, image = empty_00_dic, bg = bg)
lbl_heart_03.place(x = 0, y = 10, width = 30, height = 30)
lbl_heart_04 = Label(root, image = empty_00_dic, bg = bg)
lbl_heart_04.place(x = 0, y = 10, width = 30, height = 30)
lbl_heart_05 = Label(root, image = empty_00_dic, bg = bg)
lbl_heart_05.place(x = 0, y = 10, width = 30, height = 30)

lbl_food_01 = Label(root, image = empty_00_dic, bg = bg)
lbl_food_01.place(x = 10, y = 40, width = 30, height = 30)
lbl_food_02 = Label(root, image = empty_00_dic, bg = bg)
lbl_food_02.place(x = 40, y = 40, width = 30, height = 30)
lbl_food_03 = Label(root, image = empty_00_dic, bg = bg)
lbl_food_03.place(x = 70, y = 40, width = 30, height = 30)
lbl_food_04 = Label(root, image = empty_00_dic, bg = bg)
lbl_food_04.place(x = 100, y = 40, width = 30, height = 30)
lbl_food_05 = Label(root, image = empty_00_dic, bg = bg)
lbl_food_05.place(x = 130, y = 40, width = 30, height = 30)

main_dic = PhotoImage(file= directory + "/Arts/main.png")
lbl_main = Label(root, image = main_dic, bg = bg)
lbl_main.place(x = 10, y = 200)

#lbl_main.destroy()
#show_heart_and_food()

window.mainloop()
