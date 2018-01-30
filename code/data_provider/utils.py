from .cifar import Cifar10DataProvider, Cifar100DataProvider, \
    Cifar10AugmentedDataProvider, Cifar100AugmentedDataProvider, TinyDataProvider
from .svhn import SVHNDataProvider
import os

def get_data_provider_by_name(name, train_params):
    """Return required data provider class"""
    if name == 'C10':
        return Cifar10DataProvider(**train_params)
    if name == 'C10+':
        return Cifar10AugmentedDataProvider(**train_params)
    if name == 'C100':
        return Cifar100DataProvider(**train_params)
    if name == 'C100+':
        return Cifar100AugmentedDataProvider(**train_params)
    if name == 'SVHN':
        return SVHNDataProvider(**train_params)
    if name == 'tiny':
        return TinyDataProvider(**train_params)
    else:
        print("Sorry, data provider for `%s` dataset "
              "was not implemented yet" % name)
        exit()


def remove(path):
    if os.path.exists(path):
        os.remove(path)

def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def removedirs(path):
    import shutil
    if os.path.exists(path):
        shutil.rmtree(path)