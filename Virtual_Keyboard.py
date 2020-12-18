import cv2
import numpy as np

keyboard = np.zeros((600, 1000, 3), np.uint8)

keys_set_1 = {0: "Q", 1: "W", 2: "E", 3: "R", 4: "T",
              5: "Y", 6: "U", 7: "I", 8: "O", 9: "P",
              10: "A", 11: "S", 12: "D", 13: "F", 14: "G", 15: "H", 16: "J", 17: "K", 18: "L", 19: "<-",
              20: "Z", 21: "X", 22: "C", 23: "V", 24: "B", 25: "N", 26: "M", 27: ",", 28: ".", 29: "'"}


def letter(letter_index, text, letter_light):
    # Keys
    if letter_index == 0:
        x = 0
        y = 0
    elif letter_index == 1:
        x = 100
        y = 0
    elif letter_index == 2:
        x = 200
        y = 0
    elif letter_index == 3:
        x = 300
        y = 0
    elif letter_index == 4:
        x = 400
        y = 0
    elif letter_index == 5:
        x = 500
        y = 0
    elif letter_index == 6:
        x = 600
        y = 0
    elif letter_index == 7:
        x = 700
        y = 0
    elif letter_index == 8:
        x = 800
        y = 0
    elif letter_index == 9:
        x = 900
        y = 0
    elif letter_index == 10:
        x = 0
        y = 200
    elif letter_index == 11:
        x = 100
        y = 200
    elif letter_index == 12:
        x = 200
        y = 200
    elif letter_index == 13:
        x = 300
        y = 200
    elif letter_index == 14:
        x = 400
        y = 200
    elif letter_index == 15:
        x = 500
        y = 200
    elif letter_index == 16:
        x = 600
        y = 200
    elif letter_index == 17:
        x = 700
        y = 200
    elif letter_index == 18:
        x = 800
        y = 200
    elif letter_index == 19:
        x = 900
        y = 200
    elif letter_index == 20:
        x = 0
        y = 400
    elif letter_index == 21:
        x = 100
        y = 400
    elif letter_index == 22:
        x = 200
        y = 400
    elif letter_index == 23:
        x = 300
        y = 400
    elif letter_index == 24:
        x = 400
        y = 400
    elif letter_index == 25:
        x = 500
        y = 400
    elif letter_index == 26:
        x = 600
        y = 400
    elif letter_index == 27:
        x = 700
        y = 400
    elif letter_index == 28:
        x = 800
        y = 400
    elif letter_index == 29:
        x = 900
        y = 400

    width = 100
    heigth = 200
    thickness = 3
    if letter_light is True:
        cv2.rectangle(keyboard, (x + thickness, y + thickness), (x + width - thickness, y + heigth - thickness),
                  (255, 255, 255), -1)
    else:
        cv2.rectangle(keyboard, (x + thickness, y + thickness), (x + width - thickness, y + heigth - thickness),
                      (255, 0, 0), thickness)

    # Text Settings
    font_letter = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 5
    font_th = 4
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
    width_text, height_text = text_size[0], text_size[1]
    text_x = int((width - width_text) / 2) + x
    text_y = int((heigth + height_text) / 2) + y
    cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (255, 0, 0), font_th)


for i in range(29):
    if i == 5:
        light = True
    else:
        light = False
    letter(i, keys_set_1[i], light)


cv2.imshow("Keyboard", keyboard)

cv2.waitKey(0)
cv2.destroyAllWindows()
