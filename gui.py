# gui.py

import PySimpleGUI as sg
from formation import func

class Gui:
    def __init__(self):
        sz = (10, 2)
        col1 = [
            [sg.Text('Fire', background_color='red', size=sz)],
            [sg.Button('F1', key='F1')],
            [sg.Button('F2')],
            [sg.Button('F3')],
            [sg.Button('F4')],
            [sg.Button('F5')],
            [sg.Button('F6')],
            [sg.Button('F7')],
            [sg.Button('F8')],
            [sg.Button('F9')],
            [sg.Button('F10')],
            [sg.Button('F11')],
            [sg.Button('F12')],]
        col2 = [[sg.Text('Water', background_color='blue', size=sz)],
            [sg.Button('W1')],
            [sg.Button('W2')],
            [sg.Button('W3')],
            [sg.Button('W4')],
            [sg.Button('W5')],
            [sg.Button('W6')],
            [sg.Button('W7')],
            [sg.Button('W8')],
            [sg.Button('W9')],
            [sg.Button('W10')],
            [sg.Button('W11')],
            [sg.Button('W12')],]
        col3 = [[sg.Text('Air', background_color='gray', size=sz)],
            [sg.Button('A1')],
            [sg.Button('A2')],
            [sg.Button('A3')],
            [sg.Button('A4')],
            [sg.Button('A5')],
            [sg.Button('A6')],
            [sg.Button('A7')],
            [sg.Button('A8')],
            [sg.Button('A9')],
            [sg.Button('A10')],
            [sg.Button('A11')],
            [sg.Button('A12')],]
        col4 = [[sg.Text('Earth', background_color='green', size=sz)],
            [sg.Button('E1')],
            [sg.Button('E2')],
            [sg.Button('E3')],
            [sg.Button('E4')],
            [sg.Button('E5')],
            [sg.Button('E6')],
            [sg.Button('E7')],
            [sg.Button('E8')],
            [sg.Button('E9')],
            [sg.Button('E10')],
            [sg.Button('E11')],
            [sg.Button('E12')],]
        col5 = [[sg.Text('Special', background_color='black', size=sz)],
            [sg.Button('S1')],
            [sg.Button('S2')],
            [sg.Button('S3')],
            [sg.Button('S4')],
            [sg.Button('S5')],
            [sg.Button('S6')],
            [sg.Button('S7')],
            [sg.Button('S8')],]

        layout1 = [
            [sg.Button("DEL"), sg.Button('FIX'), sg.Button('?'), sg.Button('REF'), sg.Button('DET'), sg.Text('DEL', key='hint', background_color='black')],
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
    if event == '?':
        window['hint'].update('?', background_color='yellow', text_color='black')
        state = 2
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
                    window.FindElement(event).Update(visible=False)
                if state == 1:
                    window.FindElement(event).Update(button_color = ('', 'red'))
                if state == 2:
                    window.FindElement(event).Update(button_color = ('', '#e8d687'))
        mana_column+=1

    # if event == 'S1':
    #     if state == 0:
    #         window.FindElement(event).Update(visible=False)
    #     if state == 1:
    #         window.FindElement(event).Update(button_color = ('', 'red'))
    # if event == 'S2':
    #     if state == 0:
    #         window.FindElement(event).Update(visible=False)
    #     if state == 1:
    #         window.FindElement(event).Update(button_color = ('', 'red'))     
    # if event == 'S3':
    #     if state == 0:
    #         window.FindElement(event).Update(visible=False)
    #     if state == 1:
    #         window.FindElement(event).Update(button_color = ('', 'red'))
    # if event == 'S4':
    #     if state == 0:
    #         window.FindElement(event).Update(visible=False)
    #     if state == 1:
    #         window.FindElement(event).Update(button_color = ('', 'red'))  
    # if event == 'S5':
    #     if state == 0:
    #         window.FindElement(event).Update(visible=False)
    #     if state == 1:
    #         window.FindElement(event).Update(button_color = ('', 'red'))
    # if event == 'S6':
    #     if state == 0:
    #         window.FindElement(event).Update(visible=False)
    #     if state == 1:
    #         window.FindElement(event).Update(button_color = ('', 'red'))     
    # if event == 'S7':
    #     if state == 0:
    #         window.FindElement(event).Update(visible=False)
    #     if state == 1:
    #         window.FindElement(event).Update(button_color = ('', 'red'))
    # if event == 'S8':
    #     if state == 0:
    #         window.FindElement(event).Update(visible=False)
    #     if state == 1:
    #         window.FindElement(event).Update(button_color = ('', 'red'))  
    
    
window.close()
