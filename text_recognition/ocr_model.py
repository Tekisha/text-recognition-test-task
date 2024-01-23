import os
from pathlib import Path
from pytesseract import pytesseract
import cv2


class OCRModel:
    def __init__(self, languages=None):
        pytesseract.tesseract_cmd = '../tesseract/tesseract.exe'
        os.environ['TESSDATA_PREFIX'] = '../tesseract/tessdata'
        if languages is None:
            self.languages = "eng+chi_sim"

    def preprocess_image(self, image):
        """
        Apply advanced preprocessing to the image to improve OCR accuracy.
        """
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return gray

    def recognize_text(self, image: Path) -> str:
        """
        This method takes an image file as input and returns the recognized text from the image.

        :param image: The path to the image file.
        :return: The recognized text from the image.
        """
        image = cv2.imread(str(image))

        preprocessed_image = self.preprocess_image(image)

        text = pytesseract.image_to_string(preprocessed_image, lang=self.languages, config='--oem 1 --psm 6 -c preserve_interword_spaces=1')

        return text.strip()


if __name__ == "__main__":
    model = OCRModel()
    for i in range(1, 13, 1):
        print("\n")
        print(model.recognize_text(Path('..\\data\\public_data\\' + str(i) + '.png')))
