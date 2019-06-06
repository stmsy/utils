#!/usr/bin/env python

import pandas as pd


def categorize_df(df, target, predictor):
    """Categorize the DataFrame object so that column represents the values of
    predictor (categorical) with entries from target values (numerical).

    Arguments:
      df (pandas.DataFrame): the DataFrame object containing categorical
                             values as columns and numerical values as rows
      target (str): target variable whose values fill the entries of the
                    DataFrame object
      predictor (str): predictor variable whose values correspond to the
                       column names

    Return:
      df_cated (pandas.DataFrame): the DataFrame object with predictor values
                                   as column names and
    """
    df_groupby = df.copy().groupby(predictor)[target].apply(
        lambda df: df.reset_index(drop=True)).unstack()
    df_cated = pd.DataFrame()
    columns = df_groupby.index
    for column in columns:
        df_cated[column] = df_groupby.loc[column]
    return df_cated


def get_num_nan_rows(df):
    """"Get the number of rows filled with missing values.

    Argument:
      df (pandas.DataFrame): the DataFrame object to get the number of rows
                             filled with missing values
    Return:
      _ (int): the number of rows filled with missing values
    """
    return df.isna().all(axis=1).sum()


def is_na_contained(df):
    """Check whether the DataFrame object contains a missing value.

    Argument:
      df (pandas.DataFrame): the DataFrame object to be checked whether it
                             contains a missing value

    Return:
      True/False (boolean): True if the DataFrame object contains at least
                            one missing value, False elsewhere
    """
    return any(df.isna().any().values)


def are_na_contained(df):
    """Check whether the columns of the DataFrame object contain missing the 
    values.

    Arguement:
      df (pandas.DataFrame): the DataFrame object to be checked whether its
                             columns contain the missing values

    Return:
      sr_na_test_results (pandas.Series): the Series object whose values are
                                          True or False depending on the
                                          missing value test
    """
    sr_na_test_results = df.isna().any()
    return sr_na_test_results
