import cv2 as cv
import easyocr
import re


# gets gold amount
def get_gold_and_gems():
    reader = easyocr.Reader(['en'], verbose=False)
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
    # pixel start of resource amount
    resource_x_start = 980
    resource_x_end = 1296
    resource_y_start = 18
    resource_y_end = 65

    img = cv.imread("screenshots/screen.png")
    crop_img = img[resource_y_start:resource_y_end, resource_x_start:resource_x_end]
    cv.imwrite("screenshots/resources.png", crop_img)
    return crop_img
