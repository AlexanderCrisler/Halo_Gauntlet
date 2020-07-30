from PIL import Image, ImageGrab, ImageOps
import pytesseract

while True:
    image = ImageGrab.grab(bbox=(860, 135, 1060, 170))
    image = ImageOps.grayscale(image)
    #image.save("sc.png")
    text = pytesseract.image_to_string(image)

    print(text)