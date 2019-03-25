### experiments ###
ARCHITECTURE_NAME = 'FCRN_A'
DATASET_NAME = 'VGG_CELLS'
SUB_EXPERIMENT_NAME = f'{DATASET_NAME.lower()}/n_32_sigma_5_randseed_325_loss_mse_full_img'
DATASET_PATH = f'../../datasets/{DATASET_NAME.lower()}'
TRAIN_PATH = f'{DATASET_PATH}/train'
VAL_PATH = f'{DATASET_PATH}/val'
TEST_PATH = f'{DATASET_PATH}/test'
TRAIN_GT_COUNT_PATH = f'{TRAIN_PATH}/gt_counts'
VAL_GT_COUNT_PATH = f'{VAL_PATH}/gt_counts'
TEST_GT_COUNT_PATH = f'{TEST_PATH}/gt_counts'
CHECKPOINTS_PATH = f'./{SUB_EXPERIMENT_NAME}/checkpoints'
CHECKPOINT_FILENAME = f'{CHECKPOINTS_PATH}/best_model.hdf5'
QUALITATIVE_RESULTS_PATH = f'./{SUB_EXPERIMENT_NAME}/results/qualitative'
QUANTITATIVE_RESULTS_PATH = f'./{SUB_EXPERIMENT_NAME}/results/quantitative'
LOGS_PATH = f'./{SUB_EXPERIMENT_NAME}/logs/'
LOGS_FILENAME = f'{LOGS_PATH}/logs.json'

### create validation split from initial train data ###
VGG_CELLS_RAND_SEED = 325
VGG_CELLS_N = 32 # num of train images for current experiments
VGG_CELLS_VAL_SIZE = 100 - VGG_CELLS_N
CARPK_RAND_SEED = 128
CARPK_VAL_SIZE = 128
SHANGHAI_TECH_PART_B_RAND_SEED = 64
SHANGHAI_TECH_PART_B_VAL_SIZE = 64

RAND_SEED = VGG_CELLS_RAND_SEED
VAL_SIZE = VGG_CELLS_VAL_SIZE
if DATASET_NAME.lower() == 'carpk':
    RAND_SEED = CARPK_RAND_SEED
    VAL_SIZE = CARPK_VAL_SIZE
elif DATASET_NAME.lower() == 'shanghai_tech/part_b':
    RAND_SEED = SHANGHAI_TECH_PART_B_RAND_SEED
    VAL_SIZE = SHANGHAI_TECH_PART_B_VAL_SIZE

### train ###
LOSS_NAME = 'mean_squared_error'
DIM = (256, 256, 3)  # VGG Cells
#DIM = (768, 1024, 3) # ShanghaiTech
#DIM = (720, 1280, 3) # CARPK
BATCH_SIZE = 32
EPOCHS = 75
SHUFFLE = True

### ground truth ###
# sigma for density map generation 
SIGMA = 5
VGG_CELLS_SIGMA = SIGMA
CARPK_SIGMA = SIGMA
SHANGHAI_TECH_PART_B_SIGMA = SIGMA

GT_SIGMA = VGG_CELLS_SIGMA
if DATASET_NAME.lower() == 'carpk':
    GT_SIGMA = CARPK_SIGMA
elif DATASET_NAME.lower() == 'shanghai_tech/part_b':
    GT_SIGMA = SHANGHAI_TECH_PART_B_SIGMA
    
DENSITY_MAP_MULTIPLICATION_FACTOR = 100.