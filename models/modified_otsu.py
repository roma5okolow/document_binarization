import cv2
import numpy as np

def modified_otsu_threshold(image):
    Q_best = float('-inf')
    freqs, _ = np.histogram(image, bins=range(256), density=True)
    first_nonzero = 0

    while np.isclose(freqs[first_nonzero], 0, rtol=1e-9):
        first_nonzero += 1
    last_nonzero = len(freqs) - 1
    while np.isclose(freqs[last_nonzero], 0, rtol=1e-9):
        last_nonzero -= 1
        
    for k in range(first_nonzero, min(254, last_nonzero)):
        omega_0 = freqs[:(k + 1)].sum()
        omega_1 = 1 - omega_0
        mu_0 = (np.arange(0, k + 1) * freqs[:(k + 1)]).sum() / omega_0
        mu_0_2 = ((np.arange(0, k + 1)**2) * freqs[:(k + 1)]).sum() / omega_0
        mu_1 = (np.arange(k+1, len(freqs)) * freqs[k+1:]).sum() / omega_1
        mu_1_2 = ((np.arange(k+1, len(freqs))**2) * freqs[k+1:]).sum() / omega_1
        sigma = omega_0 * (mu_0_2 - mu_0**2)+ omega_1 * (mu_1_2 - mu_1**2)
        Q = omega_0 * np.log(omega_0) + omega_1 * np.log(omega_1) - np.log(sigma)
        if Q >= Q_best:
            Q_best = Q
            k_opt = k
    _, binary = cv2.threshold(image, k_opt, 255, cv2.THRESH_BINARY)
    return binary
