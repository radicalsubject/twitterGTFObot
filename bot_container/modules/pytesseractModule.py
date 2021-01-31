try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def read_image(path):
    # If you don't have tesseract executable in your PATH, include the following:
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
    # Simple image to string
    text = pytesseract.image_to_string(Image.open(path))
    # print(text)
    return text