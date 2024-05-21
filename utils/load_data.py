import zipfile
import requests
from io import BytesIO

# URL набора данных
url = 'https://vis.iitp.ru/binarization_dataset.zip'

# Загрузка и распаковка набора данных
response = requests.get(url)
with zipfile.ZipFile(BytesIO(response.content)) as z:
    z.extractall('binarization_dataset')