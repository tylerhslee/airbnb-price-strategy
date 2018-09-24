# coding: utf-8

class ColumnNotFoundException(Exception):

    def __init__(self, colnames):
        msg = 'Column names %s do not exist.' % ', '.join(colnames)
        super(ColumnNotFoundException, self).__init__(msg)

