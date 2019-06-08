#!/usr/bin/env python

import numpy as np
import pandas as pd


def corr_ratio(df: pd.DataFrame) -> np.float64:
    """Compute correlation ratio between categorical and numerical data.

    Argument:
      df: DataFrame object containing categorical values as columns and
          numerical values as rows

    Return:
      ratio: correlation ratio
    """
    # in-class variance
    ssw = ((df - df.mean()) ** 2).sum().sum()
    # inter-class variance
    ssb = (df.count() * ((df.mean() - np.nanmean(df)) ** 2)).sum()
    # correlation ratio
    ratio = ssb / (ssb + ssw)
    return ratio
