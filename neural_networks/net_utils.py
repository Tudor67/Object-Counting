import numpy as np

def get_counts_from_density_maps(density_maps_batch):
    return np.sum(density_maps_batch, axis=(1,2,3))

def predict_density_maps_and_get_counts(model, data_generator,
                                        density_map_multiplication_factor):
    num_images = data_generator.get_size()
    batch_size = data_generator.batch_size
    
    counts_pred = np.empty(num_images, dtype=np.float32)
    
    for idx in range(data_generator.__len__()):
        # images
        batch_images, _ = data_generator.__getitem__(idx)
        # density maps
        batch_density_maps_pred = model.predict(batch_images) / density_map_multiplication_factor
        # counts
        batch_counts_pred = get_counts_from_density_maps(batch_density_maps_pred)
        counts_pred[idx*batch_size:(idx+1)*batch_size] = batch_counts_pred
    
    return counts_pred