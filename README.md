# Document binarization

In this repo you can find 5 implemented methods for document binarization:
* **Otsu (cv2)** (Otsu N. A threshold selection method from gray-level his-
tograms // IEEE transactions on systems, man, and cybernet-
ics. — 1979. — Vol. 9, no. 1. — P. 62–66.)
* **Otsu (my implementation)**
* **Unbalanced Otsu** (Kurita T., Otsu N., Abdelmalek N. Maximum likelihood thresh-
olding based on population mixture models // Pattern recogni-
tion. — 1992. — Vol. 25, no. 10. — P. 1231–1240.)
* **Niblack** (Niblack W. An Introduction to Digital Image Processing. —
Prentice Hall, 1986. — P. 115–116.)
* **Postnikov** (modified niblack with variable window size) (not published)

## Installation

```bash
git clone https://github.com/roma5okolow/document_binarization.git
cd document_binarization
pip isntall -r requirements
```

## Usage

main.py
```python3

IMG_ROOT = Path(path/to/your/grayscale/documents)
RES_ROOT = Path(save/dir)
```
If you want, you can download test images (https://vis.iitp.ru/binarization_dataset.zi) via
```bash
python3 utils/load_data.py
```
To start binarizing images from IMG_ROOT, run
```bash
python3 main.py
```

Note, that this programm works only with grayscale images and skips color images
