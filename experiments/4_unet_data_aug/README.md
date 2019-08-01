# U-Net-A (with data augmentation)

# Results
* Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Underestimate (%U), Overestimate (%O) and Difference (%D) on counting datasets.
* Results are presented just for the test set.

## VGG Cells Dataset
| Method                        | Loss    | Epochs | N     | MAE       | RMSE       | %U          | %O          | %D          |
| :---                          | :---:   | :---:  | :---: | :---:     | :---:      | :---:       | :---:       | :---:       |
| U-Net, full images            | MSE     | ~30    | 32    | 3.4 ± 0.2 | 4.4 ± 0.3  | 1.1% ± 0.7% | 0.9% ± 0.7% | 2.0% ± 0.1% |
| U-Net, full images            | MSE     | ~30    | 64    | 2.8 ± 0.3 | 3.5 ± 0.3  | 0.7% ± 0.4% | 0.9% ± 0.5% | 1.6% ± 0.2% |
| U-Net, full images            | LogCosh | ~30    | 32    | 3.2 ± 0.3 | 4.0 ± 0.4  | 1.2% ± 0.4% | 0.6% ± 0.3% | 1.8% ± 0.2% |
| U-Net, full images            | LogCosh | ~30    | 64    | 2.8 ± 0.1 | 3.5 ± 0.1  | 1.1% ± 0.2% | 0.5% ± 0.3% | 1.6% ± 0.1% |
| U-Net, patches 4 * (128x128)  | MSE     | ~30    | 32    | 3.1 ± 0.4 | 4.0 ± 0.4  | 1.1% ± 0.5% | 0.7% ± 0.4% | 1.8% ± 0.2% |
| U-Net, patches 4 * (128x128)  | MSE     | ~30    | 64    | 3.1 ± 0.5 | 4.1 ± 0.8  | 1.1% ± 0.6% | 0.8% ± 0.4% | 1.9% ± 0.3% |
| U-Net, patches 4 * (128x128)  | LogCosh | ~30    | 32    | 2.8 ± 0.3 | 3.8 ± 0.4  | 0.7% ± 0.3% | 1.0% ± 0.3% | 1.6% ± 0.2% |
| U-Net, patches 4 * (128x128)  | LogCosh | ~30    | 64    | 2.8 ± 0.2 | 3.7 ± 0.2  | 1.1% ± 0.5% | 0.6% ± 0.4% | 1.7% ± 0.1% |

* N - number of train images;
* Our implementation includes data augmentation (augment16: flip, transpose, rgbshift and other combinations);
* Standard deviation corresponds to 5 different draws of training and validation sets;
* Counts per image: 174 ± 64;
* Optimizer: Adam(lr=1e-3).

## CARPK Dataset
| Method                        | Loss    | Epochs | MAE   | RMSE   | %U     | %O     |  %D    |
| :---                          | :---:   | :---:  | :---: | :---:  | :---:  | :---:  | :---:  |
| U-Net, full images            | MSE     |  4/10  | 10.27 | 13.36  | 5.40%  | 4.53%  |  9.93% |
| U-Net, full images            | LogCosh |  1/13  |  9.20 | 11.77  | 7.11%  | 1.78%  |  8.89% |
| U-Net, patches 16 * (256x256) | MSE     |  9/10  | 12.77 | 15.82  |11.40%  | 0.95%  | 12.35% |
| U-Net, patches 16 * (256x256) | LogCosh |  2/10  | 12.61 | 16.48  | 9.88%  | 2.30%  | 12.18% |

* Optimizer: Adam(lr=1e-4).
