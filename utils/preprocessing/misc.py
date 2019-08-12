import numpy as np
import skimage


def gaussian_smoothing(gt_dots, sigma):
    gt_density_maps = np.zeros((len(gt_dots), *gt_dots[0].shape), dtype=np.float64)
    
    for i in range(len(gt_dots)):
        gt_density_maps[i] = skimage.filters.gaussian(gt_dots[i],
                                                      sigma=sigma,
                                                      mode='reflect')
    
    return gt_density_maps


def count_map_from_dots_img(dots_img, receptive_field=32):
    num_rows, num_cols = dots_img.shape[:2]
    count_map = np.zeros((num_rows + receptive_field, num_cols + receptive_field),
                         dtype=np.float32)

    for i in range(num_rows + receptive_field):
        for j in range(num_cols + receptive_field):
            row1, col1 = max(0, i - receptive_field), max(0, j - receptive_field) 
            row2, col2 = min(num_rows, i), min(num_cols, j)
            count_map[i, j] = dots_img[row1:row2, col1:col2].sum()
        
    return count_map


def get_knn_dist(current_coords, label_coords):
    # k = 1
    x, y = current_coords
    dist = np.sqrt((label_coords[:, 0] - x) ** 2
                   + 
                   (label_coords[:, 1] - y) ** 2)
    return dist.min()


def full_knn_map_from_dots_img(dots_img):
    label_coords = np.argwhere(dots_img == 1)
    
    num_rows, num_cols = dots_img.shape[:2]
    knn_map = np.zeros((num_rows, num_cols), dtype=np.float32)
    
    for i in range(num_rows):
        for j in range(num_cols):
            knn_map[i, j] = get_knn_dist((i, j), label_coords)
        
    return knn_map


def iknn_map_from_dots_img(dots_img):
    return 1. / (full_knn_map_from_dots_img(dots_img) + 1.)