#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def corr_ratio(df):
    """Compute correlation ratio between categorical and numerical data.

    Argument:
      df (DataFrame): DataFrame object containing categorical values as 
                      columns and numerical values as rows

    Return:
      ratio (np.float64): correlation ratio
    """
    # in-class variance
    ssw = ((df - df.mean()) ** 2).sum().sum()
    # inter-class variance
    ssb = (df.count() * ((df.mean() - np.nanmean(df)) ** 2)).sum()
    # correlation ratio
    ratio = ssb / (ssb + ssw)
    return ratio
