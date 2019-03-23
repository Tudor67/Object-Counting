import config
import keras.backend as K
import numpy as np
import pandas as pd

def density_maps_to_counts(density_maps):
    counts = K.sum(density_maps, axis=(1,2,3))
    counts /= config.DENSITY_MAP_MULTIPLICATION_FACTOR
    return counts

def mae(y_true_counts, y_pred_counts):
    return np.mean(np.abs(y_true_counts - y_pred_counts))

def mae_keras(y_true_density_maps, y_pred_density_maps):
    # density maps
    y_true_counts = density_maps_to_counts(y_true_density_maps)
    y_pred_counts = density_maps_to_counts(y_pred_density_maps)
    # counts
    return K.mean(K.abs(y_true_counts - y_pred_counts))

def rmse(y_true_counts, y_pred_counts):
    return np.sqrt(np.mean(np.square(y_true_counts - y_pred_counts)))

def rmse_keras(y_true_density_maps, y_pred_density_maps):
    # density maps
    y_true_counts = density_maps_to_counts(y_true_density_maps)
    y_pred_counts = density_maps_to_counts(y_pred_density_maps)
    # counts
    return K.sqrt(K.mean(K.square(y_true_counts - y_pred_counts)))

def underestimate(y_true_counts, y_pred_counts):
    return 100. * np.sum((y_true_counts - y_pred_counts) * (y_pred_counts < y_true_counts)) / y_true_counts.sum()

def underestimate_keras(y_true_density_maps, y_pred_density_maps):
    # density maps
    y_true_counts = density_maps_to_counts(y_true_density_maps)
    y_pred_counts = density_maps_to_counts(y_pred_density_maps)
    # counts
    less_mask = K.less(y_pred_counts, y_true_counts)
    less_mask = K.cast(less_mask, 'float32')
    true_pred_diff = y_true_counts - y_pred_counts
    true_sum = K.sum(y_true_counts)
    return 100. * K.sum(true_pred_diff * less_mask) / true_sum

def overestimate(y_true_counts, y_pred_counts):
    return 100. * np.sum((y_pred_counts - y_true_counts) * (y_pred_counts > y_true_counts)) / y_true_counts.sum()

def overestimate_keras(y_true_density_maps, y_pred_density_maps):
    # density maps
    y_true_counts = density_maps_to_counts(y_true_density_maps)
    y_pred_counts = density_maps_to_counts(y_pred_density_maps)
    # counts
    greater_mask = K.greater(y_pred_counts, y_true_counts)
    greater_mask = K.cast(greater_mask, 'float32')
    pred_true_diff = y_pred_counts - y_true_counts
    true_sum = K.sum(y_true_counts)
    return 100. * K.sum(pred_true_diff * greater_mask) / true_sum

def difference(y_true_counts, y_pred_counts):
    return underestimate(y_true_counts, y_pred_counts) + overestimate(y_true_counts, y_pred_counts)

def difference_keras(y_true_density_maps, y_pred_density_maps):
    # density maps -> counts
    under = underestimate_keras(y_true_density_maps, y_pred_density_maps)
    over = overestimate_keras(y_true_density_maps, y_pred_density_maps)
    return under + over

def evaluation_results_as_dict(counts_true, counts_pred, split_name, decimals=3):
    mae_v = mae(counts_true, counts_pred).round(decimals=decimals)
    rmse_v = rmse(counts_true, counts_pred).round(decimals=decimals)
    underestimate_v = f'{underestimate(counts_true, counts_pred):.{decimals}f}%'
    overestimate_v = f'{overestimate(counts_true, counts_pred):.{decimals}f}%'
    difference_v = f'{difference(counts_true, counts_pred):.{decimals}f}%'
    
    results = {
        split_name:{
            'MAE': mae_v,
            'RMSE': rmse_v,
            'Underestimate': underestimate_v,
            'Overestimate': overestimate_v,
            'Difference': difference_v
        }
    }
    
    return results

def evaluation_results_as_df(train_results, val_results, test_results,
                             architecture_name='',
                             sub_experiment_name='',
                             dataset_name=''):
    rows = ['train', 'val', 'test']
    data = {**train_results, **val_results, **test_results}
    df = pd.DataFrame.from_dict(data=data, orient='index').reindex(rows)
    df.reset_index(level=0, inplace=True)
    df.rename(columns={'index': 'Dataset_Split'}, inplace=True)
    
    df['Architecture_Name'] = architecture_name
    df['Experiment_Name'] = sub_experiment_name
    df['Dataset_Name'] = dataset_name
    df.set_index(['Architecture_Name', 'Experiment_Name',
                  'Dataset_Name', 'Dataset_Split'], inplace=True)
    
    return df