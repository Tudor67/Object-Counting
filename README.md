# Object-Counting
Computer Vision Research Project  
![object_counting_problem](./images/object_counting_problem.png)

## Counting datasets
### VGG Cells
* Synthetic dataset;
* 200 images (256x256) containing simulated bacterial cells from fluorescence-light microscopy;
* Number of cells per image: 174 ± 64;
* Ground-truth: dot annotations.  
![vgg_cells_dataset](./images/vgg_cells_dataset.png)

### CARPK
* 1,448 images (720x1280) of cars captured from different parking lots;
* 90,000 cars;
* Number of cars in a single scene: [1, 188];
* Ground-truth: bounding boxes.  
![carpk_dataset](./images/carpk_dataset.png)

### ShanghaiTech (Part B)
* Crowd counting dataset;
* 716 images (768x1024) taken from busy streets;
* Number of people in an image: [9, 539];
* Ground-truth: dot annotations.  
![shanghai_tech_part_b_dataset](./images/shanghai_tech_part_b_dataset.png)

## Counting approaches
![counting_approaches](./images/counting_approaches.png)

## Quantitative results
### VGG Cells
Mean Absolute Error (MAE) and standard deviations for cell counting on VGG Cells dataset.

| Method                                | Details                                   | N = 32    | N = 64    |
| :---                                  | :---                                      | :---:     | :---:     |
| Lempitsky and Zisserman (2010)\[[1]\] | Linear ridge regression                   | 5.9 ± 0.5 | N/A       |
| Lempitsky and Zisserman (2010)\[[1]\] | Density learning                          | 3.5 ± 0.2 | N/A       |
| Fiaschi et al. (2012)\[[2]\]          | Regression forests                        | 3.2 ± 0.1 | N/A       |
| Arteta et al. (2014)\[[3]\]           | Interactive counting                      | 3.5 ± 0.1 | N/A       |
| Xie et al. (2016)\[[4]\]              | FCRN-A                                    | 2.9 ± 0.2 | 2.9 ± 0.2 |
| Xie et al. (2016)\[[4]\]              | FCRN-B                                    | 3.3 ± 0.2 | 3.2 ± 0.2 |
|__Cohen et al. (2017)__\[[5]\]         |__Count-ception__                          |__2.4 ± 0.4__|__2.3 ± 0.4 (N=50)__  |
| Our implementation (without data aug) | ---                                       | ---       | ---       |
| FCRN-A                                | FCRN-A, MSE loss, full images             | 6.0 ± 1.7 | 5.4 ± 1.7 |
| FCRN-A                                | FCRN-A, MAE loss, full images             | 8.3 ± 2.7 | 6.6 ± 1.8 |
| FCRN-A                                | FCRN-A, LogCosh loss, full images         | 8.3 ± 1.8 | 3.6 ± 0.3 |
| FCRN-A                                | FCRN-A, MSE loss, patches 4*(128x128)     | 5.5 ± 0.5 | 3.9 ± 1.1 |
| FCRN-A                                | FCRN-A, MAE loss, patches 4*(128x128)     | 6.2 ± 1.8 | 7.4 ± 1.0 |
| FCRN-A                                | FCRN-A, LogCosh loss, patches 4*(128x128) | 5.0 ± 1.8 | 4.0 ± 0.9 |
| U-Net                                 | U-Net, MSE loss, full images              | 4.0 ± 0.8 | 3.5 ± 0.4 |
| U-Net                                 | U-Net, MAE loss, full images              | 6.8 ± 2.0 | 5.5 ± 1.5 |
| U-Net                                 | U-Net, LogCosh loss, full images          | 4.9 ± 1.0 | 3.4 ± 0.3 |
|`U-Net`                                |`U-Net, MSE loss, patches 4*(128x128)`     |`4.4 ± 0.9`|`3.2 ± 0.1`|
| U-Net                                 | U-Net, MAE loss, patches 4*(128x128)      | 6.6 ± 1.4 | 6.8 ± 0.9 |
| U-Net                                 | U-Net, LogCosh loss, patches 4*(128x128)  | 5.5 ± 1.5 | 3.2 ± 0.4 |
| Our implementation (with data aug)    | ---                                       | ---       | ---       |
| FCRN-A                                | FCRN-A, MSE loss, full images             | 3.2 ± 0.3 | 2.8 ± 0.3 |
| FCRN-A                                | FCRN-A, LogCosh loss, full images         | 3.1 ± 0.3 | 3.1 ± 0.3 |
| FCRN-A                                | FCRN-A, MSE loss, patches 4*(128x128)     | 2.8 ± 0.3 | 2.7 ± 0.5 |
| FCRN-A                                | FCRN-A, LogCosh loss, patches 4*(128x128) | 3.0 ± 0.3 | 2.7 ± 0.5 |
| U-Net                                 | U-Net, MSE loss, full images              | 3.4 ± 0.2 | 2.8 ± 0.3 |
| U-Net                                 | U-Net, LogCosh loss, full images          | 3.2 ± 0.3 | 2.8 ± 0.1 |
| U-Net                                 | U-Net, MSE loss, patches 4*(128x128)      | 3.1 ± 0.4 | 3.1 ± 0.5 |
|`U-Net`                                |`U-Net, LogCosh loss, patches 4*(128x128)` |`2.8 ± 0.3`|`2.8 ± 0.2`|
| SegRegNet, density_map                | SegRegNet, LogCosh loss, patches 4*(128x128)| N/A     | 3.0 ± 0.2 |
| SegRegNet, density_map*(seg_map>1e-3) | SegRegNet, LogCosh loss, patches 4*(128x128)| N/A     | 2.8 ± 0.4 |


* N - number of train images;
* Our implementation does not include data preprocessing;
* Standard deviation corresponds to 5 different draws of training and validation sets;
* Results are presented just for the test set;
* Counts per image: 174 ± 64.

### CARPK
Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Underestimate (%U), Overestimate (%O) and Difference (%D) on CARPK dataset.  
MAE, RMSE, %U, %O for LPN, GAP and GSP are taken from Aich et al. (2018) \[[8]\].

| Method                      | Details                                                 | MAE   | RMSE  | %U     | %O     |  %D    |
| :---                        | :---                                                    | :---: | :---: | :---:  | :---:  | :---:  | 
| Hsieh et al. (2017) \[[6]\] | LPN                                                     | 13.72 | 21.77 |  N/A   |  N/A   |  N/A   |
| Aich et al. (2018) \[[7]\]  | GAP-224, patches                                        |  7.65 |  9.59 |  6.56% |  0.84% |  7.40% |
| Aich et al. (2018) \[[7]\]  | GAP-Full, full images                                   | 19.61 | 21.65 | 18.71% |  0.24% | 18.95% |
|__Aich et al. (2018)__ \[[8]\]|__GSP-224, patches__                                    |__5.46__|__8.09__|__4.14%__|__1.14%__|__5.28%__|
| Aich et al. (2018) \[[8]\]  | GSP-Full, full images                                   | 32.94 | 36.23 | 31.42% |  0.42% | 31.84% |
| Our implementation (without data aug)| ---                                            | ---   | ---   | ---    |  ---   | ---    |
| FCRN-A                      | FCRN-A, MSE loss, full images, 15 epochs                | 21.15 | 26.34 | 13.07% |  7.38% | 20.45% |
| FCRN-A                      | FCRN-A, LogCosh loss, full images, 15 epochs            | 23.34 | 29.65 | 20.41% |  2.15% | 22.56% |
| FCRN-A                      | FCRN-A, MSE loss, patches 32 * (128x128), 15 epochs     | 22.10 | 28.73 | 18.13% |  3.22% | 21.35% |
| FCRN-A                      | FCRN-A, MSE loss, patches 32 * (128x128),  3 epochs     | 14.73 | 17.45 |  2.15% | 12.08% | 14.23% |
| FCRN-A                      | FCRN-A, LogCosh loss, patches 32 * (128x128), 15 epochs | 26.19 | 31.63 | 23.81% |  1.50% | 25.31% | 
|`FCRN-A`                     |`FCRN-A, LogCosh loss, patches 32 * (128x128),  5 epochs`|`12.13`|`15.72`| `5.62%`| `6.10%`|`11.72%`|
| U-Net                       | U-Net, MSE loss, full images, 13/15 epochs              | 17.91 | 22.75 |  6.12% | 11.19% | 17.31% |
| U-Net                       | U-Net, LogCosh loss, full images, 12/15 epochs          | 18.44 | 23.68 | 14.28% |  3.54% | 17.82% |
| U-Net                       | U-Net, MSE loss, patches 32 * (128x128), 14/15 epochs   | 36.29 | 40.59 | 34.21% |  0.86% | 35.07% |
| U-Net                       | U-Net, LogCosh loss, patches 32 * (128x128), 15/15 epochs| 26.67| 30.91 | 25.18% |  0.59% | 25.77% |
| U-Net                       | U-Net, LogCosh loss, patches 32 * (128x128), 3/3 epochs | 14.03 | 16.49 |  4.72% |  8.83% | 13.55% |
| Our implementation (with data aug)| ---                                               | ---   | ---   | ---    |  ---   | ---    |
| FCRN-A                      | FCRN-A, MSE loss, full images, 8/10 epochs              | 10.41 | 12.99 |  8.52% |  1.54% | 10.06% |
| FCRN-A                      | FCRN-A, LogCosh loss, full images, 2/10 epochs          |  9.95 | 14.92 |  7.94% |  1.68% |  9.62% |
| FCRN-A                      | FCRN-A, MSE loss, patches 16 * (256x256), 4/5 epochs    | 11.18 | 14.03 |  8.57% |  2.24% | 10.81% |
| FCRN-A                      | FCRN-A, LogCosh loss, patches 16 * (256x256), 2/5 epochs| 12.24 | 17.02 |  9.72% |  2.10% | 11.82% |
| U-Net                       | U-Net, MSE loss, full images, 4/10 epochs               | 10.27 | 13.36 |  5.40% |  4.53% |  9.93% |
| U-Net                       | U-Net, LogCosh loss, full images, 1/13 epochs           |  9.20 | 11.77 |  7.11% |  1.78% |  8.89% |
| U-Net                       | U-Net, MSE loss, patches 16 * (256x256), 9/10 epochs    | 12.77 | 15.82 | 11.40% |  0.95% | 12.35% |
| U-Net                       | U-Net, LogCosh loss, patches 16 * (256x256), 2/10 epochs| 12.61 | 16.48 |  9.88% |  2.30% | 12.18% |
|`SegRegNet, density_map`     |`SegRegNet, LogCosh loss, full images`                   |`8.47` |`10.71`|`6.85%` |`1.34%` |`8.19%` |
| SegRegNet, density_map*(seg>1e-3)| SegRegNet, LogCosh loss, full images               | 8.66  | 10.91 | 7.10%  | 1.26%  | 8.36%  |


### ShanghaiTech (Part B)
Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Underestimate (%U), Overestimate (%O) and Difference (%D) on ShanghaiTech (Part B) dataset.

| Method                           | Details                                                     | MAE   | RMSE  | %U     | %O     |  %D    |
| :---                             | :---                                                        | :---: | :---: | :---:  | :---:  | :---:  |
| Zhang et al. (2015) \[[9]\]      | Crowd CNN                                                   | 32.0  | 49.8  | N/A    | N/A    | N/A    |
| Zhang et al. (2016) \[[10]\]     | MCNN                                                        | 26.4  | 41.3  | N/A    | N/A    | N/A    |
| Sam et al. (2017) \[[11]\]       | Switching CNN                                               | 21.6  | 33.4  | N/A    | N/A    | N/A    |
| Sindagi et al. (2017) \[[12]\]   | CP-CNN                                                      | 20.1  | 30.1  | N/A    | N/A    | N/A    |
| Ranjan et al. (2018) \[[13]\]    | ic-CNN (one stage)                                          | 10.4  | 16.70 | N/A    | N/A    | N/A    |
| Ranjan et al. (2018) \[[13]\]    | ic-CNN (two stages)                                         | 10.7  | 16.00 | N/A    | N/A    | N/A    |
| Olmschenk et al. (2019) \[[14]\] | MUD-i1NN                                                    | 13.4  | 21.4  | N/A    | N/A    | N/A    |
| Mehta and Valloli (2019) \[[15]\]| W-Net                                                       |__6.9__|__10.3__|__N/A__|__N/A__ |__N/A__ |
| Our implementation (without data aug)| ---                                                     | ---   | ---   | ---    | ---    | ---    |
| FCRN-A                           | FCRN-A, MSE loss, full images, 5/20 epochs                  | 52.95 | 74.53 | 19.08% | 23.73% | 42.81% |
| FCRN-A                           | FCRN-A, LogCosh loss, full images, 24/30 epochs             | 19.95 | 33.94 | 11.70% |  4.43% | 16.13% |
| FCRN-A                           | FCRN-A, MSE loss, patches 32 * (128x128), 54/100 epochs     | 21.49 | 34.98 |  9.33% |  8.04% | 17.37% |
| FCRN-A                           | FCRN-A, LogCosh loss, patches 32 * (128x128), 86/100 epochs | 20.81 | 38.11 | 15.44% |  1.38% | 16.82% |
| U-Net                            | U-Net, MSE loss, full images, 47/50 epochs                  | 24.85 | 39.06 | 18.83% |  1.26% | 20.09% |
|`U-Net`                           |`U-Net, LogCosh loss, full images, 31/50 epochs`             |`19.68`|`35.41`|`14.00%`| `1.92%`|`15.92%`|
| U-Net                            | U-Net, MSE loss, patches 32 * (128x128), 50/50 epochs       | 25.02 | 44.79 | 16.99% |  3.24% | 20.23% |
| U-Net                            | U-Net, LogCosh loss, patches 32 * (128x128), 50/50 epochs   | 27.72 | 45.63 | 22.08% |  0.33% | 22.41% |
| Our implementation (with data aug)| ---                                                        | ---   | ---   | ---    | ---    | ---    |
| FCRN-A                           | FCRN-A, MSE loss, full images, 41/50 epochs                 | 20.21 | 30.97 |  7.45% |  8.89% | 16.34% |
| FCRN-A                           | FCRN-A, LogCosh loss, full images, 25/50 epochs             | 19.31 | 31.82 | 10.16% |  5.45% | 15.61% |
| FCRN-A                           | FCRN-A, MSE loss, patches 16 * (256x256), 48/50 epochs      | 19.03 | 32.80 | 12.66% |  2.72% | 15.38% |
| FCRN-A                           | FCRN-A, LogCosh loss, patches 16 * (256x256), 48/50 epochs  | 15.49 | 27.88 |  8.87% |  3.65% | 12.52% |
| U-Net                            | U-Net, MSE loss, full images, 36/50 epochs                  | 17.64 | 28.62 |  7.92% |  6.34% | 14.26% |
| U-Net                            | U-Net, LogCosh loss, full images, 29/50 epochs              | 15.88 | 26.11 |  8.42% |  4.42% | 12.84% |
| U-Net                            | U-Net, MSE loss, patches 16 * (256x256), 44/50 epochs       | 18.46 | 30.63 | 10.27% |  4.65% | 14.92% |
|`U-Net`                           |`U-Net, LogCosh loss, patches 16 * (256x256), 50/50 epochs`  |`15.20`|`26.49`| `7.37%`| `4.92%`|`12.29%`|
| SegRegNet, density_map           | SegRegNet, LogCosh loss, patches 16 * (256x256)             | 18.94 | 30.79 | 10.10% |  5.21% | 15.31% |
| SegRegNet, density_map*(seg>1e-3)| SegRegNet, LogCosh loss, patches 16 * (256x256)             | 18.83 | 30.71 |  9.79% |  5.43% | 15.22% |

## Qualitative results (1_FCRN-A, MSE loss)
![fcrn_a_vgg_cells_qualitative_results](./images/fcrn_a_vgg_cells_qualitative_results_full_and_patches.png)  
![fcrn_a_carpk_qualitative_results](./images/fcrn_a_carpk_qualitative_results_full_and_patches.png)  
![fcrn_a_shanghai_tech_b_qualitative_results](./images/fcrn_a_shanghai_tech_b_qualitative_results_full_and_patches.png)  

[1]: https://www.robots.ox.ac.uk/~vgg/publications/2010/Lempitsky10b/lempitsky10b.pdf
[2]: https://www.researchgate.net/publication/261130953_Learning_to_count_with_regression_forest_and_structured_labels
[3]: https://www.robots.ox.ac.uk/~vgg/publications/2014/Arteta14/arteta14.pdf
[4]: http://www.robots.ox.ac.uk/~vgg/publications/2016/Xie16/xie16.pdf
[5]: https://arxiv.org/abs/1703.08710
[6]: https://arxiv.org/abs/1707.05972
[7]: https://arxiv.org/abs/1803.05494
[8]: https://arxiv.org/abs/1805.11123
[9]: http://www.ee.cuhk.edu.hk/~xgwang/papers/zhangLWYcvpr15.pdf
[10]: http://openaccess.thecvf.com/content_cvpr_2016/papers/Zhang_Single-Image_Crowd_Counting_CVPR_2016_paper.pdf
[11]: https://arxiv.org/abs/1708.00199
[12]: https://arxiv.org/abs/1708.00953
[13]: https://arxiv.org/abs/1807.09959
[14]: https://arxiv.org/abs/1902.05379
[15]: https://arxiv.org/abs/1903.11249

