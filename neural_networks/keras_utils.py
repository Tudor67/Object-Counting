from keras.callbacks import Callback
from neural_networks.net_utils import *
from utils.evaluation.evaluation import *

class EvalMetricsCallback(Callback):
    def __init__(self, density_map_multiplication_factor,
                 train_generator=None, val_generator=None):
        self.density_map_multiplication_factor = density_map_multiplication_factor
        self.train_generator = train_generator
        self.val_generator = val_generator
        
        self.train_gt_counts = get_gt_counts_from_data_generator(self.train_generator,
                                                                 self.density_map_multiplication_factor)
        self.val_gt_counts = get_gt_counts_from_data_generator(self.val_generator,
                                                               self.density_map_multiplication_factor)
    
    def update_current_logs(current_logs, new_logs):
        split_name = list(new_logs.keys())[0]
        
        for key in new_logs[split_name].keys():
            new_key = f'{split_name}_{key.lower()}'
            new_value = new_logs[split_name][key]
            
            if isinstance(new_value, str):
                new_value = float(new_value.split('%')[0])
            
            new_value = float(f'{new_value:.3f}')
            
            current_logs[new_key] = new_value
        
    def on_epoch_end(self, epoch, logs={}):
        train_pred_counts = predict_density_maps_and_get_counts(self.model,
                                                                self.train_generator,
                                                                self.density_map_multiplication_factor)        
        val_pred_counts = predict_density_maps_and_get_counts(self.model,
                                                              self.val_generator,
                                                              self.density_map_multiplication_factor)
        train_logs = evaluation_results_as_dict(self.train_gt_counts, train_pred_counts, 'train')
        val_logs = evaluation_results_as_dict(self.val_gt_counts, val_pred_counts, 'val')
        
        EvalMetricsCallback.update_current_logs(logs, train_logs)
        EvalMetricsCallback.update_current_logs(logs, val_logs)