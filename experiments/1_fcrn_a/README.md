# FCRN-A

# Results
* Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Underestimate (%U), Overestimate (%O) and Difference (%D) on counting datasets.
* Results are presented just for the test set.

## VGG Cells Dataset
| Method                        | Loss  | Epochs | N     | MAE       | RMSE       | %U          | %O          | %D          |
| :---                          | :---: | :---:  | :---: | :---:     | :---:      | :---:       | :---:       | :---:       |
| FCRN-A, full images           | MSE   | ~100   | 32    | 6.0 ± 1.7 |  7.2 ± 1.8 | 0.6% ± 0.6% | 2.9% ± 1.4% | 3.5% ± 1.0% |
| FCRN-A, patches 4 * (128x128) | MSE   | ~100   | 32    | 5.5 ± 0.5 |  6.6 ± 0.6 | 0.9% ± 1.0% | 2.2% ± 1.1% | 3.2% ± 0.3% |
| FCRN-A, full images           | MSE   | ~100   | 64    | 5.4 ± 1.7 |  6.5 ± 1.9 | 2.5% ± 1.5% | 0.6% ± 0.7% | 3.1% ± 1.0% |
|`FCRN-A, patches 4 * (128x128)`|`MSE`  |`~100`  |`64`   |`3.9 ± 1.1`| `4.8 ± 1.0`|`0.6% ± 0.4%`|`1.7% ± 1.0%`|`2.3% ± 0.7%`|
| FCRN-A, full images           | MAE   | ~100   | 32    | 8.3 ± 2.7 | 10.0 ± 3.1 | 4.6% ± 1.8% | 0.2% ± 0.3% | 4.8% ± 1.6% |
| FCRN-A, full images           | MAE   | ~100   | 64    | 6.6 ± 1.8 |  8.5 ± 2.1 | 3.7% ± 1.1% | 0.1% ± 0.1% | 3.9% ± 1.0% |

* N - number of train images;
* Our implementation does not include data preprocessing and augmentation;
* Standard deviation corresponds to 5 different draws of training and validation sets;
* Counts per image: 174 ± 64.

## CARPK Dataset
| Method                        | Loss  | Epochs | MAE    | RMSE  | %U     | %O    |  %D    |
| :---                          | :---: | :---:  | :---:  | :---: | :---:  | :---: | :---:  | 
| FCRN-A, full images           | MSE   | 15     | 21.15  | 26.34 | 13.07% | 7.38% | 20.45% |
| FCRN-A, patches 32 * (128x128)| MSE   | 15     | 22.10  |	28.73 | 18.13% | 3.22% | 21.35% |

* FCRN-A trained with full images or with 128x128 patches (MSE loss, 15 epochs) overfits the train set:

| Details               | Split | Loss  | Epochs | MAE    | RMSE  |
| :---                  | :---: | :---: | :---:  | :---:  | :---: |
| full images           | train | MSE   | 15     |  5.32  |  5.90 |
| full images           | test  | MSE   | 15     | 21.15  | 26.34 |
| patches 32 * (128x128)| train | MSE   | 15     |  3.65  |	 5.14 |
| patches 32 * (128x128)| test  | MSE   | 15     | 22.10  |	28.73 |

* FCRN-A trained with 32 * (128x128) patches (MSE loss):

| Epochs | Split | MAE   | RMSE  |
| :---:  | :---: | :---: | :---: |
| 1      | train | 20.01 | 23.50 |
| 1      | test  | 27.03 | 32.32 |
| 2      | train | 15.63 | 18.91 |
| 2      | test  | 18.65 | 25.01 |
| 3      | train |  7.16 |  9.37 |
|`3`     |`test` |`14.73`|`17.45`|
| 5      | train |  5.88 |  7.89 |
| 5      | test  | 16.02 | 19.84 |
| 10     | train |  3.92 |  5.25 |
| 10     | test  | 24.82 | 31.04 |
| 15     | train |  3.65 |  5.14 |
| 15     | test  | 22.10 | 28.73 |

## ShanghaiTech (Part B) Dataset
| Method              | Loss  | Epochs | MAE   | RMSE  | %U     | %O     |  %D    |
| :---                | :---: | :---:  | :---: | :---: | :---:  | :---:  | :---:  |
|`FCRN-A, full images`|`MSE`  |`5`     |`52.95`|`74.53`|`19.08%`|`23.73%`|`42.81%`|

