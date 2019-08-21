import numpy as np

def get_counts_from_density_maps(density_maps_batch):
    return np.sum(density_maps_batch, axis=(1,2,3))

def predict_density_maps_and_get_counts(model, data_generator,
                                        density_map_multiplication_factor,
                                        output_mode=None,
                                        pred_seg_thr=None):
    num_images = data_generator.get_size()
    batch_size = data_generator.batch_size
    
    counts_pred = np.empty(num_images, dtype=np.float32)
    
    for idx in range(data_generator.__len__()):
        # images
        batch_images, _ = data_generator.__getitem__(idx)
        # density maps
        if output_mode is None:
            batch_density_maps_pred = model.predict(batch_images) / density_map_multiplication_factor
        elif output_mode == 'seg_reg':
            batch_seg_maps_pred, batch_density_maps_pred = model.predict(batch_images)
            if pred_seg_thr is not None:
                batch_density_maps_pred *= (batch_seg_maps_pred > pred_seg_thr)
                
            batch_density_maps_pred /= density_map_multiplication_factor
                
        # counts
        batch_counts_pred = get_counts_from_density_maps(batch_density_maps_pred)
        counts_pred[idx*batch_size:(idx+1)*batch_size] = batch_counts_pred
    
    return counts_pred

def get_gt_counts_from_data_generator(data_generator, density_map_multiplication_factor):
    num_images = data_generator.get_size()
    batch_size = data_generator.batch_size
    
    gt_counts = np.empty(num_images, dtype=np.float32)
    for idx in range(data_generator.__len__()):
        # images
        _, batch_density_maps = data_generator.__getitem__(idx)
        batch_counts = get_counts_from_density_maps(batch_density_maps) / density_map_multiplication_factor
        gt_counts[idx*batch_size:(idx+1)*batch_size] = batch_counts
    
    return gt_counts