import numpy as np
import os
import shutil

def move_data(in_split_path, out_split_path, ids_list):
    if not os.path.exists(in_split_path):
        print(f'{in_split_path} does not exist !')
    else:
        for dir_name in os.listdir(in_split_path):
            src_dir = f'{in_split_path}/{dir_name}'
            dest_dir = f'{out_split_path}/{dir_name}'
            
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            filenames = sorted(os.listdir(src_dir))

            for idx in ids_list:
                filename = filenames[idx]
                shutil.move(f'{src_dir}/{filename}',
                            f'{dest_dir}/{filename}')
                
def move_val_split_to_train(val_path, train_path):
    # move old validation data (if any) in train dir
    if os.path.exists(val_path):
        ids_list = np.arange(len(os.listdir(f'{val_path}/images')))
        move_data(val_path, train_path, ids_list)
        # remove validation dir 
        shutil.rmtree(val_path)
        
def create_val_split_from_train(train_path, val_path, val_size, rand_seed=None):
    # create validation split from initial train data
    np.random.seed(rand_seed)
    num_train = len(os.listdir(f'{train_path}/images'))
    ids_list = np.random.permutation(num_train)[-val_size:]
    move_data(train_path, val_path, ids_list)