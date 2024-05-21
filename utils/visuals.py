import cv2
import numpy as np
from pathlib import Path
import os

def save_results(root, images, results, titles):
    os.makedirs(root, exist_ok=True)

    for i, (image, result, title) in enumerate(zip(images, results, titles)):
        ans = np.concatenate((image, result), axis=1)
        cv2.imwrite(str(Path(root) / title), ans)