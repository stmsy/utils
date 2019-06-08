#!/usr/bin/env python

import pandas as pd


def categorize_df(df: pd.DataFrame, target: str,
                  predictor: str) -> pd.DataFrame:
    """Categorize the DataFrame object so that column represents the values of
    predictor (categorical) with entries from target values (numerical).

    Arguments:
      df: the DataFrame object containing categorical values as columns and
          numerical values as rows
      target: target variable whose values fill the entries of the DataFrame
              object
      predictor: predictor variable whose values correspond to the column names

    Return:
      df_cated: the DataFrame object with predictor values as column names and
                target values as its entries
    """
    df_groupby = df.copy().groupby(predictor)[target].apply(
        lambda df: df.reset_index(drop=True)).unstack()
    df_cated = pd.DataFrame()
    columns = df_groupby.index
    for column in columns:
        df_cated[column] = df_groupby.loc[column]
    return df_cated


def get_num_nan_rows(df: pd.DataFrame) -> int:
    """"Get the number of rows filled with missing values.

    Argument:
      df: the DataFrame object to get the number of rows filled with missing
          values
    Return:
      _: the number of rows filled with missing values
    """
    return df.isna().all(axis=1).sum()


def is_na_contained(df: pd.DataFrame) -> bool:
    """Check whether the DataFrame object contains a missing value.

    Argument:
      df: the DataFrame object to be checked whether it contains a missing
          value

    Return:
      True/False: True if the DataFrame object contains at least one missing
                  value, False elsewhere
    """
    return any(df.isna().any().values)


def are_na_contained(df: pd.DataFrame) -> pd.Series:
    """Check whether the columns of the DataFrame object contain missing the
    values.

    Arguement:
      df: the DataFrame object to be checked whether its columns contain the
           missing values

    Return:
      sr_na_test_results: the Series object whose values are True or False
                          depending on the missing value test
    """
    sr_na_test_results = df.isna().any()
    return sr_na_test_results
