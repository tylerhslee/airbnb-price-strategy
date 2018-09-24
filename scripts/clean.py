#! /usr/bin/env python3
# coding: utf-8

"""
Run the script to clean the raw listings data.
"""

import csv
import os

import numpy as np
import pandas as pd

from modules.datareader import DataReader
from modules.logger import Logger, DEBUG, INFO, WARNING, ERROR, CRITICAL
from modules.exceptions import ColumnNotFoundException

logfile = os.path.join(Logger.get_logfile_dir(__file__), 'logs', 'clean.log')
_ = Logger.create(__file__, logfile, DEBUG)
_.addHandler(Logger.create_file_handler(logfile, DEBUG))
_.addHandler(Logger.create_stream_handler(WARNING))

if __name__ == '__main__':
    _.info('Cleaning data...')
    data_reader = DataReader('./data/listings.csv')

    try:
        data_reader.filter_columns('id', 'description', 'host_since', 'host_is_superhost',
                'host_listings_count', 'host_verifications', 'host_has_profile_pic',
                'host_identity_verified', 'neighbourhood_cleansed', 'zipcode',
                'property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms',
                'beds', 'bed_type', 'amenities', 'price', 'guests_included', 'extra_people',
                'minimum_nights', 'number_of_reviews', 'review_scores_rating', 'instant_bookable',
                'reviews_per_month')

        output = './data/listings_cleaned.csv'
        _.info('Writing to %s' % output)
        data_reader.write(output)
    except ColumnNotFoundException as e:
        _.exception(e)
    except Exception as e:
        _.exception(e)

