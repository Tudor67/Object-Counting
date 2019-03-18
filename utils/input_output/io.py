import json
import numpy as np
import os
import skimage

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

def load_images(path, img_names, num_images=None):
    images = []
    if num_images is None:
        num_images = len(img_names)

    for idx in range(num_images):
        img_name = img_names[idx]
        img_path = f'{path}/{img_name}'
        img = skimage.io.imread(img_path) / 255.
        images.append(img)
    
    return images

def load_images_and_density_maps(path, num_images):
    img_names = sorted(os.listdir(f'{path}/images'))[:num_images]
    density_map_names = sorted(os.listdir(f'{path}/gt_density_maps'))[:num_images]

    images = []
    density_maps = []

    for img_name, density_map_name in zip(img_names, density_map_names):
        img = skimage.io.imread(f'{path}/images/{img_name}') / 255.
        density_map = np.load(f'{path}/gt_density_maps/{density_map_name}')

        images.append(img)
        density_maps.append(density_map)
    
    return images, density_maps

def read_json(filename):
    with open(filename, 'r') as fi:
        data = json.load(fi)
    return data

def write_json(data, filename):
    dirname = os.path.dirname(filename)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
        
    with open(filename, 'w') as fo:
        json.dump(data, fo)