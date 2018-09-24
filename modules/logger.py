# coding: utf-8

import logging
import os

from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL


class Logger(object):

    _FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    @staticmethod
    def get_logfile_dir(name):
        return os.path.dirname(os.path.realpath(name))

    @staticmethod
    def create(name, fpath, loglevel, create_handler=False):
        logger = logging.getLogger(name)
        logger.setLevel(loglevel)

        if create_handler:
            handler = logging.FileHandler(fpath)
            handler.setLevel(flevel)
            handler.setFormatter(Logger._FORMAT)
            logger.addHandler(handler)

        return logger
    
    @staticmethod
    def create_file_handler(fpath, level):
        handler = logging.FileHandler(fpath)
        handler.setLevel(level)
        handler.setFormatter(Logger._FORMAT)
        return handler

    @staticmethod
    def create_stream_handler(level):
        handler = logging.StreamHandler()
        handler.setLevel(level)
        handler.setFormatter(Logger._FORMAT)
        return handler

