### experiments ###
ARCHITECTURE_NAME = 'FCRN_A'
DATASET_NAME = 'shanghai_tech/part_b'
SUB_EXPERIMENT_NAME = f'{DATASET_NAME.lower()}/sigma_10_loss_logcosh_full_img_epochs_50_lr_1e-4'
DATASET_PATH = f'../../datasets/{DATASET_NAME.lower()}'
TRAIN_PATH = f'{DATASET_PATH}/train'
VAL_PATH = f'{DATASET_PATH}/val'
TEST_PATH = f'{DATASET_PATH}/test'
TRAIN_GT_COUNT_PATH = f'{TRAIN_PATH}/gt_counts'
VAL_GT_COUNT_PATH = f'{VAL_PATH}/gt_counts'
TEST_GT_COUNT_PATH = f'{TEST_PATH}/gt_counts'
CHECKPOINTS_PATH = f'./{SUB_EXPERIMENT_NAME}/checkpoints'
CHECKPOINT_FILENAME = f'{CHECKPOINTS_PATH}/' + 'model.{epoch:02d}-{val_loss:.3f}.hdf5'
#QUALITATIVE_RESULTS_PATH = f'./{SUB_EXPERIMENT_NAME}/results/qualitative'
#QUANTITATIVE_RESULTS_PATH = './{SUB_EXPERIMENT_NAME}/results/quantitative_epoch_{epoch:02d}'
LOGS_PATH = f'./{SUB_EXPERIMENT_NAME}/logs/'
LOGS_FILENAME = f'{LOGS_PATH}/logs.json'

### create validation split from initial train data ###
VGG_CELLS_RAND_SEED = 645
VGG_CELLS_N = 64 # num of train images for vgg_cells experiments
VGG_CELLS_VAL_SIZE = 100 - VGG_CELLS_N
CARPK_RAND_SEED = 9001
CARPK_N = 900 # num of train images for carpk experiments
CARPK_VAL_SIZE = 989 - CARPK_N
SHANGHAI_TECH_PART_B_RAND_SEED = 3201
SHANGHAI_TECH_PART_B_N = 320 # num of train images for shanghai_tech/part_b experiments
SHANGHAI_TECH_PART_B_VAL_SIZE = 400 - SHANGHAI_TECH_PART_B_N

RAND_SEED = VGG_CELLS_RAND_SEED
VAL_SIZE = VGG_CELLS_VAL_SIZE
if DATASET_NAME.lower() == 'carpk':
    RAND_SEED = CARPK_RAND_SEED
    VAL_SIZE = CARPK_VAL_SIZE
elif DATASET_NAME.lower() == 'shanghai_tech/part_b':
    RAND_SEED = SHANGHAI_TECH_PART_B_RAND_SEED
    VAL_SIZE = SHANGHAI_TECH_PART_B_VAL_SIZE

### train ###
LOSS_NAME = 'logcosh'
LEARNING_RATE = 1e-4

IMG_DIM = None
if DATASET_NAME.lower() == 'vgg_cells':
    IMG_DIM = (256, 256, 3) # VGG Cells
elif DATASET_NAME.lower() == 'carpk':
    IMG_DIM = (720, 1280, 3) # CARPK
elif DATASET_NAME.lower() == 'shanghai_tech/part_b':
    IMG_DIM = (768, 1024, 3) # ShanghaiTech
        
PATCH_DIM = IMG_DIM
PATCHES_PER_IMAGE = 1
BATCH_SIZE = 1
EPOCHS = 50
SHUFFLE = True

### ground truth ###
# sigma for density map generation
VGG_CELLS_SIGMA = 5
CARPK_SIGMA = 10
SHANGHAI_TECH_PART_B_SIGMA = 10

GT_SIGMA = None
if DATASET_NAME.lower() == 'vgg_cells':
    GT_SIGMA = VGG_CELLS_SIGMA
elif DATASET_NAME.lower() == 'carpk':
    GT_SIGMA = CARPK_SIGMA
elif DATASET_NAME.lower() == 'shanghai_tech/part_b':
    GT_SIGMA = SHANGHAI_TECH_PART_B_SIGMA
    
DENSITY_MAP_MULTIPLICATION_FACTOR = None
if DATASET_NAME.lower() == 'vgg_cells':
    DENSITY_MAP_MULTIPLICATION_FACTOR = 100.
elif DATASET_NAME.lower() == 'carpk':
    DENSITY_MAP_MULTIPLICATION_FACTOR = 2000.
elif DATASET_NAME.lower() == 'shanghai_tech/part_b':
    DENSITY_MAP_MULTIPLICATION_FACTOR = 2000.
    
# ignore some train images with ground truth inconsistencies #
IGNORED_IMAGES = []
if DATASET_NAME.lower() == 'shanghai_tech/part_b':
    IGNORED_IMAGES = ['IMG_108_00', 'IMG_108_01', 'IMG_108_02', 'IMG_108_03']