#! /usr/bin/env python3
# coding: utf-8

"""
Feature selection using various techniques
"""

import pandas as pd

from sklearn.feature_selection import SelectKBest, f_regression
from modules.wrangle import E_DATAFRAME as df

ALL_FEATURES = ['id', 'description', 'host_since', 'host_is_superhost',
                'host_listings_count', 'host_verifications', 'host_has_profile_pic',
                'host_identity_verified', 'neighbourhood_cleansed', 'zipcode',
                'property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms',
                'beds', 'bed_type', 'amenities', 'guests_included', 'extra_people',
                'minimum_nights', 'number_of_reviews', 'review_scores_rating', 'instant_bookable',
                'reviews_per_month']
dummy = pd.get_dummies(df['neighbourhood_cleansed'])


def f_test():
    selector = SelectKBest(f_regression)
    selector.fit(dummy, df['price'])
    return selector


if __name__ == '__main__':
    _THRESHOLD = 0.001

    neighbourhoods = dummy.columns
    significance = f_test().pvalues_
    print(neighbourhoods[significance <= _THRESHOLD])
