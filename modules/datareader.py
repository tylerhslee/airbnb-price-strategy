# coding: utf-8
import csv
import os

import numpy as np
import pandas as pd

from modules.logger import Logger, DEBUG, INFO, WARNING, ERROR, CRITICAL
from modules.exceptions import ColumnNotFoundException

logfile = os.path.join(Logger.get_logfile_dir(__file__), '..', 'logs', 'datareader.log')
_ = Logger.create(__file__, logfile, DEBUG)
_.addHandler(Logger.create_file_handler(logfile, DEBUG))
_.addHandler(Logger.create_stream_handler(WARNING))


class DataReader(object):
    """
    Reads the CSV data file then cleans it
    """

    def __init__(self, fname, delim=","):
        self.delim = delim
        
        self.header = []
        self.data = []
        self.rows = 0
        self.cols = 0

        _.debug("Reading %s" % fname) 
        with open(fname, 'r') as rf:
            reader = csv.reader(rf, delimiter=delim)
            self.header = next(reader)
            self.cols = len(self.data)
            for row in reader:
                self.data.append(row)
                self.rows += 1
        self.data = np.array(self.data)

    def __str__(self):
        return "(%d, %d)" % (self.cols, self.rows)

    def __repr__(self):
        return self.__str__()
    
    def filter_columns(self, *args):
        _.debug("Filtering columns: %s" % ", ".join(args))
        colnames = np.array(args)
        columns_exist = self._test_all_columns_exist(colnames)
        if not np.all(columns_exist):
            raise ColumnNotFoundException(colnames[~columns_exist])
            
        cols_interest = np.in1d(self.header, np.array(args))
        # self.data = self.data[:, np.where(cols_interest)]
        self.data = self.data[:, cols_interest]
        self.header = colnames

    def _test_all_columns_exist(self, colnames):
        return np.in1d(colnames, self.header)

    def write(self, output, delim=","):
        writer = csv.writer(open(output, 'w'))
        writer.writerow(self.header)
        for row in self.data:
            writer.writerow(row)
