import albumentations as A
import numpy as np
import os
import random
import shutil
import skimage.io

def hflip(image, mask):
    aug_list = [[image, mask]]
    
    augmented = A.HorizontalFlip(p=1)(image=image, mask=mask)
    image_hf, mask_hf = augmented['image'], augmented['mask']
    aug_list.append([image_hf, mask_hf])
    
    return aug_list

def flip_transpose(image, mask):
    aug_list = [[image, mask]]
    
    augmented = A.HorizontalFlip(p=1)(image=image, mask=mask)
    image_hf, mask_hf = augmented['image'], augmented['mask']
    aug_list.append([image_hf, mask_hf])
    
    augmented = A.VerticalFlip(p=1)(image=image, mask=mask)
    image_vf, mask_vf = augmented['image'], augmented['mask']
    aug_list.append([image_vf, mask_vf])
    
    augmented = A.VerticalFlip(p=1)(image=image_hf, mask=mask_hf)
    image_hf_vf, mask_hf_vf = augmented['image'], augmented['mask']
    aug_list.append([image_hf_vf, mask_hf_vf])
    
    augmented = A.Transpose(p=1)(image=image, mask=mask)
    image_t, mask_t = augmented['image'], augmented['mask']
    aug_list.append([image_t, mask_t])
    
    augmented = A.HorizontalFlip(p=1)(image=image_t, mask=mask_t)
    image_t_hf, mask_t_hf = augmented['image'], augmented['mask']
    aug_list.append([image_t_hf, mask_t_hf])

    augmented = A.VerticalFlip(p=1)(image=image_t, mask=mask_t)
    image_t_vf, mask_t_vf = augmented['image'], augmented['mask']
    aug_list.append([image_t_vf, mask_t_vf])
    
    augmented = A.VerticalFlip(p=1)(image=image_t_hf, mask=mask_t_hf)
    image_t_hf_vf, mask_t_hf_vf = augmented['image'], augmented['mask']
    aug_list.append([image_t_hf_vf, mask_t_hf_vf])
    
    return aug_list
    
def rgb_shift(image_mask_list, rseed):
    aug_list = []
    random.seed(rseed)
    
    rgb_shift_op = A.RGBShift(always_apply=True,
                              r_shift_limit=0.2, 
                              g_shift_limit=0.2,
                              b_shift_limit=0.2,
                              p=1)
    
    for image, mask in image_mask_list:
        image_rgb_shift = rgb_shift_op(image=image)['image'].clip(0, 1)
        aug_list.append([image_rgb_shift, mask])
    
    return aug_list

def save_aug_data(aug_list, save_path, image_name):
    for idx, (image, mask) in enumerate(aug_list):
        skimage.io.imsave(f'{save_path}/images_aug/{image_name}_{idx:2}.png'.replace(' ', '0'), image)
        np.save(f'{save_path}/gt_density_maps_aug/{image_name}_{idx:2}.npy'.replace(' ', '0'), mask)
        
def augment4_and_save(image, mask, save_path, image_name, rseed):
    aug_list1 = hflip(image, mask)
    aug_list2 = rgb_shift(aug_list1, rseed)
    aug_list = aug_list1 + aug_list2
    save_aug_data(aug_list, save_path, image_name)

def augment16_and_save(image, mask, save_path, image_name, rseed):
    aug_list1 = flip_transpose(image, mask)
    aug_list2 = rgb_shift(aug_list1, rseed)
    aug_list = aug_list1 + aug_list2
    save_aug_data(aug_list, save_path, image_name)

def augment_from_dir_and_save(in_path, save_path, rseed, aug_type):
    random.seed(rseed)
    images_aug_path = f'{save_path}/images_aug'
    gt_density_maps_aug_path = f'{save_path}/gt_density_maps_aug'
    shutil.rmtree(images_aug_path, ignore_errors=True)
    shutil.rmtree(gt_density_maps_aug_path, ignore_errors=True)
    os.makedirs(images_aug_path)
    os.makedirs(gt_density_maps_aug_path)
    
    img_names = sorted(os.listdir(f'{in_path}/images'))
    
    for img_name_png in img_names:
        img_name = img_name_png.split('.')[0]
        image = skimage.io.imread(f'{in_path}/images/{img_name_png}') / 255.
        mask = np.load(f'{in_path}/gt_density_maps/{img_name}.npy')
        if aug_type == 'aug4':
            augment4_and_save(image, mask, save_path, img_name, random.randint(0, 543210))
        elif aug_type == 'aug16':
            augment16_and_save(image, mask, save_path, img_name, random.randint(0, 543210))
        else:
            print('Wrong aug_type: {aug_type}')
            break

def augment4_from_dir_and_save(in_path, save_path, rseed=None):
    augment_from_dir_and_save(in_path, save_path, rseed=rseed, aug_type='aug4')
            
def augment16_from_dir_and_save(in_path, save_path, rseed=None):
    augment_from_dir_and_save(in_path, save_path, rseed=rseed, aug_type='aug16')