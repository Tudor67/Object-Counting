# FCRN-A

# Results
* Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Underestimate (%U), Overestimate (%O) and Difference (%D) on counting datasets.
* Results are presented just for the test set.

## VGG Cells Dataset
| Method                        | Loss  | Epochs | N     | MAE       | RMSE       | %U          | %O          | %D          |
| :---:                         | :---: | :---:  | :---: | :---:     | :---:      | :---:       | :---:       | :---:       |
| FCRN-A, full images           | MSE   | ~100   | 32    | 6.0 ± 1.7 |  7.2 ± 1.8 | 0.6% ± 0.6% | 2.9% ± 1.4% | 3.5% ± 1.0% |
| FCRN-A, patches 4 * (128x128) | MSE   | ~100   | 32    | 5.5 ± 0.5 |  6.6 ± 0.6 | 0.9% ± 1.0% | 2.2% ± 1.1% | 3.2% ± 0.3% |
| FCRN-A, full images           | MSE   | ~100   | 64    | 5.4 ± 1.7 |  6.5 ± 1.9 | 2.5% ± 1.5% | 0.6% ± 0.7% | 3.1% ± 1.0% |
| FCRN-A, patches 4 * (128x128) | MSE   | ~100   | 64    | 3.9 ± 1.1 |  4.8 ± 1.0 | 0.6% ± 0.4% | 1.7% ± 1.0% | 2.3% ± 0.7% |
| FCRN-A, full images           | MAE   | ~100   | 32    | 8.3 ± 2.7 | 10.0 ± 3.1 | 4.6% ± 1.8% | 0.2% ± 0.3% | 4.8% ± 1.6% |
| FCRN-A, full images           | MAE   | ~100   | 64    | 6.6 ± 1.8 |  8.5 ± 2.1 | 3.7% ± 1.1% | 0.1% ± 0.1% | 3.9% ± 1.0% |

* N - number of train images;
* Our implementation does not include data preprocessing and augmentation;
* Standard deviation corresponds to 5 different draws of training and validation sets;
* Counts per image: 174 ± 64.

## CARPK Dataset
| Method              | Loss  | Epochs | MAE    | RMSE  | %U     | %O    |  %D    |
| :---:               | :---: | :---:  | :---:  | :---: | :---:  | :---: | :---:  | 
| FCRN-A, full images | MSE   | 15     | 21.15  | 26.34 | 13.07% | 7.38% | 20.45% |

## ShanghaiTech (Part B) Dataset
| Method              | Loss  | Epochs | MAE   | RMSE  | %U     | %O     |  %D    |
| :---:               | :---: | :---:  | :---: | :---: | :---:  | :---:  | :---:  |
| FCRN-A, full images | MSE   | 5      | 52.95 | 74.53 | 19.08% | 23.73% | 42.81% |

