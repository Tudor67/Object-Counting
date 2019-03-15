import numpy as np
import skimage


def gaussian_smoothing(gt_dots, sigma):
    gt_density_maps = np.zeros((len(gt_dots), *gt_dots[0].shape))
    
    for i in range(len(gt_dots)):
        gt_density_maps[i] = skimage.filters.gaussian(gt_dots[i],
                                                      sigma=sigma,
                                                      mode='reflect')
    
    return gt_density_maps