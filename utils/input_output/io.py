import numpy as np
import os

def save_np_arrays(images, img_names, save_path):
    for img, img_name in zip(images, img_names):
        np.save(f'{save_path}/{img_name}', img)
        
def load_np_arrays(path, num=None):
    images = []
    img_names = sorted(os.listdir(path))
    
    if num is None:
        num = len(img_names)
    
    for idx in range(num):
        img_name = img_names[idx]
        img = np.load(f'{path}/{img_name}')
        images.append(img)
    
    return np.array(images)