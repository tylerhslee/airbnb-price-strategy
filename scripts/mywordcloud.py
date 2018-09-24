#! /usr/bin/env python3
# coding: utf-8

"""
Generate wordcloud of the listing descriptions
"""

import matplotlib
matplotlib.use('PS')    # For Mac OSX
import numpy as np

from wordcloud import WordCloud, STOPWORDS
from modules.wrangle import E_DATAFRAME

text = E_DATAFRAME['description'].str.cat(sep='\n')
wc = WordCloud(background_color='white', max_words=100, stopwords=set(STOPWORDS), contour_width=3, contour_color='steelblue')

wc.generate(text)
wc.to_file('./data/wc.png')
