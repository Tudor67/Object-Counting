import config
import keras
import numpy as np
import os
import skimage.io

class DataGenerator(keras.utils.Sequence):
    def __init__(self, dataset_path, dataset_split='train',
                 dim=(256, 256, 3), batch_size=32, shuffle=True):
        
        path = f'{dataset_path}/{dataset_split}'
        img_path = f'{path}/images'
        density_map_path = f'{path}/gt_density_maps'
        img_names = sorted(os.listdir(img_path))
        density_map_names = sorted(os.listdir(density_map_path))
        
        self.path = path
        self.img_path = img_path
        self.density_map_path = density_map_path
        self.img_names = img_names
        self.density_map_names = density_map_names
        self.dim = dim
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.on_epoch_end()
        
    def __len__(self):
        return int(np.floor(len(self.img_names) / float(self.batch_size)))
    
    def on_epoch_end(self):
        self.indexes = np.arange(len(self.img_names))
        if self.shuffle:
            np.random.shuffle(self.indexes)
        
    def __data_generation__(self, img_ids_list):
        X = np.empty((self.batch_size, *self.dim))
        y = np.empty((self.batch_size, *self.dim[:2], 1))
        
        for i, img_idx in enumerate(img_ids_list):
            img_name = self.img_names[img_idx]
            density_map_name = self.density_map_names[img_idx]
            
            X[i] = skimage.io.imread(f'{self.img_path}/{img_name}') / 255.
            y[i] = np.load(f'{self.density_map_path}/{density_map_name}')[..., None] *\
                   config.DENSITY_MAP_MULTIPLICATION_FACTOR
            
        return X, y
    
    def __getitem__(self, index):
        # generate one batch of data
        img_ids_list = self.indexes[index*self.batch_size:(index+1)*self.batch_size]
        X, y = self.__data_generation__(img_ids_list)
        return X, y
    
    def get_size(self):
        return len(self.img_names)