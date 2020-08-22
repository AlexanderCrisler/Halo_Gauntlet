import re
import statistics
import serial
import time

# Python Imaging Library
from PIL import Image, ImageGrab, ImageFilter, ImageOps
# Optical Character Recognition
import pytesseract


def check_death_scope():
    """Checking for the death of player or if the player is scoped in."""
    # Grabbing image of region where "Respawn in #" is displayed
    image = ImageOps.grayscale(ImageGrab.grab(bbox=(860, 135, 1060, 170)))
    text = pytesseract.image_to_string(image)
    respawn = "Respawn"

    # Checking for the word respawn in the image
    if respawn in text:
        print(f"Dead: {text}", end=": ")

        try:
            # Numbers aren't always recognized by pytesseract resulting in try block
            res = int(re.search(r'\d+', text).group())
            if res <= 10:
                time.sleep(res + 1)
        except:
            print("no number in text.")

        return

    else:
        print("Scoped in or Health 1 depleted.")
        return


ser = serial.Serial('COM3', 9600)

while True:
    # Pixels of healthbar used in image for health detection
    x1 = 786
    y1 = 125
    x2 = 1130
    y2 = 126

    # Grabbing a single line on x axis of the health bar and converting to RGB values
    image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    colors = image.getdata()

    # Extracting and seperating all blue values into the list of lists, blues
    blues = [[], [], [], [], []]
    i = x1
    for color in colors:
        if i < 855:
            blues[0].append(color[2])
        elif i >= 855 and i < 924:
            blues[1].append(color[2])
        elif i >= 924 and i < 993:
            blues[2].append(color[2])
        elif i >= 993 and i < 1062:
            blues[3].append(color[2])
        elif i >= 1062 and i < x2:
            blues[4].append(color[2])
        i += 1

    # Taking the mode of each of the 5 sections of the blues
    bluemode = []
    for i in range(0, len(blues)):
            bluemode.append(int(statistics.mode(blues[i])))

    # Checking each section for a blue majority and printing results
    if bluemode[0] < 155:
        check_death_scope()
    elif bluemode[1] < 155:
        print("health 2 depeleted!")
        ser.write(2)
    elif bluemode[2] < 155:
        print("health 3 depeleted!")
        ser.write(3)
    elif bluemode[3] < 155:
        print("health 4 depeleted!")
        ser.write(4)
    elif bluemode[4] < 155:
        print("health 5 depeleted!")
        ser.write(5)

    #TODO: Near Death Function

    #TODO: Signals to Arduino via serial

ser.close()