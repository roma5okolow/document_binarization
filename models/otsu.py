import cv2

def otsu_threshold(image):
    # Применение метода Оцу
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    _, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary