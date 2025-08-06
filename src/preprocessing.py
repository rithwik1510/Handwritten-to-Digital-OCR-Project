import cv2
import numpy as np

def preprocess_image(img_path, show_steps=False):
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {img_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # A gentle blur to remove noise before thresholding
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Binarization with Otsu's thresholding
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    if show_steps:
        cv2.imshow("Original", img)
        cv2.imshow("Grayscale", gray)
        cv2.imshow("Blurred", blurred)
        cv2.imshow("Binarized", binary)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return binary

if __name__ == '__main__':
    import sys
    preprocess_image(sys.argv[1], show_steps=True)
