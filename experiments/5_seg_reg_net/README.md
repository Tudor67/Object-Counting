# SegRegNet (with data augmentation)

# Results
* Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Underestimate (%U), Overestimate (%O) and Difference (%D) on counting datasets.
* Results are presented just for the test set.

## VGG Cells Dataset
| Method                           |   Method              | MAE       | RMSE      | %U          | %O          | %D          |
| :---                             |                       | :---:     | :---:     | :---:       | :---:       | :---:       |
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
