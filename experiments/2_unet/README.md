# U-Net

# Results
* Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Underestimate (%U), Overestimate (%O) and Difference (%D) on counting datasets.
* Results are presented just for the test set.

## VGG Cells Dataset
| Method                       | Loss    | Epochs | N     | MAE       | RMSE       | %U          | %O          | %D          |
| :---                         | :---:   | :---:  | :---: | :---:     | :---:      | :---:       | :---:       | :---:       |
| U-Net, full images           | MSE     | ~100   | 32    | 4.0 ± 0.8 | 5.0 ± 1.0  | 1.3% ± 0.9% | 1.1% ± 0.8% | 2.4% ± 0.5% |
| U-Net, full images           | MSE     | ~100   | 64    | 3.5 ± 0.4 | 4.6 ± 0.6  | 1.2% ± 0.7% | 0.8% ± 0.5% | 2.0% ± 0.3% |
| U-Net, full images           | MAE     | ~100   | 32    | | | | | | 
| U-Net, full images           | MAE     | ~100   | 64    | | | | | | 
| U-Net, full images           | LogCosh | ~100   | 32    | | | | | | 
| U-Net, full images           | LogCosh | ~100   | 64    | | | | | |
| U-Net, patches 4 * (128x128) | MSE     | ~100   | 32    | | | | | |
| U-Net, patches 4 * (128x128) | MSE     | ~100   | 64    | | | | | |
| U-Net, patches 4 * (128x128) | MAE     | ~100   | 32    | | | | | |
| U-Net, patches 4 * (128x128) | MAE     | ~100   | 64    | | | | | |
| U-Net, patches 4 * (128x128) | LogCosh | ~100   | 32    | | | | | |
| U-Net, patches 4 * (128x128) | LogCosh | ~100   | 64    | | | | | |

* N - number of train images;
* Our implementation does not include data preprocessing and augmentation;
* Standard deviation corresponds to 5 different draws of training and validation sets;
* Counts per image: 174 ± 64.
