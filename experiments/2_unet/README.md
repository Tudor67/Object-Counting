# U-Net

# Results
* Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Underestimate (%U), Overestimate (%O) and Difference (%D) on counting datasets.
* Results are presented just for the test set.

## VGG Cells Dataset
| Method                       | Loss    | N     | MAE       | RMSE       | %U          | %O          | %D          |
| :---                         | :---:   | :---: | :---:     | :---:      | :---:       | :---:       | :---:       |
| U-Net, full images           | MSE     | 32    | 4.0 ± 0.8 | 5.0 ± 1.0  | 1.3% ± 0.9% | 1.1% ± 0.8% | 2.4% ± 0.5% |
| U-Net, full images           | MSE     | 64    | 3.5 ± 0.4 | 4.6 ± 0.6  | 1.2% ± 0.7% | 0.8% ± 0.5% | 2.0% ± 0.3% |
| U-Net, full images           | MAE     | 32    | 6.8 ± 2.0 | 8.4 ± 2.1  | 3.8% ± 1.3% | 0.1% ± 0.1% | 3.9% ± 1.1% |
| U-Net, full images           | MAE     | 64    | 5.5 ± 1.5 | 6.8 ± 1.7  | 3.0% ± 1.0% | 0.2% ± 0.1% | 3.2% ± 0.9% |
| U-Net, full images           | LogCosh | 32    | 4.9 ± 1.0 | 6.3 ± 1.4  | 2.4% ± 1.1% | 0.5% ± 0.5% | 2.9% ± 0.6% |
| U-Net, full images           | LogCosh | 64    | 3.4 ± 0.3 | 4.5 ± 0.5  | 1.2% ± 0.6% | 0.7% ± 0.4% | 2.0% ± 0.2% |
| U-Net, patches 4 * (128x128) | MSE     | 32    | 4.4 ± 0.9 | 5.4 ± 1.0  | 1.1% ± 0.8% | 1.4% ± 1.1% | 2.6% ± 0.5% |
|`U-Net, patches 4 * (128x128)`|`MSE`    |`64`   |`3.2 ± 0.1`|`4.2 ± 0.2` |`1.2% ± 0.3%`|`0.7% ± 0.3%`|`1.8% ± 0.0%`|
| U-Net, patches 4 * (128x128) | MAE     | 32    | 6.6 ± 1.4 | 8.1 ± 1.3  | 3.8% ± 0.9% | 0.1% ± 0.1% | 3.9% ± 0.8% |
| U-Net, patches 4 * (128x128) | MAE     | 64    | 6.8 ± 0.9 | 8.4 ± 1.2  | 4.0% ± 0.5% | 0.0% ± 0.0% | 4.0% ± 0.5% |
| U-Net, patches 4 * (128x128) | LogCosh | 32    | 5.5 ± 1.5 | 6.7 ± 1.4  | 2.3% ± 1.4% | 0.9% ± 0.6% | 3.2% ± 0.9% |
| U-Net, patches 4 * (128x128) | LogCosh | 64    | 3.2 ± 0.4 | 4.3 ± 0.4  | 1.1% ± 0.2% | 0.8% ± 0.4% | 1.9% ± 0.2% |

* Epochs: ~100;
* Batch size: 16;
* N - number of train images;
* Our implementation does not include data preprocessing and augmentation;
* Standard deviation corresponds to 5 different draws of training and validation sets;
* Counts per image: 174 ± 64.

## CARPK Dataset
| Method                       | Loss    | Epochs | MAE   | RMSE  | %U      | %O     |  %D    |
| :---                         | :---:   | :---:  | :---: | :---: | :---:   | :---:  | :---:  | 
| U-Net, full images           | MSE     | 13/15  | 17.91 | 22.75 |  6.12%  | 11.19% | 17.31% |

* U-Net trained with full images (MSE loss, 15 epochs) overfits the train set:

| Details               | Split | Loss  | Epochs | MAE    | RMSE  |
| :---                  | :---: | :---: | :---:  | :---:  | :---: |
| full images           | train | MSE   | 13/15  |  3.12  |  4.04 |
| full images           | test  | MSE   | 13/15  | 17.91  | 22.75 |
