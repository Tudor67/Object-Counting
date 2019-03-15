from utils.input_output.io import save_np_arrays
from utils.preprocessing.misc import gaussian_smoothing

def create_and_save_density_maps(dots_images, sigma, img_names, save_path):
    for idx, img_name in enumerate(img_names):
        density_maps = gaussian_smoothing([dots_images[idx]], sigma=sigma)
        save_np_arrays(density_maps, [img_names[idx].split('.')[0]], save_path)