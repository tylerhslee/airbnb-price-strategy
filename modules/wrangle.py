#! /usr/bin/env python3
# coding: utf-8

"""
Available data formats:
  - Pandas DataFrame
"""

import os

import numpy as np
import pandas as pd

from datetime import datetime
from modules.datareader import DataReader
from modules.logger import Logger, DEBUG, INFO, WARNING, ERROR, CRITICAL

logfile = os.path.join(Logger.get_logfile_dir(__file__), '..', 'logs', 'wrangle.log')
_ = Logger.create(__file__, logfile, DEBUG)
_.addHandler(Logger.create_file_handler(logfile, DEBUG))
_.addHandler(Logger.create_stream_handler(WARNING))


def make_dataframe(fpath):
	df = pd.read_csv(fpath).dropna(subset=['host_since'])

	# Dates
	df['host_since_days'] = (pd.to_datetime('now') - pd.to_datetime(df['host_since'])).dt.days.astype(int)

	# Booleans
	df['host_is_superhost'] = df['host_is_superhost'] == 't'
	df['host_has_profile_pic'] = df['host_has_profile_pic'] == 't'
	df['host_identity_verified'] = df['host_identity_verified'] == 't'
	df['instant_bookable'] = df['instant_bookable'] == 't'

	# Lists
	df['host_verifications'] = _parse_list_from_str(df['host_verifications'])
	df['amenities'] = _parse_list_from_str(df['amenities'])

	# Currency
	df['price'] = _parse_float_from_currency(df['price'])
	df['extra_people'] = _parse_float_from_currency(df['extra_people'])

	return df


def _parse_list_from_str(col):
	return col.str[1:-1].replace('\'', '').str[1:-1].replace('"', '').str.split(',')


def _parse_float_from_currency(col):
	return col.str.replace(r'\$|,', '').astype(np.float32)


# I hate pathing in Python
CPATH = os.path.dirname(os.path.realpath(__file__))
ROOT = os.path.join(CPATH, '..')

# Exports
E_DATAFRAME = make_dataframe(os.path.join(ROOT, 'data', 'listings_cleaned.csv'))
