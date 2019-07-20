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
| U-Net, patches 4 * (128x128)  | MSE     | ~50    | 32    | | | | | |
| U-Net, patches 4 * (128x128)  | MSE     | ~50    | 64    | | | | | |
| U-Net, patches 4 * (128x128)  | LogCosh | ~50    | 32    | | | | | |
| U-Net, patches 4 * (128x128)  | LogCosh | ~50    | 64    | | | | | |

* N - number of train images;
* Our implementation includes data augmentation (augment16: flip, transpose, rgbshift and other combinations);
* Standard deviation corresponds to 5 different draws of training and validation sets;
* Counts per image: 174 ± 64;
* Optimizer: Adam(lr=1e-3).
