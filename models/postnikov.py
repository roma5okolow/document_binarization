import cv2
import numpy as np

def postnikov_threshold(image, k=-0.2, initial_window_size=15, sigma0=10):
    def compute_threshold(image, window_size):
        mean = cv2.boxFilter(image, cv2.CV_32F, (window_size, window_size))
        sqmean = cv2.sqrBoxFilter(image, cv2.CV_32F, (window_size, window_size))
        variance = sqmean - mean ** 2
        stddev = np.sqrt(variance)
        return mean + k * stddev

    window_size = initial_window_size
    while window_size < image.shape[0]:
        threshold = compute_threshold(image, window_size)
        binary = image > threshold
        stddev = np.std(threshold)
        if stddev >= sigma0:
            return (binary * 255).astype(np.uint8)
        window_size *= 2

    # Если не удалось принять решение, возвращаем пустое изображение
    return np.zeros_like(image)
