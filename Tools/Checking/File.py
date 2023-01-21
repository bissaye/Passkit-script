import os

__all__ = ['check_if_path_exists']

def check_if_path_exists(path):
    return os.path.exists(path)