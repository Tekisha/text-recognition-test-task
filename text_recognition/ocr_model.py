import os
from pathlib import Path

from pytesseract import pytesseract
import cv2
from langdetect import detect
from easyocr import Reader


class OCRModel:
    def __init__(self, languages=None):
        pytesseract.tesseract_cmd = '../tesseract/tesseract.exe'
        os.environ['TESSDATA_PREFIX'] = '../tesseract/tessdata'
        if languages is None:
            languages = ['en', 'ch_sim']
        self.reader = Reader(languages, gpu=True)

    def image_first_scan(self, image: Path) -> str:
        try:
            result = ' '.join(self.reader.readtext(str(image), detail=0))
            if not result:
                return "No text found in the image."
            return str(result)
        except Exception as e:
            print(f"Error processing image {image}: {e}")
            return "An error occurred during text recognition."


    def recognize_text(self, image: Path) -> str:
        """
        This method takes an image file as input and returns the recognized text from the image.

        :param image: The path to the image file.
        :return: The recognized text from the image.
        """
        first_scan_text = self.image_first_scan(image)
        detected_lang = self.detect_language(first_scan_text)
        # Read the image using OpenCV
        image = cv2.imread(str(image))

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(gray_image, lang=detected_lang)

        return text.strip()

    def detect_language(self, text: str) -> str:
        try:
            language = detect(text)

            lang_mapping = {
                'en': 'eng',
                'zh-cn': 'chi_sim',
                # Add more mappings as needed
            }

            return lang_mapping.get(language)
        except:
            return "en"


if __name__ == "__main__":
    model = OCRModel()
    for i in range(1, 13, 1):
        print("\n")
        print(model.recognize_text(Path('..\\data\\public_data\\' + str(i) + '.png')))
