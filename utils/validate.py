import os
import cv2

# Функция для проверки числа каналов изображения и предотвращения обработки полноцветных изображений
def load_grayscale_images(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
            if img is not None:
                images.append(img)
    return images