import numpy as np
import pandas as pd

def mae(y_true_counts, y_pred_counts):
    return np.mean(np.abs(y_true_counts - y_pred_counts))

def rmse(y_true_counts, y_pred_counts):
    return np.sqrt(np.mean(np.square(y_true_counts - y_pred_counts)))

def underestimate(y_true_counts, y_pred_counts):
    return 100. * np.sum((y_true_counts - y_pred_counts) * (y_pred_counts < y_true_counts)) / y_true_counts.sum()

def overestimate(y_true_counts, y_pred_counts):
    return 100. * np.sum((y_pred_counts - y_true_counts) * (y_pred_counts > y_true_counts)) / y_true_counts.sum()

def difference(y_true_counts, y_pred_counts):
    return underestimate(y_true_counts, y_pred_counts) + overestimate(y_true_counts, y_pred_counts)

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