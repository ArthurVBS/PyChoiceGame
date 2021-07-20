#Import - Libraries _________________________________________________________________________________________

from tkinter import *

#Function - Images __________________________________________________________________________________________

def images(directory):
    images = {
        'empty_00_dic' : PhotoImage(file= directory + "/Images/empty.png"),
        'empty_01_dic' : PhotoImage(file= directory + "/Images/empty_plus.png"),
        'Sam_dic' : PhotoImage(file= directory + "/Images/Sam.png"),
        'back_dic' : PhotoImage(file= directory + "/Images/back.png"),

        'flag_UK_dic' : PhotoImage(file= directory + "/Images/Nations/UK.png"),
        'flag_FR_dic' : PhotoImage(file= directory + "/Images/Nations/FR.png"),
        'flag_BR_dic' : PhotoImage(file= directory + "/Images/Nations/BR.png"),
        'flag_SP_dic' : PhotoImage(file= directory + "/Images/Nations/SP.png"),
        'flag_GE_dic' : PhotoImage(file= directory + "/Images/Nations/GE.png"),

        'vol_max_dic' : PhotoImage(file= directory + "/Images/Volume/vol_max.png"),
        'vol_plus_dic' : PhotoImage(file= directory + "/Images/Volume/vol_plus.png"),
        'vol_minus_dic' : PhotoImage(file= directory + "/Images/Volume/vol_minus.png"),
        'vol_mute_dic' : PhotoImage(file= directory + "/Images/Volume/vol_mute.png"),
        
        'scenario_01_dic' : PhotoImage(file= directory + "/Images/Scenarios/Scenario_01.png"),
        'scenario_02_dic' : PhotoImage(file= directory + "/Images/Scenarios/Scenario_02.png"),
        'scenario_03_dic' : PhotoImage(file= directory + "/Images/Scenarios/Scenario_03.png"),

        'heart_11_dic' : PhotoImage(file= directory + "/Images/Hearts/heart_11.png"),
        'heart_01_dic' : PhotoImage(file= directory + "/Images/Hearts/heart_01.png"),
        'heart_00_dic' : PhotoImage(file= directory + "/Images/Hearts/heart_00.png"),

        'food_11_dic' : PhotoImage(file= directory + "/Images/Foods/food_11.png"),
        'food_01_dic' : PhotoImage(file= directory + "/Images/Foods/food_01.png"),
        'food_00_dic' : PhotoImage(file= directory + "/Images/Foods/food_00.png"),

        'key_E_dic' : PhotoImage(file= directory + "/Images/Keys/Key_E.png"),
        'key_B_dic' : PhotoImage(file= directory + "/Images/Keys/Key_B.png"),
        'key_S_dic' : PhotoImage(file= directory + "/Images/Keys/Key_S.png"), 
        'key_G_dic' : PhotoImage(file= directory + "/Images/Keys/Key_G.png"),

        'just_way_dic' : PhotoImage(file = directory + "/Images/Ways/just_way.png"),
        'way_dic' : PhotoImage(file = directory + "/Images/Ways/way.png"),

        'item_lighter_dic' : PhotoImage(file = directory + "/Images/Items/item_lighter.png"),
        'item_wolfhide_dic' : PhotoImage(file = directory + "/Images/Items/item_wolfhide.png"),
        'item_future_friendship_dic' : PhotoImage(file = directory + "/Images/Items/item_future_friendship.png"),
        'item_nausea_dic' : PhotoImage(file = directory + "/Images/Items/item_nausea.png"),
        'item_shotgun_dic' : PhotoImage(file = directory + "/Images/Items/item_shotgun.png"),
        'item_crowbar_dic' : PhotoImage(file = directory + "/Images/Items/item_crowbar.png"),
        'item_screwdriver_dic' : PhotoImage(file = directory + "/Images/Items/item_screwdriver.png"),
        'item_gear_dic' : PhotoImage(file = directory + "/Images/Items/item_gear.png")}

    return images

