# FCRN-A (with data augmentation)

# Results
* Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Underestimate (%U), Overestimate (%O) and Difference (%D) on counting datasets.
* Results are presented just for the test set.

## VGG Cells Dataset
| Method                        | Loss    | Epochs | N     | MAE       | RMSE       | %U          | %O          | %D          |
| :---                          | :---:   | :---:  | :---: | :---:     | :---:      | :---:       | :---:       | :---:       |
| FCRN-A, full images           | MSE     | ~50    | 32    | 3.2 ± 0.3 | 4.1 ± 0.4  | 1.5% ± 0.3% | 0.4% ± 0.2% | 1.9% ± 0.1% |
| FCRN-A, full images           | MSE     | ~50    | 64    | 2.8 ± 0.3 | 3.6 ± 0.4  | 0.8% ± 0.4% | 0.7% ± 0.3% | 1.6% ± 0.2% |
| FCRN-A, full images           | LogCosh | ~50    | 32    | 3.1 ± 0.3 | 4.0 ± 0.4  | 1.2% ± 0.3% | 0.7% ± 0.3% | 1.8% ± 0.2% |
| FCRN-A, full images           | LogCosh | ~50    | 64    | 3.1 ± 0.3 | 4.1 ± 0.4  | 1.1% ± 0.5% | 0.7% ± 0.4% | 1.8% ± 0.2% |
| FCRN-A, patches 4 * (128x128) | MSE     | ~50    | 32    | 2.8 ± 0.3 | 3.8 ± 0.4  | 1.3% ± 0.3% | 0.4% ± 0.2% | 1.7% ± 0.2% |
| FCRN-A, patches 4 * (128x128) | MSE     | ~50    | 64    | 2.7 ± 0.5 | 3.6 ± 0.7  | 1.0% ± 0.5% | 0.5% ± 0.3% | 1.6% ± 0.3% |
| FCRN-A, patches 4 * (128x128) | LogCosh | ~50    | 32    | 3.0 ± 0.3 | 4.0 ± 0.3  | 1.0% ± 0.6% | 0.7% ± 0.5% | 1.8% ± 0.1% |
|`FCRN-A, patches 4 * (128x128)`|`LogCosh`|`~50`   |`64`   |`2.7 ± 0.5`|`3.6 ± 0.6` |`1.0% ± 0.4%`|`0.5% ± 0.3%`|`1.6% ± 0.3%`|

* N - number of train images;
* Our implementation includes data augmentation (augment16: flip, transpose, rgbshift and other combinations);
* Standard deviation corresponds to 5 different draws of training and validation sets;
* Counts per image: 174 ± 64;
* Optimizer: Adam(lr=1e-3).

## CARPK Dataset
| Method                        | Loss    | Epochs | MAE   | RMSE   | %U     | %O     |  %D    |
| :---                          | :---:   | :---:  | :---: | :---:  | :---:  | :---:  | :---:  | 
|`FCRN-A, full images`          |`MSE`    | `8/10` |`10.41`|`12.99` | `8.52%`| `1.54%`|`10.06%`|
| FCRN-A, patches 16 * (256x256)| MSE     |  4/5   | 11.18 | 14.03  |  8.57% |  2.24% | 10.81% |

* Optimizer: Adam(lr=1e-4).
