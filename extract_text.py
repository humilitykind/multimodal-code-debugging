import cv2
import pytesseract

def preprocess_image(image_path):
    try:
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        return thresh
    except Exception as e:
        print(f"Error in preprocessing image: {e}")
        return None

def extract_text(image_path):
    try:
        preprocessed_image = preprocess_image(image_path)
        if preprocessed_image is not None:
            text = pytesseract.image_to_string(preprocessed_image)
            return text
        else:
            return ""
    except Exception as e:
        print(f"Error in extracting text: {e}")
        return ""
