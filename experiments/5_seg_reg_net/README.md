# SegRegNet (with data augmentation)

# Results
* Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Underestimate (%U), Overestimate (%O) and Difference (%D) on counting datasets.
* Results are presented just for the test set.

## VGG Cells Dataset
| Method                           |   Method              | MAE       | RMSE      | %U          | %O          | %D          |
| :---                             |     :---:             | :---:     | :---:     | :---:       | :---:       | :---:       |
| SegRegNet, patches 4 * (128x128) | density_map           | 3.0 ± 0.2 | 3.9 ± 0.3 | 0.9% ± 0.4% | 0.9% ± 0.4% | 1.7% ± 0.1% |
|`SegRegNet, patches 4 * (128x128)`|`density_map*(seg>thr)`|`2.8 ± 0.4`|`3.9 ± 0.6`|`1.2% ± 0.4%`|`0.5% ± 0.2%`|`1.7% ± 0.2%`|

Details:
- N = 64;
- SegLoss = binary_crossentropy;
- RegLoss = logcosh;
- Seg epochs = 10;
- Reg epochs = 25;
- thr = 1e-3;

* Seg - segmentation (rough segmentation);
* Reg - regression (of density maps);
* N - number of train images;
* Our implementation includes data augmentation (augment16: flip, transpose, rgbshift and other combinations);
* Standard deviation corresponds to 5 different draws of training and validation sets;
* Counts per image: 174 ± 64;
* Optimizer: Adam(lr=1e-3).

## CARPK Dataset
| Method                 |  Method               | MAE   | RMSE  | %U    | %O    |  %D   |
| :---                   |   :---:               | :---: | :---: | :---: | :---: | :---: |
|`SegRegNet, full images`|`density_map`          |`8.47` |`10.71`|`6.85%`|`1.34%`|`8.19%`|
| SegRegNet, full images | density_map*(seg>thr) | 8.66  | 10.91 | 7.10% | 1.26% | 8.36% |

Details:
- SegLoss = binary_crossentropy;
- RegLoss = logcosh;
- Seg epochs = 3/3;
- Reg epochs = 2/3;
- thr = 1e-3;

* Optimizer: Adam(lr=1e-4).

## ShanghaiTech (Part B) Dataset
| Method                            |  Method               | MAE    | RMSE   | %U     | %O     |  %D    |
| :---                              | :---:                 | :---:  | :---:  | :---:  | :---:  | :---:  |
| SegRegNet, patches 16 * (256x256) | density_map           | 18.94  | 30.79  | 10.10% |  5.21% | 15.31% |
|`SegRegNet, patches 16 * (256x256)`|`density_map*(seg>thr)`|`18.83` |`30.71` | `9.79%`| `5.43%`|`15.22%`|

Details:
- SegLoss = binary_crossentropy;
- RegLoss = logcosh;
- Seg epochs = 23/25;
- Reg epochs = 18/50;
- thr = 1e-3;

* Optimizer: Adam(lr=1e-4).
