# FCRN-A (with data augmentation)

# Results
* Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Underestimate (%U), Overestimate (%O) and Difference (%D) on counting datasets.
* Results are presented just for the test set.

## VGG Cells Dataset
| Method                        | Loss    | Epochs | N     | MAE       | RMSE       | %U          | %O          | %D          |
| :---                          | :---:   | :---:  | :---: | :---:     | :---:      | :---:       | :---:       | :---:       |
| FCRN-A, full images           | MSE     | ~100   | 32    | 3.2 ± 0.3 | 4.1 ± 0.4  | 1.5% ± 0.3% | 0.4% ± 0.2% | 1.9% ± 0.1% |
| FCRN-A, full images           | MSE     | ~100   | 64    | 2.8 ± 0.3 | 3.6 ± 0.4  | 0.8% ± 0.4% | 0.7% ± 0.3% | 1.6% ± 0.2% |

* N - number of train images;
* Our implementation includes data augmentation (augment16: flip, transpose, rgbshift and other combinations);
* Standard deviation corresponds to 5 different draws of training and validation sets;
* Counts per image: 174 ± 64.
