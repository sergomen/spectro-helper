#------------------THERE WE WILL USE OPENCV & PYTESSERACT--------------
import cv2
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"
# Reading image using opencv
image = cv2.imread('01.jpg')
# Converting image into gray scale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Converting it to binary image by Thresholding
threshold_img = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# Configuring parameters for tesseract
# threshold_img = 255 - cv2.GaussianBlur(threshold_img, (5,5), 0)
# Get part of image
# card_img = threshold_img[300:800, 500:1200]
card_f1 = threshold_img[353:364, 580:592] #y, x
card_f2 = threshold_img[456:466, 575:594]
card_f3 = threshold_img[561:584, 576:594]
card_f4 = threshold_img[664:677, 577:594]

card_w1 = threshold_img[360:373, 685:694] # circle
card_w2 = threshold_img[456:469, 682:699] # square
card_w3 = threshold_img[561:572, 686:699] # square
card_w4 = threshold_img[665:677, 682:699] # square

card_a1 = threshold_img[354:364, 788:801] # square
card_a2 = threshold_img[454:468, 788:801] # square
card_a3 = threshold_img[569:581, 788:798] # circle
card_a4 = threshold_img[674:684, 787:801] # circle

card_e1 = threshold_img[354:377, 890:903] # circle
card_e2 = threshold_img[465:478, 892:903] # circle
card_e3 = threshold_img[559:573, 890:903] # square
card_e4 = threshold_img[665:677, 890:907] # square

deck_list = [card_f1, card_f2, card_f3, card_f4, card_w1, card_w2, card_w3, card_w4, card_a1, card_a2, card_a3, card_a4, card_e1, card_e2, card_e3, card_e4]
custom_config = '--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'
#'--oem 3 --psm 6'#'--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789 %' 
#'--oem 3 --psm 6'#'--oem 3 --psm 6'
 #r'--oem 3 --psm 6'
for card in deck_list:
# Resize
    card = cv2.resize(card, None, fx=4.2, fy=4.2, interpolation=cv2.INTER_CUBIC)

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
    print(details['text'])
    total_boxes = len(details['text'])
    for sequence_number in range(total_boxes):
        if int(float(details['conf'][sequence_number])) > 30:
            (x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number], details['height'][sequence_number])
            card_img = cv2.rectangle(card, (x, y), (x+w, y+h), (0,255,0), 2)

# Display image
cv2.imshow('captured text', card_e3)
# Maintain output window until user presses a key
cv2.waitKey(0)
# Destroying present windows on screen
cv2.destroyAllWindows()