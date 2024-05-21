# Document binarization

In this repo you can find 4 implemented methods for document binarization:
* Otsu (cv2)
* Otsu (my implementation)
* Unbalanced Otsu
* Niblack
* Postnikov (modified niblack)

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
```bash
python3 main.py
```

