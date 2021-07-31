#Import - Libraries _________________________________________________________________________________________

from tkinter import *

#Function - Assets __________________________________________________________________________________________

def assets(directory):
    assets = {
        'rock_dic' : PhotoImage(file= directory + "/Assets/rock.png"),
        'paper_dic' : PhotoImage(file= directory + "/Assets/paper.png"),
        'scissors_dic' : PhotoImage(file= directory + "/Assets/scissors.png"),
        'question_mark_dic' : PhotoImage(file= directory + "/Assets/question_mark.png")}

    return assets
