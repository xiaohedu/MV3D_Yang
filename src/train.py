import mv3d
import glob
from config import *
import utils.batch_loading as ub
import argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='training')
    parser.add_argument('-w', '--weights', type=str, nargs='?', default='',
        help='use pre trained weigthts example: -w "rpn,fusion" ')
    parser.add_argument('-i', '--max_iter', type=int, nargs='?', default=1000,
                        help='max count of train iter')
    args = parser.parse_args()

    print('\n\n{}\n\n'.format(args))
    max_iter = args.max_iter
    weights=[]
    if args.weights != '':
        weights = args.weights.split(',')

    dataset_dir = cfg.PREPROCESSED_DATA_SETS_DIR

    if cfg.DATA_SETS_TYPE == 'didi':
        training_dataset = {
            '1': ['6_f', '9_f', '10', '13', '20', '21_f', '15', '19'],
            '2': ['3_f', '6_f', '8_f'],
            '3': ['2_f', '4', '6', '8', '7', '11_f']}

        validation_dataset = {
            '1': ['15']}

    elif cfg.DATA_SETS_TYPE == 'kitti':
        training_dataset = {
            '2011_09_26': ['0001', '0017', '0029', '0052', '0070', '0002', '0018', '0056',  '0019',
                       '0036', '0005',
                       '0057', '0084', '0020', '0039', '0086', '0011', '0023', '0046', '0060', '0091']}

        validation_dataset = {
            '2011_09_26': ['0013', '0027', '0048',
                           '0061', '0015', '0028', '0051', '0064']
        }

    training = ub.batch_loading(dataset_dir, training_dataset)

    validation = ub.batch_loading(dataset_dir, validation_dataset)

    train = mv3d.Trainer(train_set=training, validation_set=validation, pre_trained_weights=weights)

    train(max_iter=max_iter)


