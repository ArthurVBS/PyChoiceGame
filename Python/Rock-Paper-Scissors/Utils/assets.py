#Import - Libraries _________________________________________________________________________________________

from tkinter import *

#Function - Assets __________________________________________________________________________________________

def assets(directory):
    assets = {
        'rock_dic' : PhotoImage(file= directory + "/Assets/rock.png"),
        'paper_dic' : PhotoImage(file= directory + "/Assets/paper.png"),
        'scissors_dic' : PhotoImage(file= directory + "/Assets/scissors.png")}

    return assets
