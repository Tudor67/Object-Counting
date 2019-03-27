# FCRN-A

## VGG Cells Dataset

Mean absolute error (MAE) and standard deviations for cell counting on VGG Cells dataset.

| Method                                | Details                 | N = 32    | N = 64    |
| :---                                  | :---:                   | :---:     | :---:     |
| Lempitsky and Zisserman (2010)\[[1]\] | Linear ridge regression | 5.9 ± 0.5 | N/A       |
| Lempitsky and Zisserman (2010)\[[1]\] | Density learning        | 3.5 ± 0.2 | N/A       |
| Fiaschi et al. (2012)\[[2]\]          | Regression forests      | 3.2 ± 0.1 | N/A       |
| Arteta et al. (2014)\[[3]\]           | Interactive counting    | 3.5 ± 0.1 | N/A       |
| Xie et al. (2016)\[[4]\]              | FCRN-A                  | 2.9 ± 0.2 | 2.9 ± 0.2 |
| Xie et al. (2016)\[[4]\]              | FCRN-B                  | 3.3 ± 0.2 | 3.2 ± 0.2 |
| FCRN-A (our implementation)           | FCRN-A, MSE loss        | 6.0 ± 1.7 | 5.4 ± 1.7 |
| FCRN-A (our implementation)           | FCRN-A, MAE loss        | 8.3 ± 2.7 | 6.6 ± 1.8 |

* N - number of train images;
* Our implementation does not include data preprocessing and augmentation;
* Standard deviation corresponds to 5 different draws of training and validation sets;
* Results are presented just for the test set;
* Counts per image: 174 ± 64.

[1]: https://www.robots.ox.ac.uk/~vgg/publications/2010/Lempitsky10b/lempitsky10b.pdf
[2]: https://www.researchgate.net/publication/261130953_Learning_to_count_with_regression_forest_and_structured_labels
[3]: https://www.robots.ox.ac.uk/~vgg/publications/2014/Arteta14/arteta14.pdf
[4]: http://www.robots.ox.ac.uk/~vgg/publications/2016/Xie16/xie16.pdf
