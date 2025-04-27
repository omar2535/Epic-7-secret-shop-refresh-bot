import cv2 as cv
import easyocr
import re

# Initialize EasyOCR Reader (English only, adjust languages if needed)
reader = easyocr.Reader(['en'], gpu=False)

# pixel start of resource amount
RESOURCE_X_START = 980
RESOURCE_X_END = 1296
RESOURCE_Y_START = 18
RESOURCE_Y_END = 65


# gets gold amount
def get_gold_and_gems():
    image = crop_resources_from_screenshot()

    # EasyOCR expects filepath or image array
    results = reader.readtext(image, detail=0)  # detail=0 to get only the text

    if len(results) < 2:
        # In case OCR only found one item or failed
        gold, gems = '', ''
    else:
        gold = re.sub('[^0-9]', '', str(results[0]))
        gems = re.sub('[^0-9]', '', str(results[1]))

    return gold, gems


# crops image
def crop_resources_from_screenshot():
    img = cv.imread("screenshots/screen.png")
    crop_img = img[RESOURCE_Y_START:RESOURCE_Y_END, RESOURCE_X_START:RESOURCE_X_END]
    cv.imwrite("screenshots/resources.png", crop_img)
    return crop_img
