import numpy as np
import skimage

def load_bbs_from_txt(filename):
    with open(filename, 'r') as fi:
        data = fi.read().split()
        bbs = np.array(data).astype(np.int).reshape(-1, 5)
    return bbs[:, :4]

def load_bbs_from_dir(path, bbs_filenames):
    bbs = []
    for bbs_filename in bbs_filenames:
        bbs.append(load_bbs_from_txt(f'{path}/{bbs_filename}'))
    return bbs

def bb_to_dot(bb):
    x1, y1, x2, y2 = bb
    xc = (x1 + x2) // 2
    yc = (y1 + y2) // 2
    return (xc, yc)

def bbs_to_dots(bbs):
    dots = []
    for bb in bbs:
        dot = bb_to_dot(bb)
        dots.append(dot)
    return dots

def bbs_list_to_dots_list(bbs_list):
    dots_list = []
    for bbs in bbs_list:
        dots = bbs_to_dots(bbs)
        dots_list.append(dots)
    return dots_list

def create_dots_image(dots, img_shape):
    dots_img = np.zeros(img_shape, dtype=np.uint8)
    for (x, y) in dots:
        dots_img[y, x] = 255
    return dots_img

def save_dots_images(dots_list, img_shape, img_names, save_path):
    for dots, img_name in zip(dots_list, img_names):
        dots_img = create_dots_image(dots, img_shape)
        skimage.io.imsave(f'{save_path}/{img_name}', dots_img)
        
def load_dots_images(gt_path, gt_dots_names):
    gt_dots = []
    for gt_dots_name in gt_dots_names:
        gt_dots_path = f'{gt_path}/{gt_dots_name}'
        gt_dots_mask = skimage.io.imread(gt_dots_path) / 255.
        gt_dots.append(gt_dots_mask)
    return gt_dots