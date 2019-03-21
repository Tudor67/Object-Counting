import numpy as np
import pandas as pd

def mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def rmse(y_true, y_pred):
    return np.sqrt(np.mean(np.square(y_true - y_pred)))

def underestimate(y_true, y_pred):
    return 100. * np.sum((y_true - y_pred) * (y_pred < y_true)) / y_true.sum()

def overestimate(y_true, y_pred):
    return 100. * np.sum((y_pred - y_true) * (y_pred > y_true)) / y_true.sum()

def difference(y_true, y_pred):
    return underestimate(y_true, y_pred) + overestimate(y_true, y_pred)

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