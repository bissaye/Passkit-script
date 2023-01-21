import logging

__all__ = ['info', 'error']

def info(msg):
    logging.warn(msg)

def error(msg):
    logging.error(msg)
