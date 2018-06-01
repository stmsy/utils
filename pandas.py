#!/usr/bin/env python

import pandas as pd


def categorize_df(df, target, predictor):
    """Categorize the DataFrame object so that column represents the values of 
    predictor (categorical) with entries from target values (numerical)

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
