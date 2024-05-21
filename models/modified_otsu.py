import cv2
import numpy as np

def modified_otsu_threshold(image, w0=0.5, w1=0.5):
    # Гистограмма изображения
    hist = cv2.calcHist([image], [0], None, [256], [0, 256]).flatten()
    total = image.size
    current_max, threshold = 0, 0
    sumB, wB, sum1 = 0, 0, np.dot(np.arange(256), hist)

    for i in range(256):
        wB += hist[i]
        if wB == 0:
            continue
        wF = total - wB
        if wF == 0:
            break
        sumB += i * hist[i]
        mB = sumB / wB
        mF = (sum1 - sumB) / wF
        between_var = w0 * wB * wF * (mB - mF) ** 2
        if between_var > current_max:
            current_max = between_var
            threshold = i
    _, binary = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return binary
