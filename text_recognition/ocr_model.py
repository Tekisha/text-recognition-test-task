from pathlib import Path

from pytesseract import pytesseract
import cv2


class OCRModel:
    def __init__(self):
        pytesseract.tesseract_cmd = '..\\tesseract\\tesseract.exe'
    def recognize_text(self, image: Path) -> str:
        """
        This method takes an image file as input and returns the recognized text from the image.

        :param image: The path to the image file.
        :return: The recognized text from the image.
        """
        # Read the image using OpenCV
        image = cv2.imread(str(image))

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Use pytesseract to extract text from the image
        text = pytesseract.image_to_string(gray_image)

        return text.strip()
        #return 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


if __name__=="__main__":
    model = OCRModel()
    for i in range(1,13,1):
        print(model.recognize_text(Path('..\\data\\public_data\\'+str(i)+'.png')))
