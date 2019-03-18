### experiments ###
SUB_EXPERIMENT_NAME = 'vgg_cells_test_1'
DATASET_PATH = '../../datasets/vgg_cells'
VAL_PATH = f'{DATASET_PATH}/test'
CHECKPOINTS_PATH = f'./{SUB_EXPERIMENT_NAME}/checkpoints'
QUALITATIVE_RESULTS_PATH = f'./{SUB_EXPERIMENT_NAME}/results/qualitative'
QUANTITATIVE_RESULTS_PATH = f'./{SUB_EXPERIMENT_NAME}/results/quantitative'
LOGS_PATH = f'./{SUB_EXPERIMENT_NAME}/logs/'
LOGS_FILENAME = f'{LOGS_PATH}/logs.json'

### train ###
DIM = (256, 256, 3)
BATCH_SIZE = 32
EPOCHS = 25
SHUFFLE = True

### ground truth ###
# sigma for density map generation 
SIGMA = 5
VGG_CELLS_SIGMA = SIGMA
CARPK_SIGMA = SIGMA
SHANGHAI_TECH_PART_A_SIGMA = SIGMA
SHANGHAI_TECH_PART_B_SIGMA = SIGMA

DENSITY_MAP_MULTIPLICATION_FACTOR = 100.


