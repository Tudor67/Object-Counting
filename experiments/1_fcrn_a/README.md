# FCRN-A

# Results
* Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Underestimate (%U), Overestimate (%O) and Difference (%D) on counting datasets.
* Results are presented just for the test set.

## VGG Cells Dataset
| Method                        | Loss    | Epochs | N     | MAE       | RMSE       | %U          | %O          | %D          |
| :---                          | :---:   | :---:  | :---: | :---:     | :---:      | :---:       | :---:       | :---:       |
| FCRN-A, full images           | MSE     | ~100   | 32    | 6.0 ± 1.7 |  7.2 ± 1.8 | 0.6% ± 0.6% | 2.9% ± 1.4% | 3.5% ± 1.0% |
| FCRN-A, full images           | MSE     | ~100   | 64    | 5.4 ± 1.7 |  6.5 ± 1.9 | 2.5% ± 1.5% | 0.6% ± 0.7% | 3.1% ± 1.0% |
| FCRN-A, full images           | MAE     | ~100   | 32    | 8.3 ± 2.7 | 10.0 ± 3.1 | 4.6% ± 1.8% | 0.2% ± 0.3% | 4.8% ± 1.6% |
| FCRN-A, full images           | MAE     | ~100   | 64    | 6.6 ± 1.8 |  8.5 ± 2.1 | 3.7% ± 1.1% | 0.1% ± 0.1% | 3.9% ± 1.0% |
| FCRN-A, full images           | LogCosh | ~100   | 32    | 8.3 ± 1.8 |  9.8 ± 1.9 | 2.4% ± 2.7% | 2.4% ± 2.1% | 4.8% ± 1.0% |
|`FCRN-A, full images`          |`LogCosh`|`~100`  |`64`   |`3.6 ± 0.3`| `4.5 ± 0.4`|`0.9% ± 0.5%`|`1.2% ± 0.4%`|`2.1% ± 0.2%`|
| FCRN-A, patches 4 * (128x128) | MSE     | ~100   | 32    | 5.5 ± 0.5 |  6.6 ± 0.6 | 0.9% ± 1.0% | 2.2% ± 1.1% | 3.2% ± 0.3% |
| FCRN-A, patches 4 * (128x128) | MSE     | ~100   | 64    | 3.9 ± 1.1 |  4.8 ± 1.0 | 0.6% ± 0.4% | 1.7% ± 1.0% | 2.3% ± 0.7% |
| FCRN-A, patches 4 * (128x128) | MAE     | ~100   | 32    | 6.2 ± 1.8 |  8.0 ± 1.8 | 3.4% ± 1.1% | 0.2% ± 0.1% | 3.6% ± 1.0% |
| FCRN-A, patches 4 * (128x128) | MAE     | ~100   | 64    | 7.4 ± 1.0 |  9.2 ± 1.1 | 4.3% ± 0.6% | 0.0% ± 0.0% | 4.3% ± 0.6% |
| FCRN-A, patches 4 * (128x128) | LogCosh | ~100   | 32    | 5.0 ± 1.8 |  6.5 ± 2.5 | 1.7% ± 1.2% | 1.2% ± 0.7% | 2.9% ± 1.0% |
| FCRN-A, patches 4 * (128x128) | LogCosh | ~100   | 64    | 4.0 ± 0.9 |  5.3 ± 1.0 | 1.8% ± 0.9% | 0.5% ± 0.6% | 2.4% ± 0.5% |

* N - number of train images;
* Our implementation does not include data preprocessing and augmentation;
* Standard deviation corresponds to 5 different draws of training and validation sets;
* Counts per image: 174 ± 64.

## CARPK Dataset
| Method                        | Loss    | Epochs | MAE   | RMSE   | %U     | %O    |  %D    |
| :---                          | :---:   | :---:  | :---: | :---:  | :---:  | :---: | :---:  | 
| FCRN-A, full images           | MSE     |   15   | 21.15 |  26.34 | 13.07% | 7.38% | 20.45% |
| FCRN-A, full images           | MAE     |  1/15  | 95.54 | 103.78 | 92.30% | 0.02% | 92.32% |
| FCRN-A, full images           | LogCosh | 14/15  | 23.34 |  29.65 | 20.41% | 2.15% | 22.56% |
| FCRN-A, patches 32 * (128x128)| MSE     |   15   | 22.10 |  28.73 | 18.13% | 3.22% | 21.35% |

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
| Method                         | Loss    | Epochs | MAE    | RMSE   | %U      | %O     |  %D     |
| :---                           | :---:   | :---:  | :---:  | :---:  | :---:   | :---:  | :---:   |
| FCRN-A, full images            | MSE     |  5/20  |  52.95 |  74.53 |  19.08% | 23.73% |  42.81% |
| FCRN-A, full images            | MSE     |  3/100 |  53.27 |  67.10 |  11.61% | 31.45% |  43.06% |
| FCRN-A, full images            | MAE     | 51/100 | 123.70 | 155.97 | 100.00% |  0.00% | 100.00% |
|`FCRN-A, full images`           |`LogCosh`|`24/30` | `19.95`| `33.94`| `11.70%`| `4.43%`| `16.13%`|
| FCRN-A, full images            | LogCosh | 23/100 |  23.69 |  40.34 |  18.07% |  1.08% |  19.15% |
| FCRN-A, patches 32 * (128x128) | MSE     | 54/100 |  21.49 |  34.98 |   9.33% |  8.04% |  17.37% |
| FCRN-A, patches 32 * (128x128) | MAE     | 32/100 | 123.70 | 155.97 | 100.00% |  0.00% | 100.00% |
| FCRN-A, patches 32 * (128x128) | LogCosh | 86/100 |  20.81 |  38.11 |  15.44% |  1.38% |  16.82% |

* FCRN-A trained with 32 * (128x128) patches (MSE loss):

| Epochs | Split | MAE   | RMSE  | %U     | %O     | %D     |
| :---:  | :---: | :---: | :---: | :---:  | :---:  | :---:  |
|  1/5   | train | 62.72 | 82.35 | 19.99% | 30.69% | 50.68% |
|  1/5   | test  | 64.13 | 85.65 | 19.87% | 31.97% | 51.84% |
| 23/25  | train | 34.12 | 50.49 | 12.21% | 15.35% | 27.56% |
| 23/25  | test  | 36.77 | 55.55 | 13.81% | 15.91% | 29.72% |
| 15/50  | train | 28.90 | 43.02 | 10.23% | 13.12% | 23.35% |
| 15/50  | test  | 33.15 | 49.82 | 12.58% | 14.22% | 26.80% |
| 54/100 | train | 20.70 | 32.46 |  8.42% |  8.31% | 16.73% |
| 54/100 | test  | 21.49 | 34.98 |  9.33% |  8.04% | 17.37% |
