import cv2 as cv
import pytesseract
import re

# pixel start of resource amount
RESOURCE_X_START = 980
RESOURCE_X_END = 1296
RESOURCE_Y_START = 18
RESOURCE_Y_END = 65

# gets gold amount
def get_gold_and_gems():
    image = crop_resources_from_screenshot()
    text = pytesseract.image_to_string(image)
    text = text.split()
    gold = text[1].replace(',','')
    gems = text[3].replace(',','')
    return gold, gems

# crops image
def crop_resources_from_screenshot():
    img = cv.imread("screenshots/screen.png")
    crop_img = img[RESOURCE_Y_START:RESOURCE_Y_END, RESOURCE_X_START:RESOURCE_X_END]
    # cv.imwrite("screenshots/resources.png", crop_img)
    return crop_img
