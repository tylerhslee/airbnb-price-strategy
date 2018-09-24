#! /usr/bin/env python3
# coding: utf-8

"""
Unit test script for modules/wrangle.py
"""

import unittest

import numpy as np

from datetime import datetime
from modules.wrangle import E_DATAFRAME as df


class TestWrangle(unittest.TestCase):

	def test_make_dataframe(self):
		# Datetime
		self.assertTrue(isinstance(df['host_since_days'][0], np.int64))

		# Boolean
		self.assertTrue(df['host_is_superhost'].dtype == np.bool_)
		self.assertTrue(df['host_has_profile_pic'].dtype == np.bool_)
		self.assertTrue(df['host_identity_verified'].dtype == np.bool_)
		self.assertTrue(df['instant_bookable'].dtype == np.bool_)

		# List
		self.assertTrue(len(df['host_verifications'][0]) == 5)
		self.assertTrue(len(df['amenities'][0]) == 8)

		# Currency
		self.assertTrue(int(df['price'][0]) == 275)
		self.assertTrue(int(df['extra_people'][0]) == 99)


if __name__ == '__main__':
	unittest.main()
