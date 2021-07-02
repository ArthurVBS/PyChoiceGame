from tkinter import *

def images(directory):
    images = {
        'empty_00_dic' : PhotoImage(file= directory + "/Images/empty.png"),
        'empty_01_dic' : PhotoImage(file= directory + "/Images/empty_plus.png"),
        'Sam_dic' : PhotoImage(file= directory + "/Images/Sam.png"),

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

def roots(root, bg, bg_frames, bg_narrative):
    roots = {
        'root_status' : Frame(root, bd = 1, relief = "ridge", bg = bg),
        'root_narrative' : Frame(root, bd = 1, relief = "ridge", bg = bg_narrative),
        'root_volume' : Frame(root, bd = 1, relief = "ridge", bg = bg)}

    return roots

def sub_roots(roots, bg, bg_frames, bg_narrative):
    sub_roots = {
        'root_hearts' : Frame(roots['root_status'], bd = 1, relief = "sunken", bg = bg_frames),
        'root_foods' : Frame(roots['root_status'], bd = 1, relief = "sunken", bg = bg_frames),
        'root_keys' : Frame(roots['root_status'], bd = 1, relief = "sunken", bg = bg_frames),
        'root_way' : Frame(roots['root_status'], bd = 1, relief = "sunken", bg = bg_narrative),
        'root_options' : Frame(roots['root_narrative'], bd = 1, relief = "sunken", bg = bg),
        'root_scenario' : Frame(roots['root_status'], bd = 0.5, relief = "groove", bg = bg_frames),
        'root_item_main' : Frame(roots['root_status'], bd = 1, relief = "sunken", bg = bg_frames)}

    sub_roots['root_hearts'].place(x = 10, y = 10, width = 160, height = 40)
    sub_roots['root_foods'].place(x = 180, y = 10, width = 160, height = 40)
    sub_roots['root_keys'].place(x = 10, y = 60, width = 50, height = 100)
    sub_roots['root_way'].place(x = 350, y = 0, width = 350, height = 50)
    sub_roots['root_options'].place(x = -1, y = 220, width = 351, height = 60)
    sub_roots['root_scenario'].place(x = 350, y = 60, width = 250, height = 100)
    sub_roots['root_item_main'].place(x = 180, y = 60, width = 160, height = 100)

    return sub_roots

def sub_sub_roots(sub_roots, bg, bg_frames, bg_narrative):
    sub_sub_roots = {
        'root_item_01' : Frame(sub_roots['root_item_main'], bd = 2, relief = "groove", bg = bg),
        'root_item_02' : Frame(sub_roots['root_item_main'], bd = 2, relief = "groove", bg = bg),
        'root_item_03' : Frame(sub_roots['root_item_main'], bd = 2, relief = "groove", bg = bg),
        'root_item_04' : Frame(sub_roots['root_item_main'], bd = 2, relief = "groove", bg = bg),
        'root_item_05' : Frame(sub_roots['root_item_main'], bd = 2, relief = "groove", bg = bg),
        'root_item_06' : Frame(sub_roots['root_item_main'], bd = 2, relief = "groove", bg = bg),
        'root_item_07' : Frame(sub_roots['root_item_main'], bd = 2, relief = "groove", bg = bg),
        'root_item_08' : Frame(sub_roots['root_item_main'], bd = 2, relief = "groove", bg = bg)}

    sub_sub_roots['root_item_01'].place(x = 5, y = 5, width = 35, height = 40)
    sub_sub_roots['root_item_02'].place(x = 44, y = 5, width = 35, height = 40)
    sub_sub_roots['root_item_03'].place(x = 82, y = 5, width = 35, height = 40)
    sub_sub_roots['root_item_04'].place(x = 120, y = 5, width = 35, height = 40)
    sub_sub_roots['root_item_05'].place(x = 5, y = 55, width = 35, height = 40)
    sub_sub_roots['root_item_06'].place(x = 44, y = 55, width = 35, height = 40)
    sub_sub_roots['root_item_07'].place(x = 82, y = 55, width = 35, height = 40)
    sub_sub_roots['root_item_08'].place(x = 120, y = 55, width = 35, height = 40)

    return sub_sub_roots

def labels(roots, bg, bg_frames, bg_narrative, fg, images, sub_roots, sub_sub_roots):
    labels = {
        'lbl_Sam' : Label(roots['root_status'], image = images['Sam_dic'], bg = bg, anchor = CENTER),
        'lbl_scenario' : Label(sub_roots['root_scenario'], image = images['empty_00_dic'], bg = bg),

        'lbl_heart_01' : Label(sub_roots['root_hearts'], image = images['empty_00_dic'], bg = bg_frames),
        'lbl_heart_02' : Label(sub_roots['root_hearts'], image = images['empty_00_dic'], bg = bg_frames),
        'lbl_heart_03' : Label(sub_roots['root_hearts'], image = images['empty_00_dic'], bg = bg_frames),
        'lbl_heart_04' : Label(sub_roots['root_hearts'], image = images['empty_00_dic'], bg = bg_frames),
        'lbl_heart_05' : Label(sub_roots['root_hearts'], image = images['empty_00_dic'], bg = bg_frames),
        
        'lbl_food_01' : Label(sub_roots['root_foods'], image = images['empty_00_dic'], bg = bg_frames),
        'lbl_food_02' : Label(sub_roots['root_foods'], image = images['empty_00_dic'], bg = bg_frames),
        'lbl_food_03' : Label(sub_roots['root_foods'], image = images['empty_00_dic'], bg = bg_frames),
        'lbl_food_04' : Label(sub_roots['root_foods'], image = images['empty_00_dic'], bg = bg_frames),
        'lbl_food_05' : Label(sub_roots['root_foods'], image = images['empty_00_dic'], bg = bg_frames),

        'lbl_key_B' : Label(sub_roots['root_keys'], image = images['empty_00_dic'], bg = bg_frames),
        'lbl_key_S' : Label(sub_roots['root_keys'], image = images['empty_00_dic'], bg = bg_frames),
        'lbl_key_G' : Label(sub_roots['root_keys'], image = images['empty_00_dic'], bg = bg_frames),

        'lbl_just_way_01' : Label(sub_roots['root_way'], image = images['just_way_dic'], bg = bg_narrative),
        'lbl_just_way_02' : Label(sub_roots['root_way'], image = images['just_way_dic'], bg = bg_narrative),
        'lbl_just_way_03' : Label(sub_roots['root_way'], image = images['just_way_dic'], bg = bg_narrative),
        'lbl_just_way_04' : Label(sub_roots['root_way'], image = images['just_way_dic'], bg = bg_narrative),
        'lbl_just_way_05' : Label(sub_roots['root_way'], image = images['just_way_dic'], bg = bg_narrative),
        'lbl_just_way_06' : Label(sub_roots['root_way'], image = images['just_way_dic'], bg = bg_narrative),
        'lbl_just_way_07' : Label(sub_roots['root_way'], image = images['just_way_dic'], bg = bg_narrative),
        'lbl_just_way_08' : Label(sub_roots['root_way'], image = images['just_way_dic'], bg = bg_narrative),

        'lbl_item_lighter' : Label(sub_sub_roots['root_item_01'], image = images['empty_01_dic'], bg = bg),
        'lbl_item_wolfhide' : Label(sub_sub_roots['root_item_02'], image = images['empty_01_dic'], bg = bg),
        'lbl_item_future_friendship' : Label(sub_sub_roots['root_item_03'], image = images['empty_01_dic'], bg = bg),
        'lbl_item_nausea' : Label(sub_sub_roots['root_item_04'], image = images['empty_01_dic'], bg = bg),
        'lbl_item_shotgun' : Label(sub_sub_roots['root_item_05'], image = images['empty_01_dic'], bg = bg),
        'lbl_item_crowbar' : Label(sub_sub_roots['root_item_06'], image = images['empty_01_dic'], bg = bg),
        'lbl_item_screwdriver' : Label(sub_sub_roots['root_item_07'], image = images['empty_01_dic'], bg = bg),
        'lbl_item_gear' : Label(sub_sub_roots['root_item_08'], image = images['empty_01_dic'], bg = bg),
        
        'lbl_crossroads' : Label(roots['root_narrative'], text = "", anchor=CENTER, justify=CENTER, font = "courier 14 italic",
                                bg = bg_narrative, fg = fg),
        'lbl_opt_A' : Label(roots['root_narrative'], text = "", anchor = NW, justify=LEFT, font = "courier 12 italic",
                                bg = bg_narrative, fg = fg),
        'lbl_opt_B' : Label(roots['root_narrative'], text = "", anchor = NW, justify=LEFT, font = "courier 12 italic",
                                bg = bg_narrative, fg = fg),
        'lbl_opt_C' : Label(roots['root_narrative'], text = "", anchor = NW, justify=LEFT, font = "courier 12 italic",
                                bg = bg_narrative, fg = fg)}

    labels['lbl_Sam'].place(x = 70, y = 60)

    labels['lbl_scenario'].place(x = 5, y = 5, width = 240, height = 90)
    labels['lbl_heart_01'].place(x = 5, y = 5, width = 30, height = 30)
    labels['lbl_heart_02'].place(x = 35, y = 5, width = 30, height = 30)
    labels['lbl_heart_03'].place(x = 65, y = 5, width = 30, height = 30)
    labels['lbl_heart_04'].place(x = 95, y = 5, width = 30, height = 30)
    labels['lbl_heart_05'].place(x = 125, y = 5, width = 30, height = 30)

    labels['lbl_food_01'].place(x = 5, y = 5, width = 30, height = 30)
    labels['lbl_food_02'].place(x = 35, y = 5, width = 30, height = 30)
    labels['lbl_food_03'].place(x = 65, y = 5, width = 30, height = 30)
    labels['lbl_food_04'].place(x = 95, y = 5, width = 30, height = 30)
    labels['lbl_food_05'].place(x = 125, y = 5, width = 30, height = 30)

    labels['lbl_key_B'].place(x = 10, y = 5, width = 30, height = 30)
    labels['lbl_key_S'].place(x = 10, y = 35, width = 30, height = 30)
    labels['lbl_key_G'].place(x = 10, y = 65, width = 30, height = 30)

    labels['lbl_just_way_01'].place(x = 7.5, y = 5, width = 35, height = 35)
    labels['lbl_just_way_02'].place(x = 50, y = 5, width = 35, height = 35)
    labels['lbl_just_way_03'].place(x = 92.5, y = 5, width = 35, height = 35)
    labels['lbl_just_way_04'].place(x = 135, y = 5, width = 35, height = 35)
    labels['lbl_just_way_05'].place(x = 177.5, y = 5, width = 35, height = 35)
    labels['lbl_just_way_06'].place(x = 220, y = 5, width = 35, height = 35)
    labels['lbl_just_way_07'].place(x = 262.5, y = 5, width = 35, height = 35)
    labels['lbl_just_way_08'].place(x = 305, y = 5, width = 35, height = 35)

    labels['lbl_item_lighter'].place(x = 0, y = 2.5, width = 30, height = 30)
    labels['lbl_item_wolfhide'].place(x = 0, y = 2.5, width = 30, height = 30)
    labels['lbl_item_future_friendship'].place(x = 0, y = 2.5, width = 30, height = 30)
    labels['lbl_item_nausea'].place(x = 0, y = 2.5, width = 30, height = 30)
    labels['lbl_item_shotgun'].place(x = 0, y = 2.5, width = 30, height = 30)
    labels['lbl_item_crowbar'].place(x = 0, y = 2.5, width = 30, height = 30)
    labels['lbl_item_screwdriver'].place(x = 0, y = 2.5, width = 30, height = 30)
    labels['lbl_item_gear'].place(x = 0, y = 2.5, width = 30, height = 30)

    labels['lbl_crossroads'].place(x = 10, y = 10, width = 330, height = 200)
    labels['lbl_opt_A'].place(x = 360, y = 10, width = 330, height = 80)
    labels['lbl_opt_B'].place(x = 360, y = 100, width = 330, height = 80)
    labels['lbl_opt_C'].place(x = 360, y = 190, width = 330, height = 80)

    return labels

def buttons(roots, bg, bg_frames, bg_narrative, fg, options, click_back_with_sound):
    buttons = {
        'btn_back_newgame' : Button(roots['root_status'], text= "Voltar", bg=bg, bd = 2, relief = "ridge", command = lambda: click_back_with_sound(), cursor="hand2",
                            font = "courier 12 bold", activebackground="#ccc", activeforeground=fg),
        'btn_opt_A' : Button(roots['root_narrative'], text= "- A -", bg=bg_frames, bd = 2, relief = "ridge", command = lambda: options("A"),
                            cursor="hand2", font = "courier 16 bold", activebackground="#ccc", activeforeground=fg),
        'btn_opt_B' : Button(roots['root_narrative'], text= "- B -", bg=bg_frames, bd = 2, relief = "ridge", command = lambda: options("B"),
                            cursor="hand2", font = "courier 16 bold", activebackground="#ccc", activeforeground=fg),
        'btn_opt_C' : Button(roots['root_narrative'], text= "- C -", bg=bg_frames, bd = 2, relief = "ridge", command = lambda: options("C"),
                            cursor="hand2", font = "courier 16 bold", activebackground="#ccc", activeforeground=fg)}

    #buttons['btn_back_newgame'].place(x = 610, y = 60, width = 80, height = 100)
    buttons['btn_opt_A'].place(x = 10, y = 230, width = 100, height = 40)
    buttons['btn_opt_B'].place(x = 125, y = 230, width = 100, height = 40)
    buttons['btn_opt_C'].place(x = 240, y = 230, width = 100, height = 40)

    return buttons
