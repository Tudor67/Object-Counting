import matplotlib.pyplot as plt
import numpy as np

def plot_logs(train_loss, val_loss, title='loss'):
    x = np.arange(len(train_loss)) + 1
    
    plt.figure(figsize=(15,5))
    plt.subplot(1, 2, 1)
    plt.title(title)
    plt.plot(x, train_loss, label='train')
    plt.plot(x, val_loss, label='val')
    plt.ylabel(title)
    plt.xlabel('epoch')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.title(f'Log({title})')
    plt.plot(x, np.log(train_loss), label='train')
    plt.plot(x, np.log(val_loss), label='val')
    plt.ylabel(f'Log({title})')
    plt.xlabel('epoch')
    plt.legend()
    
    plt.show()
    
def plot_some_predictions(images, density_maps, preds):
    num_images = len(images)
    for i in range(num_images):
        plt.figure(figsize=(15, 12))
        plt.subplot(num_images, 3, 1)
        plt.title('Input image')
        plt.imshow(images[i])
        
        vmin = min(density_maps[i].min(), preds[i].min())
        vmax = max(density_maps[i].max(), preds[i].max())
        
        plt.subplot(num_images, 3, 2)
        plt.title(f'GT density map: {density_maps[i].sum():.2f}')
        plt.imshow(density_maps[i], cmap='jet', vmin=vmin, vmax=vmax)
        plt.colorbar(fraction=0.045, pad=0.04)
        plt.axis('off')

        plt.subplot(num_images, 3, 3)
        pred = preds[i].squeeze()
        plt.title(f'Predicted density map: {pred.sum():.2f}')
        plt.imshow(pred, cmap='jet', vmin=vmin, vmax=vmax)
        plt.colorbar(fraction=0.045, pad=0.04)
        plt.axis('off')
        
def plot_gt_vs_pred_counts(gt_counts, pred_counts, split_name, new_figure=True,
                           criterion='gt-pred', print_stats=True):
    diff = gt_counts - pred_counts
    if criterion == 'gt':
        diff = gt_counts
    sorted_indices = np.argsort(diff)
    
    if print_stats:
        print()
        print(f'{split_name} set: {len(gt_counts)} images')
        print(f'Underestimation in {(diff > 0).sum()} images')
        print(f'Overestimation in {(diff < 0).sum()} images')
        print(f'(GT stats)         counts per image: '
              f'mean={np.mean(gt_counts):.2f}, std={np.std(gt_counts):.2f}, '
              f'min={np.min(gt_counts)},    max={np.max(gt_counts)}')
        print(f'(Prediction stats) counts per image: '
              f'mean={np.mean(pred_counts):.2f}, std={np.std(pred_counts):.2f}, '
              f'min={np.min(pred_counts):.2f}, max={np.max(pred_counts):.2f}')
    
    if new_figure:
        plt.figure(figsize=(7.5, 5))
    plt.title(f'GT vs Predicted counts ({split_name} set: {len(gt_counts)} images)')
    plt.plot(gt_counts[sorted_indices], color='green', label='GT counts')
    plt.plot(pred_counts[sorted_indices], label='Predicted counts')
    plt.ylabel('Counts')
    if criterion == 'gt-pred':
        plt.xlabel('Image indices (ascending order of count difference)')
    else:
        plt.xlabel('Image indices (ascending order of ground truth counts)')
    plt.legend()
    
def plot_aug16(aug_list):
    img, mask = aug_list[0]
    img_hf, mask_hf = aug_list[1]
    img_vf, mask_vf = aug_list[2]
    img_hf_vf, mask_hf_vf = aug_list[3]
    img_t, mask_t = aug_list[4]
    img_t_hf, mask_t_hf = aug_list[5]
    img_t_vf, mask_t_vf = aug_list[6]
    img_t_hf_vf, mask_t_hf_vf = aug_list[7]
    
    img_rgb, mask_rgb = aug_list[8]
    img_hf_rgb, mask_hf_rgb = aug_list[9]
    img_vf_rgb, mask_vf_rgb = aug_list[10]
    img_hf_vf_rgb, mask_hf_vf_rgb = aug_list[11]
    img_t_rgb, mask_t_rgb = aug_list[12]
    img_t_hf_rgb, mask_t_hf_rgb = aug_list[13]
    img_t_vf_rgb, mask_t_vf_rgb = aug_list[14]
    img_t_hf_vf_rgb, mask_t_hf_vf_rgb = aug_list[15]
    
    num = 8
    plt.figure(figsize=(20, 5))
    
    plt.subplot(2, num, 1)
    plt.title('Original', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img)
    
    plt.subplot(2, num, num + 1)
    plt.axis('off')
    plt.imshow(mask, cmap='jet')
    
    plt.subplot(2, num, 2)
    plt.title('HFlip', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_hf)
    
    plt.subplot(2, num, num + 2)
    plt.axis('off')
    plt.imshow(mask_hf, cmap='jet')
    
    plt.subplot(2, num, 3)
    plt.title('VFlip', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_vf)
    
    plt.subplot(2, num, num + 3)
    plt.axis('off')
    plt.imshow(mask_vf, cmap='jet')
    
    plt.subplot(2, num, 4)
    plt.title('HFlip + VFlip', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_hf_vf)
    
    plt.subplot(2, num, num + 4)
    plt.axis('off')
    plt.imshow(mask_hf_vf, cmap='jet')
    
    plt.subplot(2, num, 5)
    plt.title('T', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_t)
    
    plt.subplot(2, num, num + 5)
    plt.axis('off')
    plt.imshow(mask_t, cmap='jet')
    
    plt.subplot(2, num, 6)
    plt.title('T + HFlip', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_t_hf)
    
    plt.subplot(2, num, num + 6)
    plt.axis('off')
    plt.imshow(mask_t_hf, cmap='jet')
    
    plt.subplot(2, num, 7)
    plt.title('T + VFlip', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_t_vf)
    
    plt.subplot(2, num, num + 7)
    plt.axis('off')
    plt.imshow(mask_t_vf, cmap='jet')
    
    plt.subplot(2, num, 8)
    plt.title('T + HFlip + VFlip', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_t_hf_vf)
    
    plt.subplot(2, num, num + 8)
    plt.axis('off')
    plt.imshow(mask_t_hf_vf, cmap='jet')
    
    
    plt.figure(figsize=(20, 5))
    plt.subplot(2, num, 1)
    plt.title('RGBShift', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_rgb)
    
    plt.subplot(2, num, num + 1)
    plt.axis('off')
    plt.imshow(mask_rgb, cmap='jet')
    
    plt.subplot(2, num, 2)
    plt.title('HFlip + RGBShift', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_hf_rgb)
    
    plt.subplot(2, num, num + 2)
    plt.axis('off')
    plt.imshow(mask_hf_rgb, cmap='jet')
    
    plt.subplot(2, num, 3)
    plt.title('VFlip + RGBShift', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_vf_rgb)
    
    plt.subplot(2, num, num + 3)
    plt.axis('off')
    plt.imshow(mask_vf_rgb, cmap='jet')
    
    plt.subplot(2, num, 4)
    plt.title('HFlip + VFlip + RGBShift', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_hf_vf_rgb)
    
    plt.subplot(2, num, num + 4)
    plt.axis('off')
    plt.imshow(mask_hf_vf_rgb, cmap='jet')
    
    plt.subplot(2, num, 5)
    plt.title('T + RGBShift', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_t_rgb)
    
    plt.subplot(2, num, num + 5)
    plt.axis('off')
    plt.imshow(mask_t_rgb, cmap='jet')
    
    plt.subplot(2, num, 6)
    plt.title('T + HFlip + RGBShift', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_t_hf_rgb)
    
    plt.subplot(2, num, num + 6)
    plt.axis('off')
    plt.imshow(mask_t_hf_rgb, cmap='jet')
    
    plt.subplot(2, num, 7)
    plt.title('T + VFlip + RGBShift', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_t_vf_rgb)
    
    plt.subplot(2, num, num + 7)
    plt.axis('off')
    plt.imshow(mask_t_vf_rgb, cmap='jet')
    
    plt.subplot(2, num, 8)
    plt.title('T + HFlip + VFlip + RGBShift', fontsize=8.2)
    plt.axis('off')
    plt.imshow(img_t_hf_vf_rgb)
    
    plt.subplot(2, num, num + 8)
    plt.axis('off')
    plt.imshow(mask_t_hf_vf_rgb, cmap='jet')
    
def plot_aug4(aug_list):
    img, mask = aug_list[0]
    img_hf, mask_hf = aug_list[1]
    
    img_rgb, mask_rgb = aug_list[2]
    img_hf_rgb, mask_hf_rgb = aug_list[3]
    
    num = 4
    figsize = (18, 6.5)
    fontsize = 13
    plt.figure(figsize=figsize)
    
    plt.subplot(2, num, 1)
    plt.title('Original', fontsize=fontsize)
    plt.axis('off')
    plt.imshow(img)
    
    plt.subplot(2, num, num + 1)
    plt.axis('off')
    plt.imshow(mask, cmap='jet')
    
    plt.subplot(2, num, 2)
    plt.title('HFlip', fontsize=fontsize)
    plt.axis('off')
    plt.imshow(img_hf)
    
    plt.subplot(2, num, num + 2)
    plt.axis('off')
    plt.imshow(mask_hf, cmap='jet')
    
    #plt.figure(figsize=figsize)
    plt.subplot(2, num, 3)
    plt.title('RGBShift', fontsize=fontsize)
    plt.axis('off')
    plt.imshow(img_rgb)
    
    plt.subplot(2, num, num + 3)
    plt.axis('off')
    plt.imshow(mask_rgb, cmap='jet')
    
    plt.subplot(2, num, 4)
    plt.title('HFlip + RGBShift', fontsize=fontsize)
    plt.axis('off')
    plt.imshow(img_hf_rgb)
    
    plt.subplot(2, num, num + 4)
    plt.axis('off')
    plt.imshow(mask_hf_rgb, cmap='jet')
    

def plot_seg_reg_maps(img, gt_seg_map, pred1, gt_density_map, pred2, mult_factor):
    fraction = 0.047
    pad = 0.02
    fontsize = 16

    num_plots = 5
    plt.figure(figsize=(20, 6))
    plt.subplot(1, num_plots, 1)
    plt.title('Input Image\n\n', fontsize=fontsize)
    plt.imshow(img)
    plt.colorbar(fraction=fraction, pad=pad)
    plt.axis('off')
    
    vmin = min(gt_seg_map.min(), pred1.min())
    vmax = max(gt_seg_map.max(), pred1.max())
    plt.subplot(1, num_plots, 2)
    plt.title(f'Ground Truth\nSegmentation Map\n{gt_seg_map.sum()}', fontsize=fontsize)
    plt.imshow(gt_seg_map.squeeze().astype(np.float32), cmap='gray', vmin=vmin, vmax=vmax)
    plt.colorbar(fraction=fraction, pad=pad)
    plt.axis('off')
    plt.subplot(1, num_plots, 3)
    plt.title(f'Prediction\nSegmentation Map\n{pred1.sum():.1f}', fontsize=fontsize)
    plt.imshow(pred1.squeeze(), cmap='gray', vmin=vmin, vmax=vmax)
    plt.colorbar(fraction=fraction, pad=pad)
    plt.axis('off')
    
    vmin = min(gt_density_map.min(), pred2.min()) / mult_factor
    vmax = max(gt_density_map.max(), pred2.max()) / mult_factor
    plt.subplot(1, num_plots, 4)
    plt.title(f'Ground Truth\nDensity Map\n{gt_density_map.sum()/mult_factor:.1f}', fontsize=fontsize)
    plt.imshow(gt_density_map.squeeze()/mult_factor, cmap='jet', vmin=vmin, vmax=vmax)
    plt.colorbar(fraction=fraction, pad=pad)
    plt.axis('off')
    plt.subplot(1, num_plots, 5)
    plt.title(f'Prediction\nDensity Map\n{pred2.sum()/mult_factor:.1f}', fontsize=fontsize)
    plt.imshow(pred2[0].squeeze()/mult_factor, cmap='jet', vmin=vmin, vmax=vmax)
    plt.colorbar(fraction=fraction, pad=pad)
    plt.axis('off')
    plt.show()