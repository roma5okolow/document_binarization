import cv2
import numpy as np
import matplotlib.pyplot as plt

def otsu_threshold(image):
    thr, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary

def my_otsu_threshold(image):
    sigma_best = 0
    freqs, _ = np.histogram(image, bins=range(256), density=True)
    first_nonzero = 0
    
    if np.any(np.isclose(freqs, 1, rtol=1e-9)):
        return image > 0

    while np.isclose(freqs[first_nonzero], 0, rtol=1e-9):
        first_nonzero += 1
    last_nonzero = len(freqs) - 1
    while np.isclose(freqs[last_nonzero], 0, rtol=1e-9):
        last_nonzero -= 1
        
    for k in range(first_nonzero, min(254, last_nonzero)):
        omega_0 = freqs[:(k + 1)].sum()
        omega_1 = 1 - omega_0
        mu_0 = (np.arange(0, k + 1) * freqs[:(k + 1)]).sum() / omega_0
        mu_1 = (np.arange(k+1, len(freqs)) * freqs[k+1:]).sum() / omega_1
        sigma = omega_0 * omega_1 * (mu_0 - mu_1) ** 2
        if sigma >= sigma_best:
            sigma_best = sigma
            k_opt = k
    _, binary = cv2.threshold(image, k_opt, 255, cv2.THRESH_BINARY)
    return binary