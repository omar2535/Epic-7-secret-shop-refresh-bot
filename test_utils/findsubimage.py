import argparse
import cv2 as cv
from matplotlib import pyplot as plt
import os


def match_template(source_path, template_path):
    # Load images
    img = cv.imread(source_path, 0)
    if img is None:
        raise ValueError(f"Could not load source image from {source_path}")

    img2 = img.copy()
    template = cv.imread(template_path, 0)
    if template is None:
        raise ValueError(f"Could not load template image from {template_path}")

    w, h = template.shape[::-1]

    methods = [
        "cv.TM_CCOEFF",
        "cv.TM_CCOEFF_NORMED",
        "cv.TM_CCORR",
        "cv.TM_CCORR_NORMED",
        "cv.TM_SQDIFF",
        "cv.TM_SQDIFF_NORMED",
    ]

    plt.figure(figsize=(12, 8))
    for idx, meth in enumerate(methods):
        img = img2.copy()
        method = eval(meth)
        res = cv.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(img, top_left, bottom_right, 255, 2)

        plt.subplot(2, len(methods), idx + 1)
        plt.imshow(res, cmap="gray")
        plt.title(f"{meth}\nMatching Result")

        plt.subplot(2, len(methods), idx + 1 + len(methods))
        plt.imshow(img, cmap="gray")
        plt.title(f"{meth}\nDetected Point")

    plt.tight_layout()
    plt.show()


# Sample usage: python findsubimage.py --source screenshots/screen.png --template matches/helmet.png
def main():
    parser = argparse.ArgumentParser(description="Template Matching CLI Tool")
    parser.add_argument("--source", required=True, help="Path to the source image")
    parser.add_argument("--template", required=True, help="Path to the template image")
    args = parser.parse_args()

    match_template(args.source, args.template)


if __name__ == "__main__":
    main()
