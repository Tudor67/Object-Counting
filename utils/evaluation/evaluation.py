import numpy as np

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