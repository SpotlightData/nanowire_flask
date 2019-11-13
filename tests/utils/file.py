import os

directory = os.path.dirname(os.path.realpath(__file__))


def lfile(name):
    return os.path.join(directory, '../files', name)
