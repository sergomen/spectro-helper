# gui.py

import PySimpleGUI as sg
from formation import func
from readcv import number_list

class Gui:
    def __init__(self):
        sz = (10, 2)
        fire = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12']
        water = ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10', 'W11', 'W12']
        air = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12']
        earth = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12']
        special = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']
        col1 = [[sg.Text('Fire', background_color='red', size=sz)]]
        # Create several similar fire buttons in the vertical column
        for card in fire:
            col1 += [
                [sg.Button(card, key=card)]
            ]
        col2 = [[sg.Text('Water', background_color='blue', size=sz)]]
        for card in water:
            col2 += [
                [sg.Button(card, key=card)]
            ]
        col3 = [[sg.Text('Air', background_color='gray', size=sz)]]
        for card in air:
            col3 += [
                [sg.Button(card, key=card)]
            ]
        col4 = [[sg.Text('Earth', background_color='green', size=sz)]]
        for card in earth:
            col4 += [
                [sg.Button(card, key=card)]
            ]
        col5 = [[sg.Text('Special', background_color='black', size=sz)]]
        for card in special:
            col5 += [
                [sg.Button(card, key=card)]
            ]

        # -------------------------Create the two layouts this window will display------------------- 
        layout1 = [
            [sg.Button("DEL"), sg.Button('FIX'), sg.Button('?'), sg.Button('REF'), sg.Button('PTN'), sg.Button('DET'), sg.Text('DEL', key='hint', background_color='black')],
            [
            sg.Column(col1, element_justification='c'), 
            sg.Column(col2, element_justification='c'), 
            sg.Column(col3, element_justification='c'), 
            sg.Column(col4, element_justification='c'), 
            sg.Column(col5, element_justification='c')
            ],
        ]

        layout2 = [
            [sg.Text("Hello from PySimpleGUI")]
        ]

        self.layout = [
            [sg.Column(layout1, key='-COL1-'), sg.Column(layout2, key='-COL2', visible=False)],
        ]

        

gui = Gui()
window = sg.Window("spectro-helper", gui.layout)
state = 0


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'DEL':
        state = 0
        window['hint'].update('DEL', background_color='black', text_color='white')
    if event == 'FIX':
        state = 1
        window['hint'].update('FIX', background_color='red', text_color='white')
    if event == '?':
        window['hint'].update('?', background_color='yellow', text_color='black')
        state = 2
    if event == 'REF':
        window['hint'].update('REF', background_color='green', text_color='white')
        mana_column = 0 
        mana_list = ['F', 'W', 'A', 'E', 'S']
        while mana_column < len(mana_list):
            # Divide bacis elements from Specialization
            if mana_list[mana_column] == 'S':
                card_count = 8
            else:
                card_count = 12
            # Refresh all card buttons
            for card_number in range(1, card_count+1):
                btn_key = f"{mana_list[mana_column]}{card_number}"
                window[str(btn_key)].Update(visible=True, button_color = ('white','#102b4a'))
                # window[str(btn_key)].Update(button_color = ('', ''))
            mana_column+=1
    
    if event == 'PTN':
        for i in range(0, 4):
            window[str(f"F{number_list[i]}")].Update(visible=False)
        for i in range(4, 8):
            window[str(f"W{number_list[i]}")].Update(visible=False)
        for i in range(8, 12):
            window[str(f"A{number_list[i]}")].Update(visible=False)
        for i in range(12, 16):
            window[str(f"E{number_list[i]}")].Update(visible=False)
    if event == 'DET':
        window['hint'].update('DET')
        window[f'-COL2'].update(visible=True)

    # RENDERING WINDOW
    mana_column = 0 
    mana_list = ['F', 'W', 'A', 'E', 'S']
    while mana_column < len(mana_list):
        if mana_list[mana_column] == 'S':
                card_count = 8
        else:
                card_count = 12
        for card_number in range(1, card_count+1):
            if event == f"{mana_list[mana_column]}{card_number}":
                if state == 0:
                    window[event].Update(visible=False)
                if state == 1:
                    window[event].Update(button_color = ('', 'red'))
                if state == 2:
                    window[event].Update(button_color = ('', '#e8d687'))
        mana_column+=1
 
window.close()
