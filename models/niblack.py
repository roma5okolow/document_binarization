import cv2
import numpy as np

def niblack_threshold(image, k=-1, a=0, window_size=40):
    mean = cv2.boxFilter(image, cv2.CV_32F, (window_size, window_size), normalize=True)
    sqmean = cv2.sqrBoxFilter(image, cv2.CV_32F, (window_size, window_size), normalize=True)
    variance = sqmean - mean ** 2
    stddev = np.sqrt(variance)
    threshold = mean + k * stddev + a
    binary = image > threshold
    return (binary * 255).astype(np.uint8)
