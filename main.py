import matplotlib.pyplot as plt
import numpy as np
from models import otsu_threshold, niblack_threshold, modified_otsu_threshold, postnikov_threshold

def display_results(images, results, titles):
    plt.figure(figsize=(12, 8))
    for i, (image, result, title) in enumerate(zip(images, results, titles)):
        plt.subplot(2, len(images), i + 1)
        plt.imshow(image, cmap='gray')
        plt.title(f'Original {i+1}')
        plt.axis('off')

        plt.subplot(2, len(images), i + 1 + len(images))
        plt.imshow(result, cmap='gray')
        plt.title(title)
        plt.axis('off')
    plt.show()

results_otsu = [otsu_threshold(img) for img in images]
results_mod_otsu = [modified_otsu_threshold(img) for img in images]
results_niblack = [niblack_threshold(img) for img in images]
results_postnikov = [postnikov_threshold(img) for img in images]

display_results(images, results_otsu, ['Otsu' for _ in images])
display_results(images, results_mod_otsu, ['Mod. Otsu' for _ in images])
display_results(images, results_niblack, ['Niblack' for _ in images])
display_results(images, results_postnikov, ['Postnikov' for _ in images])
