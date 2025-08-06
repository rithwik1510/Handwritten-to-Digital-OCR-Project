import pytesseract
from .preprocessing import preprocess_image
from spellchecker import SpellChecker

# Update this path to your Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(img_path, show_steps=False):
    processed_img = preprocess_image(img_path, show_steps)
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(processed_img, lang='eng', config=custom_config)

    # Post-processing with a spell checker
    spell = SpellChecker()
    words = text.split()
    corrected_words = [spell.correction(word) for word in words]
    corrected_text = " ".join(corrected_words)

    return corrected_text

