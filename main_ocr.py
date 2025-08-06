import os
print("Current Directory:", os.getcwd())
print("Files in src:", os.listdir('src'))


import argparse
import os
from src.ocr_engine import image_to_text
from src.utils import get_image_files


def main():
    parser = argparse.ArgumentParser(description="Handwritten OCR Tool")
    parser.add_argument('--input', type=str, required=True,
                        help='Path to image file or folder.')
    parser.add_argument('--show-steps', action='store_true',
                        help="Show image preprocessing steps visually.")
    args = parser.parse_args()
    input_path = args.input
    show_steps = args.show_steps
    if os.path.isdir(input_path):
        images = get_image_files(input_path)
        for img in images:
            print(f"\n=== Text from {img} ===\n")
            print(image_to_text(img, show_steps=show_steps))
    else:
        print(f"\n=== Text from {input_path} ===\n")
        print(image_to_text(input_path, show_steps=show_steps))

if __name__ == "__main__":
    main()
