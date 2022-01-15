#Import - Libs

from tkinter import *

#Function - Assets

def images(directory):
    images = {
        'empty_00_dic' : PhotoImage(file= directory + "/Assets/Empty/empty.png"),
        'empty_01_dic' : PhotoImage(file= directory + "/Assets/Empty/empty_plus.png"),

        'vol_max_dic' : PhotoImage(file= directory + "/Assets/Volume/vol_max.png"),
        'vol_plus_dic' : PhotoImage(file= directory + "/Assets/Volume/vol_plus.png"),
        'vol_minus_dic' : PhotoImage(file= directory + "/Assets/Volume/vol_minus.png"),
        'vol_mute_dic' : PhotoImage(file= directory + "/Assets/Volume/vol_mute.png"),
        
        'scenario_01_dic' : PhotoImage(file= directory + "/Assets/Scenarios/Scenario_01.png"),
        'scenario_02_dic' : PhotoImage(file= directory + "/Assets/Scenarios/Scenario_02.png"),
        'scenario_03_dic' : PhotoImage(file= directory + "/Assets/Scenarios/Scenario_03.png"),

        'heart_11_dic' : PhotoImage(file= directory + "/Assets/Hearts/heart_11.png"),
        'heart_01_dic' : PhotoImage(file= directory + "/Assets/Hearts/heart_01.png"),
        'heart_00_dic' : PhotoImage(file= directory + "/Assets/Hearts/heart_00.png"),

        'food_11_dic' : PhotoImage(file= directory + "/Assets/Foods/food_11.png"),
        'food_01_dic' : PhotoImage(file= directory + "/Assets/Foods/food_01.png"),
        'food_00_dic' : PhotoImage(file= directory + "/Assets/Foods/food_00.png"),

        'key_E_dic' : PhotoImage(file= directory + "/Assets/Keys/Key_E.png"),
        'key_B_dic' : PhotoImage(file= directory + "/Assets/Keys/Key_B.png"),
        'key_S_dic' : PhotoImage(file= directory + "/Assets/Keys/Key_S.png"), 
        'key_G_dic' : PhotoImage(file= directory + "/Assets/Keys/Key_G.png"),

        'just_way_dic' : PhotoImage(file = directory + "/Assets/Ways/just_way.png"),
        'way_dic' : PhotoImage(file = directory + "/Assets/Ways/way.png"),

        'item_lighter_dic' : PhotoImage(file = directory + "/Assets/Items/item_lighter.png"),
        'item_wolfhide_dic' : PhotoImage(file = directory + "/Assets/Items/item_wolfhide.png"),
        'item_future_friendship_dic' : PhotoImage(file = directory + "/Assets/Items/item_future_friendship.png"),
        'item_nausea_dic' : PhotoImage(file = directory + "/Assets/Items/item_nausea.png"),
        'item_shotgun_dic' : PhotoImage(file = directory + "/Assets/Items/item_shotgun.png"),
        'item_crowbar_dic' : PhotoImage(file = directory + "/Assets/Items/item_crowbar.png"),
        'item_screwdriver_dic' : PhotoImage(file = directory + "/Assets/Items/item_screwdriver.png"),
        'item_gear_dic' : PhotoImage(file = directory + "/Assets/Items/item_gear.png")}

    return images
