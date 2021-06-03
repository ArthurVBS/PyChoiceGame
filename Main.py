#____________________________________________________________________________________________________________
#Import

from tkinter import *
import os

#____________________________________________________________________________________________________________
#Functions and Variables

def gameover(Value):
    if Value == "True":
        print("Game Over")
        quit()
    else:
        pass

def show_heart():
    global hearts
    #Heart - 1
    if hearts >= 1:
        lbl_heart_01.config(image = heart_11_dic)
    elif hearts == 0.5:
        lbl_heart_01.config(image = heart_01_dic)
    elif hearts < 0.5:
        lbl_heart_01.config(image = heart_00_dic)
        gameover("True")

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
    if hearts == 5:
        lbl_heart_05.config(image = heart_11_dic)
    elif hearts == 4.5:
        lbl_heart_05.config(image = heart_01_dic)
    elif hearts < 4.5:
        lbl_heart_05.config(image = heart_00_dic)

    #Heart - +5
    if hearts > 5:
        hearts = 5

def show_food():
    global foods
    #Food - 1
    if foods >= 1:
        lbl_food_01.config(image = food_11_dic)
    elif foods == 0.5:
        lbl_food_01.config(image = food_01_dic)
    elif foods < 0.5:
        lbl_food_01.config(image = food_00_dic)
        gameover("True")

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

    #Foods - +5
    if foods > 5:
        foods = 5

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

def show_item():
    global lighter
    global wolfhide

    if lighter == True:
        lbl_item_lighter.config(image = item_lighter_dic)
    if wolfhide == True:
        lbl_item_wolfhide.config(image = item_lighter_dic) #Alterar!!!

def show_way():
    global level
    global bronze_key
    global golden_key
    global silver_key
    global world

    lbl_just_way_01.config(image = just_way_dic)
    lbl_just_way_02.config(image = just_way_dic)
    lbl_just_way_03.config(image = just_way_dic)
    lbl_just_way_04.config(image = just_way_dic)
    lbl_just_way_05.config(image = just_way_dic)
    lbl_just_way_06.config(image = just_way_dic)
    lbl_just_way_07.config(image = just_way_dic)
    lbl_just_way_08.config(image = just_way_dic)

    if level == 1:
        lbl_just_way_01.config(image = way_dic)
    elif level == 2:
        lbl_just_way_02.config(image = way_dic)
    elif level == 3:
        lbl_just_way_03.config(image = way_dic)
    elif level == 4:
        lbl_just_way_04.config(image = way_dic)
    elif level == 5:
        lbl_just_way_05.config(image = way_dic)
    elif level == 6:
        lbl_just_way_06.config(image = way_dic)
    elif level == 7:
        lbl_just_way_07.config(image = way_dic)
    elif level == 8:
        lbl_just_way_08.config(image = way_dic)
    else:
        print("Level Up")
        level = 1
        world += 1
        lbl_just_way_01.config(image = way_dic)

    if world == 1:
        bronze_key = True
    elif world == 2:
        silver_key = True
    elif world == 3:
        golden_key = True

    show_key()

def show_toplevel(title, lbl_text, losewin_hearts, losewin_foods):
    #Tkinter
    win_toplevel = Toplevel()
    win_toplevel.geometry(f"370x320+{pos_x + 200}+{pos_y + 100}")
    win_toplevel.title(title)
    win_toplevel.iconbitmap(directory + "/Arts/icon.ico")
    win_toplevel.resizable(False, False)
    win_toplevel.configure(background = bg)

    #Labels and Buttons

    lbl_tl_main = Label(win_toplevel, text = "A sua escolha ocasionou:", justify=CENTER, font = "courier 16 bold", bg = bg)
    lbl_tl = Label(win_toplevel, text = f"{lbl_text}", justify=CENTER, font = "courier 16 italic",
                anchor = N, bg = bg, bd = 1, relief = "sunken")
    btn_tl = Button(win_toplevel, text= "OK", bg=bg, bd = 2, relief = "ridge", command = lambda: win_toplevel.destroy(),
                    cursor="hand2", font = "courier 16 bold", activebackground="#ccc", activeforeground=fg)

    #Frame and Labels (PhotoImage)

    frame_toplevel_heart = Frame(win_toplevel, bd = 1, relief = "sunken", bg = bg_frames)
    frame_toplevel_food = Frame(win_toplevel, bd = 1, relief = "sunken", bg = bg_frames)
    frame_toplevel_item_or_key = Frame(win_toplevel, bd = 1, relief = "sunken", bg = bg_frames)

    if losewin_hearts >= 0:
        sinal_hearts = "+"
    elif losewin_hearts < 0:
        sinal_hearts = "-" 

    if losewin_hearts == 0:
        phImg_heart_01 = heart_00_dic
        phImg_heart_02 = heart_00_dic

    elif losewin_hearts == 0.5 or losewin_hearts == -0.5:
        phImg_heart_01 = heart_01_dic
        phImg_heart_02 = heart_00_dic

    elif losewin_hearts == 1 or losewin_hearts == -1:
        phImg_heart_01 = heart_11_dic
        phImg_heart_02 = heart_00_dic

    elif losewin_hearts == 1.5 or losewin_hearts == -1.5:
        phImg_heart_01 = heart_11_dic
        phImg_heart_02 = heart_01_dic

    elif losewin_hearts == 2 or losewin_hearts == -2:
        phImg_heart_01 = heart_11_dic
        phImg_heart_02 = heart_11_dic


    if losewin_foods >= 0:
        sinal_foods = "+"
    elif losewin_foods < 0:
        sinal_foods = "-"

    if losewin_foods == 0:
        phImg_food_01 = food_00_dic
        phImg_food_02 = food_00_dic

    elif losewin_foods == 0.5 or losewin_foods == -0.5:
        phImg_food_01 = food_01_dic
        phImg_food_02 = food_00_dic

    elif losewin_foods == 1 or losewin_foods == -1:
        phImg_food_01 = food_11_dic
        phImg_food_02 = food_00_dic

    elif losewin_foods == 1.5 or losewin_foods == -1.5:
        phImg_food_01 = food_11_dic
        phImg_food_02 = food_01_dic

    elif losewin_foods == 2 or losewin_foods == -2:
        phImg_food_01 = food_11_dic
        phImg_food_02 = food_11_dic


    lbl_heart = Label(frame_toplevel_heart, text = sinal_hearts, justify=CENTER, font = "courier 16 italic", bg = bg_frames)
    lbl_food = Label(frame_toplevel_food, text = sinal_foods, justify=CENTER, font = "courier 16 italic", bg = bg_frames)

    lbl_heart_losewin_01 = Label(frame_toplevel_heart, image = phImg_heart_01, bg = bg_frames)
    lbl_heart_losewin_02 = Label(frame_toplevel_heart, image = phImg_heart_02, bg = bg_frames)

    lbl_food_losewin_01 = Label(frame_toplevel_food, image = phImg_food_01, bg = bg_frames)
    lbl_food_losewin_02 = Label(frame_toplevel_food, image = phImg_food_02, bg = bg_frames)

    #.Place

    lbl_tl_main.place(x = 10, y = 10, width = 350, height = 30)
    lbl_tl.place(x = 10, y = 50, width = 350, height = 120)
    btn_tl.place(x = 145, y = 270, width = 80, height = 40)

    frame_toplevel_heart.place(x = 10, y = 180, width = 110, height = 45)
    frame_toplevel_food.place(x = 130, y = 180, width = 110, height = 45)
    frame_toplevel_item_or_key.place(x = 250, y = 180, width = 110, height = 45)

    lbl_heart.place(x = 5, y = 5, width = 30, height = 35)
    lbl_food.place(x = 5, y = 5, width = 30, height = 35)

    lbl_heart_losewin_01.place(x = 35, y = 5, width = 35, height = 35)
    lbl_heart_losewin_02.place(x = 70, y = 5, width = 35, height = 35)

    lbl_food_losewin_01.place(x = 35, y = 5, width = 35, height = 35)
    lbl_food_losewin_02.place(x = 70, y = 5, width = 35, height = 35)

    win_toplevel.mainloop()

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

def options_lvl01(x):
    global hearts
    global foods
    global level
    w = level
    level+=1
    show_way()

    if w == 1:
        window.title(f"Level 0{w+1}")
        if x == "A":
            lbl_toplevel = "Abcd"
            losewin_hearts = 0
            losewin_foods = -0.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 01 - A", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "B":
            lbl_toplevel = "Abcd"
            losewin_hearts = -1
            losewin_foods = 0

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 01 - B", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "C":
            lbl_toplevel = "Abcd"
            losewin_hearts = -0.5
            losewin_foods = +1.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 01 - C", lbl_toplevel, losewin_hearts, losewin_foods)

    elif w == 2:
        window.title(f"Level 0{w+1}")
        if x == "A":
            lbl_toplevel = "Abcd"
            losewin_hearts = 0
            losewin_foods = -0.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 02 - A", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "B":
            lbl_toplevel = "Abcd"
            losewin_hearts = -1
            losewin_foods = 0

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 02 - B", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "C":
            lbl_toplevel = "Abcd"
            losewin_hearts = -0.5
            losewin_foods = +1.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 02 - C", lbl_toplevel, losewin_hearts, losewin_foods)

    elif w == 3:
        window.title(f"Level 0{w+1}")
        if x == "A":
            lbl_toplevel = "Abcd"
            losewin_hearts = 0
            losewin_foods = -0.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 03 - A", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "B":
            lbl_toplevel = "Abcd"
            losewin_hearts = -1
            losewin_foods = 0

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 03 - B", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "C":
            lbl_toplevel = "Abcd"
            losewin_hearts = -0.5
            losewin_foods = +1.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 03 - C", lbl_toplevel, losewin_hearts, losewin_foods)

    elif w == 4:
        window.title(f"Level 0{w+1}")
        if x == "A":
            lbl_toplevel = "Abcd"
            losewin_hearts = 0
            losewin_foods = -0.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 04 - A", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "B":
            lbl_toplevel = "Abcd"
            losewin_hearts = -1
            losewin_foods = 0

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 04 - B", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "C":
            lbl_toplevel = "Abcd"
            losewin_hearts = -0.5
            losewin_foods = +1.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 04 - C", lbl_toplevel, losewin_hearts, losewin_foods)

    elif w == 5:
        window.title(f"Level 0{w+1}")
        if x == "A":
            lbl_toplevel = "Abcd"
            losewin_hearts = 0
            losewin_foods = -0.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 05 - A", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "B":
            lbl_toplevel = "Abcd"
            losewin_hearts = -1
            losewin_foods = 0

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 05 - B", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "C":
            lbl_toplevel = "Abcd"
            losewin_hearts = -0.5
            losewin_foods = +1.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 05 - C", lbl_toplevel, losewin_hearts, losewin_foods)

    elif w == 6:
        window.title(f"Level 0{w+1}")
        if x == "A":
            lbl_toplevel = "Abcd"
            losewin_hearts = 0
            losewin_foods = -0.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 06 - A", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "B":
            lbl_toplevel = "Abcd"
            losewin_hearts = -1
            losewin_foods = 0

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 06 - B", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "C":
            lbl_toplevel = "Abcd"
            losewin_hearts = -0.5
            losewin_foods = +1.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 06 - C", lbl_toplevel, losewin_hearts, losewin_foods)

    elif w == 7:
        window.title(f"Level 0{w+1}")
        if x == "A":
            lbl_toplevel = "Abcd"
            losewin_hearts = 0
            losewin_foods = -0.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 07 - A", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "B":
            lbl_toplevel = "Abcd"
            losewin_hearts = -1
            losewin_foods = 0

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 07 - B", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "C":
            lbl_toplevel = "Abcd"
            losewin_hearts = -0.5
            losewin_foods = +1.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 07 - C", lbl_toplevel, losewin_hearts, losewin_foods)

    elif w == 8:
        window.title(f"Level 01")
        if x == "A":
            lbl_toplevel = "Abcd"
            losewin_hearts = 0
            losewin_foods = -0.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 08 - A", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "B":
            lbl_toplevel = "Abcd"
            losewin_hearts = -1
            losewin_foods = 0

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 08 - B", lbl_toplevel, losewin_hearts, losewin_foods)

        elif x == "C":
            lbl_toplevel = "Abcd"
            losewin_hearts = -0.5
            losewin_foods = +1.5

            hearts += losewin_hearts
            show_heart()
            foods += losewin_foods
            show_food()

            show_toplevel("Level 08 - C", lbl_toplevel, losewin_hearts, losewin_foods)

#____________________________________________________________________________________________________________
#Tkinter

directory = os.path.dirname(__file__)

window = Tk()

game_over = bronze_key = silver_key = golden_key = wolfhide = False
lighter = True
world = level = 1
hearts = foods = 3

bg = fg = "#fafafa"
bg_frames = "#f1f1f1"
bg_narrative = "#252525"

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
window.configure(background = "#000")

#____________________________________________________________________________________________________________
#Main Menu 

#Frame
root = Frame(window, bd = 1, relief = "sunken", bg = bg)
root.place(x = 10, y = 10, width = width - 20, height = height - 20)

#Labels
lbl_01 = Label(root, text = " - Lost - ", bg=bg, font = "courier 40 bold")
lbl_02 = Label(root, text = "a chronicle of choices", bg=bg, font = "courier 32 bold", anchor = N)

#Buttons

btn_start = Button(root, text= "Start", bg=bg, bd = 2, relief = "ridge", command = lambda: start(), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)
btn_tutorial = Button(root, text= "Tutorial", bg=bg, bd = 2, relief = "ridge", command = lambda: tutorial(), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)
btn_credits = Button(root, text= "Credits", bg=bg, bd = 2, relief = "ridge", command = lambda: credits(), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)
btn_quit = Button(root, text= "Quit", bg=bg, bd = 2, relief = "ridge", command = lambda: quit(), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)

show_main_menu()

#____________________________________________________________________________________________________________
#Tutorial

def tutorial():
    window.title("Tutorial")

    clear_main_menu()

    btn_back.place(x = 225, y = 365, width = 250, height = 60)
    lbl_tutorial_01.place(x = 225, y = 150, width = 250, height = 60)

lbl_tutorial_01 = Label(root, text="By: Arthur V.B.S.", bg=bg, font = "courier 18 italic")
btn_back = Button(root, text= "Back", bg=bg, bd = 2, relief = "ridge", command = lambda: back(), cursor="hand2",
                    font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)

#____________________________________________________________________________________________________________
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
                    font = "courier 27 bold", activebackground="#ccc", activeforeground=fg)

#____________________________________________________________________________________________________________
#Levels

def start():
    window.title("Level 01")

    root_status.place(x = 0, y = 280, width = width - 23, height = 175)
    root_narrative.place(x = 0, y = 0, width = width - 23, height = 280)
    btn_back_start.place(x = 610, y = 120, width = 80, height = 40)

    clear_main_menu()

#Frame
root_status = Frame(root, bd = 1, relief = "ridge", bg = bg)
#root_status.place(x = 0, y = 280, width = width - 23, height = 175)

root_narrative = Frame(root, bd = 1, relief = "ridge", bg = bg_narrative)
#root_narrative.place(x = 0, y = 0, width = width - 23, height = 280)

root_hearts = Frame(root_status, bd = 1, relief = "sunken", bg = bg_frames)
root_hearts.place(x = 10, y = 10, width = 160, height = 40)

root_foods = Frame(root_status, bd = 1, relief = "sunken", bg = bg_frames)
root_foods.place(x = 180, y = 10, width = 160, height = 40)

root_keys = Frame(root_status, bd = 1, relief = "sunken", bg = bg_frames)
root_keys.place(x = 10, y = 60, width = 50, height = 100)

root_way = Frame(root_status, bd = 1, relief = "sunken", bg = bg_narrative)
root_way.place(x = 350, y = 0, width = 350, height = 50)

root_options = Frame(root_narrative, bd = 1, relief = "sunken", bg = bg)
root_options.place(x = -1, y = 220, width = 351, height = 60)

root_item_main = Frame(root_status, bd = 1, relief = "sunken", bg = bg_frames)
root_item_main.place(x = 180, y = 60, width = 160, height = 100)

root_item_01 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_01.place(x = 5, y = 5, width = 35, height = 40)

root_item_02 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_02.place(x = 44, y = 5, width = 35, height = 40)

root_item_03 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_03.place(x = 82, y = 5, width = 35, height = 40)

root_item_04 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_04.place(x = 120, y = 5, width = 35, height = 40)

root_item_05 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_05.place(x = 5, y = 55, width = 35, height = 40)

root_item_06 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_06.place(x = 44, y = 55, width = 35, height = 40)

root_item_07 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_07.place(x = 82, y = 55, width = 35, height = 40)

root_item_08 = Frame(root_item_main, bd = 2, relief = "groove", bg = bg)
root_item_08.place(x = 120, y = 55, width = 35, height = 40)

#buttons

btn_back_start = Button(root_status, text= "Menu", bg=bg, bd = 2, relief = "ridge", command = lambda: back(), cursor="hand2",
                    font = "courier 12 bold", activebackground="#ccc", activeforeground=fg)
btn_opt_A = Button(root_narrative, text= "- A -", bg=bg_frames, bd = 2, relief = "ridge", command = lambda: options_lvl01("A"),
                    cursor="hand2", font = "courier 16 bold", activebackground="#ccc", activeforeground=fg)
btn_opt_B = Button(root_narrative, text= "- B -", bg=bg_frames, bd = 2, relief = "ridge", command = lambda: options_lvl01("B"),
                    cursor="hand2", font = "courier 16 bold", activebackground="#ccc", activeforeground=fg)
btn_opt_C = Button(root_narrative, text= "- C -", bg=bg_frames, bd = 2, relief = "ridge", command = lambda: options_lvl01("C"),
                    cursor="hand2", font = "courier 16 bold", activebackground="#ccc", activeforeground=fg)

btn_back_start.place(x = 610, y = 120, width = 80, height = 40)
btn_opt_A.place(x = 10, y = 230, width = 100, height = 40)
btn_opt_B.place(x = 125, y = 230, width = 100, height = 40)
btn_opt_C.place(x = 240, y = 230, width = 100, height = 40)

#Labels

crossroads_text = "Você está caminhando a\n" + "algumas horas e está\n" + "começando a sentir fome.\n" + " Então você se depara com\n" \
"algumas frutinhas"

opt_A_text = "123"
opt_B_text = "245"
opt_C_text = "456"

lbl_crossroads = Label(root_narrative, text = crossroads_text, anchor=N, justify=CENTER, font = "courier 16 italic",
                        bg = bg_narrative, fg = fg)
lbl_opt_A = Label(root_narrative, text = f"- A - {opt_A_text}", anchor = NW, justify=CENTER, font = "courier 12 italic",
                        bg = bg_narrative, fg = fg)
lbl_opt_B = Label(root_narrative, text = f"- B - {opt_B_text}", anchor = NW, justify=CENTER, font = "courier 12 italic",
                        bg = bg_narrative, fg = fg)
lbl_opt_C = Label(root_narrative, text = f"- C - {opt_C_text}", anchor = NW, justify=CENTER, font = "courier 12 italic",
                        bg = bg_narrative, fg = fg)

lbl_crossroads.place(x = 10, y = 10, width = 330, height = 200)
lbl_opt_A.place(x = 360, y = 10, width = 330, height = 80)
lbl_opt_B.place(x = 360, y = 100, width = 330, height = 80)
lbl_opt_C.place(x = 360, y = 190, width = 330, height = 80)

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

just_way_dic = PhotoImage(file = directory + "/Arts/W_and_I/just_way.png")
way_dic = PhotoImage(file = directory + "/Arts/W_and_I/way.png")

item_lighter_dic = PhotoImage(file = directory + "/Arts/W_and_I/item_lighter.png")

#Hearts, Foods, Keys and ways - Labels

lbl_item_lighter = Label(root_item_01, image = empty_00_dic, bg = bg)
lbl_item_lighter.place(x = 0, y = 2.5, width = 30, height = 30)

lbl_item_wolfhide = Label(root_item_02, image = empty_00_dic, bg = bg)
lbl_item_wolfhide.place(x = 0, y = 2.5, width = 30, height = 30)

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

lbl_just_way_01 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_01.place(x = 7.5, y = 5, width = 35, height = 35)
lbl_just_way_02 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_02.place(x = 50, y = 5, width = 35, height = 35)
lbl_just_way_03 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_03.place(x = 92.5, y = 5, width = 35, height = 35)
lbl_just_way_04 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_04.place(x = 135, y = 5, width = 35, height = 35)
lbl_just_way_05 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_05.place(x = 177.5, y = 5, width = 35, height = 35)
lbl_just_way_06 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_06.place(x = 220, y = 5, width = 35, height = 35)
lbl_just_way_07 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_07.place(x = 262.5, y = 5, width = 35, height = 35)
lbl_just_way_08 = Label(root_way, image = just_way_dic, bg = bg_narrative)
lbl_just_way_08.place(x = 305, y = 5, width = 35, height = 35)

main_dic = PhotoImage(file= directory + "/Arts/main.png")
lbl_main = Label(root_status, image = main_dic, bg = bg)
lbl_main.place(x = 70, y = 60)

show_heart()
show_food()
show_key()
show_way()
show_item()

window.mainloop()
