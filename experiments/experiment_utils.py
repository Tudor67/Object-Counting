import numpy as np
import os
import pandas as pd

def load_experiments_results(experiments_path, experiments_substrings, verbose=True, csv_name='results'):
    res_list = []
    
    experiment_names = os.listdir(experiments_path)
    for exp_name in experiment_names:
        if all(exp_substring in exp_name for exp_substring in experiments_substrings):
            if verbose:
                print(exp_name)
            res_path = f'{experiments_path}/{exp_name}/results/quantitative/{csv_name}.csv'
            if os.path.isfile(res_path):
                res_df = pd.read_csv(res_path, index_col=[3])
                res_list.append(res_df)
    
    return res_list

def get_mean_and_std_of_experiments(res_list, experiments_remarks='', decimals=1):
    res_dict = {}
    eval_metrics = ['MAE', 'RMSE', 'Underestimate', 'Overestimate', 'Difference']
    
    for split_name in ['train', 'val', 'test']:
        res_dict[split_name] = {}
        
        for eval_metric in eval_metrics:
            res_dict[split_name][eval_metric + '_all'] = []
            contains_percent = False
            
            for pd_df in res_list:
                r = pd_df.loc[split_name][eval_metric]
                
                if isinstance(r, str):
                    if '%' in r:
                        r = r.split('%')[0]
                        contains_percent = True
                    r = float(r)
                
                r = float(f'{r:.{decimals}f}')
                res_dict[split_name][eval_metric + '_all'].append(r)
            
            r_mean = float(f'{np.mean(res_dict[split_name][eval_metric + "_all"]):.{decimals}f}')
            r_std = float(f'{np.std(res_dict[split_name][eval_metric + "_all"]):.{decimals}f}')
            r_mean_std = f'{r_mean} \u00B1 {r_std}'
            
            if contains_percent:
                r_mean_std = f'{r_mean}% \u00B1 {r_std}%'
                             
            res_dict[split_name][eval_metric] = r_mean_std
            
    rows = ['train', 'val', 'test']
    res_df = pd.DataFrame.from_dict(data=res_dict, orient='index').reindex(rows)
    res_df['Experiments_Remarks'] = experiments_remarks              
    res_df.drop(columns=[eval_metric + "_all" for eval_metric in eval_metrics],
                inplace=True)
    
    return res_df