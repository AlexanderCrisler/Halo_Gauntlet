from PIL import Image, ImageGrab, ImageFilter, ImageOps
import pytesseract
import statistics
import re
import time

def check_death_scope():
    image = ImageOps.grayscale(ImageGrab.grab(bbox=(860, 135, 1060, 170)))
    text = pytesseract.image_to_string(image)
    respawn = "Respawn"

    if respawn in text:
        print(f"Dead: {text}", end=": ")
        try:
            res = int(re.search(r'\d+', text).group())
            if res <= 10:
                time.sleep(res + 1)
        except:
            print("no number in text.")
        return
    else:
        print("Scoped in or Health 1 depleted.")
        return

while True:
    image = ImageGrab.grab(bbox=(786, 125, 1130, 126))
    colors = image.getdata()
    blues = [[], [], [], [], []]
    i = 786
    for color in colors:
        if i < 855:
            blues[0].append(color[2])
        elif i >= 855 and i < 924:
            blues[1].append(color[2])
        elif i >= 924 and i < 993:
            blues[2].append(color[2])
        elif i >= 993 and i < 1062:
            blues[3].append(color[2])
        elif i >= 1062 and i < 1130:
            blues[4].append(color[2])
        i += 1

    bluemode = []
    for i in range(0, len(blues)):
            bluemode.append(int(statistics.mode(blues[i])))

    if bluemode[0] < 155:
        check_death_scope()
    elif bluemode[1] < 155:
        print("health 2 depeleted!")
    elif bluemode[2] < 155:
        print("health 3 depeleted!")
    elif bluemode[3] < 155:
        print("health 4 depeleted!")
    elif bluemode[4] < 155:
        print("health 5 depeleted!")

    #TODO: Near Death Function

    #TODO: Signals to Arduino via serial