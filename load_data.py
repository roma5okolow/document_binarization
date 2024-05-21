import os
import cv2
import zipfile
import requests
from io import BytesIO
i

# URL набора данных
url = 'https://vis.iitp.ru/binarization_dataset.zip'

# Загрузка и распаковка набора данных
response = requests.get(url)
with zipfile.ZipFile(BytesIO(response.content)) as z:
    z.extractall('binarization_dataset')

# Функция для проверки числа каналов изображения и предотвращения обработки полноцветных изображений
def load_grayscale_images(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
            if img is not None:
                images.append(img)
    return images

# Загрузка изображений
images = load_grayscale_images('binarization_dataset')
