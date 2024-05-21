import cv2
import numpy as np

def postnikov_threshold(image, k=-1, a = 0, initial_window_size=40, sigma0=20):
    def niblack_threshold(image, k=-1, a=0, window_size=40):
        mean = cv2.boxFilter(image, cv2.CV_32F, (window_size, window_size), normalize=True)
        sqmean = cv2.sqrBoxFilter(image, cv2.CV_32F, (window_size, window_size), normalize=True)
        variance = sqmean - mean ** 2
        stddev = np.sqrt(variance)
        threshold = mean + k * stddev + a
        return threshold

    window_size = initial_window_size
    while window_size < image.shape[0] and window_size < image.shape[1]:
        threshold = niblack_threshold(image, k, a, window_size)
        binary = image > threshold
        stddev = np.std(threshold)
        print(stddev)
        print(f"{window_size=}")
        if stddev >= sigma0:
            print(f"finished")
            return (binary * 255).astype(np.uint8)
        window_size *= 2

    # Если не удалось принять решение, возвращаем пустое изображение
    return np.zeros_like(image)
