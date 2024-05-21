import cv2
import numpy as np

def niblack_threshold(image, k=-0.2, window_size=15):
    mean = cv2.boxFilter(image, cv2.CV_32F, (window_size, window_size))
    sqmean = cv2.sqrBoxFilter(image, cv2.CV_32F, (window_size, window_size))
    variance = sqmean - mean ** 2
    stddev = np.sqrt(variance)
    threshold = mean + k * stddev
    binary = image > threshold
    return (binary * 255).astype(np.uint8)
