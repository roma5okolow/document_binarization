from models import otsu_threshold, niblack_threshold, modified_otsu_threshold, postnikov_threshold, my_otsu_threshold
from utils import load_grayscale_images, save_results
from pathlib import Path

IMG_ROOT = Path('binarization_dataset/Задача 1 -- бинаризация')
RES_ROOT = Path('results')

images = load_grayscale_images(IMG_ROOT)

results_otsu = [otsu_threshold(img) for img in images]
results_mod_otsu = [modified_otsu_threshold(img) for img in images]
results_niblack = [niblack_threshold(img) for img in images]
results_postnikov = [postnikov_threshold(img) for img in images]
results_my_otsu = [my_otsu_threshold(img) for img in images]




save_results(RES_ROOT / "otsu", images, results_otsu, [f'Otsu{i}.png' for i in range(len(images))])
save_results(RES_ROOT / "mod_otsu", images, results_mod_otsu, [f'Mod_otsu{i}.png' for i in range(len(images))])
save_results(RES_ROOT / "niblack", images, results_niblack, [f'Niblack{i}.png' for i in range(len(images))])
save_results(RES_ROOT / "postnikov", images, results_postnikov, [f'Postnikov{i}.png' for i in range(len(images))])
save_results(RES_ROOT / "my_otsu", images, results_my_otsu, [f'my_otsu{i}.png' for i in range(len(images))])
