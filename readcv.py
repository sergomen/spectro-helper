#------------------THERE WE WILL USE OPENCV & PYTESSERACT--------------
import cv2
import pytesseract
from pytesseract import Output
import pandas as pd

from PIL import Image, ImageGrab, ImageChops
import numpy as np

printscreen = np.array(ImageGrab.grab(bbox=(0,0,1024,800)))
# printscreen = np.array(pyautogui.screenshot(region=(0, 0, 1024, 800)))
cv2.imshow('captured text2', printscreen)
# cv2.imwrite('', printscreen)
# printscreen.save("spell2.png")
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"
number_list = []
# Reading image using opencv
# image = cv2.imread('image.png')
# (height,width) = image.shape[:2]
# image = cv2.resize(image, (width*4, height*4))
# Converting image into gray scale image
gray_image = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
# Converting it to binary image by Thresholding
threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)[1]
# Configuring parameters for tesseract
# threshold_img = 255 - cv2.GaussianBlur(threshold_img, (5,5), 0)
# Get part of image
# card_img = threshold_img[300:800, 500:1200]
# spell_img = printscreen[552:575, 566:589]
# spell2_img = printscreen[552:575, 566:589]
spell_img = np.array(Image.open("spell_img.png"))
spell2_img = printscreen[585:592, 575:595] #y+7
# diff = cv2.absdiff(spell_img, spell2_img)
# print(diff[0][0][0])
# cv2.imwrite('spell_img.png', spell2_img)
cv2.imshow('Is spell?', spell2_img)

# diff = ImageChops.difference(spell_img, spell2_img)
# print(diff.getbbox())
# diff.show()
# if spell_img == cv2.imread('spell.jpg'):
#     print("YES")
# cv2.imshow('Spell', diff)
# print(diff)
# for card in range(17):
spell2_img = printscreen[480:487, 580:592]
cv2.imshow('Difference', spell2_img)
# diff = cv2.absdiff(spell_img, spell2_img)
# print(diff[0][0][0])
#     if threshold[m1:m2: n1:n2] == spell_img:
#         y1, y2, x1, x2 = 
#     else:
#         y1, y2, x1, x2 = 
#     card = threshold_img[y1:y2, x1:x2]
# Creating the Pandas DataFrame
# df = pd.DataFrame({ 'y1':[370, 480, 586, 688],
#                     'y2':[377, 487, 593, 695],
#                     'x1':[580, 575, ],
#                     'x2':[]})
card_f1 = threshold_img[375:392, 575:595] #y, x
card_f2 = threshold_img[480:496, 575:595]
card_f3 = threshold_img[585:599, 577:595]
card_f4 = threshold_img[688:704, 577:595]

card_w1 = threshold_img[376:392, 682:698] # circle4
card_w2 = threshold_img[480:496, 682:699] # square
card_w3 = threshold_img[585:599, 682:699] # square
card_w4 = threshold_img[688:704, 682:699] # square

card_a1 = threshold_img[375:392, 788:801] # square
card_a2 = threshold_img[480:496, 788:801] # square
card_a3 = threshold_img[585:599, 788:801] # circle
card_a4 = threshold_img[688:704, 788:802] # circle

card_e1 = threshold_img[374:392, 892:904] # circle
card_e2 = threshold_img[480:496, 892:904] # circle
card_e3 = threshold_img[586:599, 892:904] # square
card_e4 = threshold_img[688:704, 892:904] # square
# y1+=8 y2+=9
#spell_f1
spell_f2 = threshold_img[488:505, 575:595]
spell_f3 = threshold_img[593:608, 577:595] # changed
spell_f4 = threshold_img[696:713, 575:595]

spell_w1 = threshold_img[384:401, 682:699] # changed
spell_w2 = threshold_img[488:505, 682:699]
spell_w3 = threshold_img[593:608, 682:699]
#spell_w4

spell_a1 = threshold_img[383:401, 788:801]
spell_a2 = threshold_img[488:505, 788:801]
spell_a3 = threshold_img[593:608, 788:801]
spell_a4 = threshold_img[696:713, 788:801]

spell_e1 = threshold_img[383:401, 892:904]
spell_e2 = threshold_img[488:504, 893:904]
spell_e3 = threshold_img[593:608, 890:904]
#spell_e4
df_spell = pd.DataFrame({ 
                    'y1':[383, 488, 593, 696, 384, 488, 593, 696, 383, 488, 593, 696, 383, 488, 593, 696],
                    'y2':[401, 505, 608, 713, 401, 505, 608, 713, 401, 505, 608, 713, 401, 504, 608, 713],
                    'x1':[575, 575, 577, 575, 682, 682, 682, 788, 788, 788, 788, 788, 892, 893, 892, 892],
                    'x2':[595, 595, 595, 595, 699, 699, 699, 801, 801, 801, 801, 801, 904, 904, 904, 904]
                    })
df_is_spell = pd.DataFrame({
                    'y1':[375, 480, 585, 688, 376, 480, 585, 688, 375, 480, 585, 688, 374, 480, 586, 688],
                    'y2':[382, 487, 592, 695, 383, 487, 592, 695, 382, 487, 592, 695, 381, 487, 593, 695],
                    'x1':[575, 575, 575, 575, 679, 679, 679, 679, 781, 781, 781, 781, 884, 884, 884, 884],
                    'x2':[595, 595, 595, 595, 699, 699, 699, 699, 801, 801, 801, 801, 904, 904, 904, 904]
})

# print(df_spell)
# spell_img = threshold_img[375:382, 560:580]
ind = 13
spell_img = threshold_img[df_is_spell['y1'][ind]:df_is_spell['y2'][ind], df_is_spell['x1'][ind]-15:df_is_spell['x2'][ind]-15]

spell = threshold_img[df_is_spell['y1'][ind]:df_is_spell['y2'][ind], df_is_spell['x1'][ind]:df_is_spell['x2'][ind]]
spell_img = cv2.resize(spell_img, None, fx=4.2, fy=4.2, interpolation=cv2.INTER_CUBIC)
spell = cv2.resize(spell, None, fx=4.2, fy=4.2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Pokaji1', spell_img)
cv2.imshow('Pokaji2', spell)
diff = cv2. absdiff(spell_img, spell)
print('Sledim', diff)
# spell_img2 = threshold_img[585:592, 575:595]
# diff = cv2.absdiff(spell_img, spell_img2)
# print('This is a diff', diff[0][0])
# if diff[0][0] < 10:
#     print('This is a spell!')
for ind in df_is_spell.index:
    print(ind)
    spell_img = threshold_img[df_is_spell['y1'][ind]:df_is_spell['y2'][ind], df_is_spell['x1'][ind]-15:df_is_spell['x2'][ind]-15]
    spell = threshold_img[df_is_spell['y1'][ind]:df_is_spell['y2'][ind], df_is_spell['x1'][ind]:df_is_spell['x2'][ind]]
    cv2.imshow('Spell pictures', spell)
    diff = cv2.absdiff(spell_img, spell)
    if diff[0][0] < 10:
        print('Spell is found!')
        
    # print(diff[0][0][0])
    print(df_spell['y1'][ind], df_spell['y2'][ind], df_spell['x1'][ind], df_spell['x2'][ind])

deck_list = [card_f1, card_f2, card_f3, card_f4, card_w1, card_w2, card_w3, card_w4, card_a1, card_a2, card_a3, card_a4, card_e1, card_e2, card_e3, card_e4]

custom_config = '--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'#'--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
#'--oem 3 --psm 6'#'--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789 %' 
#'--oem 3 --psm 6'#'--oem 3 --psm 6'
 #r'--oem 3 --psm 6'
card_f3 = cv2.resize(spell_e2, None, fx=4.2, fy=4.2, interpolation=cv2.INTER_CUBIC)
# card_f4 = cv2.resize(card_f4, None, fx=4.2, fy=4.2, interpolation=cv2.INTER_CUBIC)
details = pytesseract.image_to_data(card_f3, output_type=Output.DICT, config=custom_config, lang='eng')
print(details['text'])
cv2.imshow('captured text', card_f3)

for ind in df_is_spell.index:
    print(ind)
    spell_img = threshold_img[df_is_spell['y1'][ind]:df_is_spell['y2'][ind], df_is_spell['x1'][ind]-15:df_is_spell['x2'][ind]-15]
    spell = threshold_img[df_is_spell['y1'][ind]:df_is_spell['y2'][ind], df_is_spell['x1'][ind]:df_is_spell['x2'][ind]]
    diff = cv2.absdiff(spell_img, spell)
    if ind == 5:
        cv2.imshow('Spell Diff', spell)
    print('Differ', diff)
    if (diff[2][10] + diff[2][11]) < 12 and diff[3][10] + diff[3][11] + diff[3][12] + diff[2][13] < 20 and diff[3][13] < 20 and diff[4][13]< 30:#diff[4][14] + diff[2][10] < 20 or diff[3][10] < 10:
        print('PRINTIM', diff[2][10])
        deck_list[ind] = threshold_img[df_spell['y1'][ind]:df_spell['y2'][ind], df_spell['x1'][ind]:df_spell['x2'][ind]]
        print('Spell is found!')
        
        

for card in deck_list:
# Resize
    card = cv2.resize(card, None, fx=4.2, fy=4.2, interpolation=cv2.INTER_CUBIC)
    card_f2 = cv2.resize(deck_list[1], None, fx=4.2, fy=4.2, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('card f2', card_f2)
# Feeding image to tesseract
    details = pytesseract.image_to_data(card, output_type=Output.DICT, config=custom_config, lang='eng')
# print(range(details['text']))
# for i in range(details['text']):
# print(details['text'][4])

    try:
        if details['text'][4] == '111':
            details['text'][4] = 10
    except:
        pass
    # print(details['text'])
    total_boxes = len(details['text'])
    for sequence_number in range(total_boxes):
        if int(float(details['conf'][sequence_number])) > 30:
            (x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number], details['height'][sequence_number])
            card_img = cv2.rectangle(card, (x, y), (x+w, y+h), (0,255,0), 2)
    
    for word in details['text']:
        if word != '':
            number_list.append(word)
            print(number_list)
# Display image
# cv2.imshow('captured text', card_e3)
# Maintain output window until user presses a key
cv2.waitKey(0)
# Destroying present windows on screen
cv2.destroyAllWindows()