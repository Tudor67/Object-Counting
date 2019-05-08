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
| Method                        | Loss    | Epochs | MAE   | RMSE  | %U      | %O     |  %D    |
| :---                          | :---:   | :---:  | :---: | :---: | :---:   | :---:  | :---:  | 
| U-Net, full images            | MSE     | 13/15  | 17.91 | 22.75 |  6.12%  | 11.19% | 17.31% |
| U-Net, full images            | LogCosh | 12/15  | 18.44 | 23.68 | 14.28%  |  3.54% | 17.82% |
| U-Net, patches 32 * (128x128) | MSE     | 14/15  | 36.29 | 40.59 | 34.21%  |  0.86% | 35.07% |

* Batch size: 1 (full images) / 32 (patches 128x128)
___
* U-Net trained with full images (MSE loss) overfits the train set:

| Epochs | MAE    | RMSE  |
| :---:  | :---:  | :---: |
|   1    | 20.82  | 23.65 |
|   1    | 47.40  | 52.21 |
|   2    |  6.78  |  9.01 |
|   2    | 20.12  | 24.50 |
|   3    |  9.21  | 10.74 |
|   3    | 16.42  | 19.88 |
|   4    |  4.83  |  6.92 |
|  `4`   |`15.15` |`20.67`|
|   5    |  6.70  |  8.81 |
|   5    | 21.81  | 27.98 | 
|   6    |  4.62  |  6.58 |
|   6    | 25.97  | 32.83 | 
|   7    |  3.88  |  5.74 |
|   7    | 19.85  | 25.44 |
|  10    |  5.57  |  6.34 |
|  10    | 22.86  | 29.37 |
| 13/15  |  3.12  |  4.04 |
| 13/15  | 17.91  | 22.75 |
___
* U-Net trained with full images (LogCosh loss) overfits the train set:

| Epochs | MAE    | RMSE  |
| :---:  | :---:  | :---: |
|   1    |  9.93  | 12.85 |
|   1    | 45.20  | 49.91 |
|   3    |  6.08  |  8.08 |
|   3    | 24.23  | 30.16 |
|   5    |  3.81  |  5.41 |
|   5    | 21.78  | 27.67 |
|   7    |  4.14  |  5.53 |
|   7    | 20.80  | 26.44 |
|  10    |  2.05  |  2.88 |
| `10`   |`18.08` |`23.56`|
| 12/15  |  1.91  |  2.61 |
| 12/15  | 18.44  | 23.68 |
___
* U-Net trained with patches (32 * 128x128) (MSE loss) overfits the train set:

| Epochs | MAE    | RMSE  |
| :---:  | :---:  | :---: |
|   1    | 11.91  | 15.48 |
|   1    | 21.19  | 26.29 |
|   3    |  8.25  | 11.38 |
|   3    | 22.25  | 27.16 |
|   5    |  5.06  |  7.59 |
|   5    | 19.10  | 24.58 |
|   7    |  4.42  |  6.64 |
|   7    | 23.87  | 28.64 |
|  10    |  4.07  |  5.62 |
|  10    | 20.00  | 26.53 |
| 14/15  |  3.80  |  5.27 |
| 14/15  | 36.29  | 40.59 |
___
