import cv2
import numpy as np

def preprocess_image(img_path, show_steps=False):
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {img_path}")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    binary = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 15, 8
    )
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
