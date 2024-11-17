#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  17 2024

@author: Shane R. Mangold
"""

import pandas as pd
import numpy as np
from src.static import DATA_DIR

# read in data
mapped_data = pd.read_csv(f'{DATA_DIR}/mapped_data.csv', na_values = ['.', 'NaN', 'None'])
mapped_data.sort_values(by = ['year', 'enterprise_flag', 'record_number'], inplace = True)
mapped_data = mapped_data[mapped_data.year >= (2023 - 5)]

# one hot encode certain columns
df = pd.get_dummies(mapped_data, columns=['num_bedrooms', 'affordability_level'])

# refine column names
df.columns = df.columns.str.strip()

# define a helper function
def unit_count_transformer(df: pd.core.frame.DataFrame, cols=list[str]) -> pd.core.DataFrame:
    '''
    map unit counts to certain columns. needs at least one column named `num_units` which is the
        target of the transformation. i.e., values from `num_units` are mapped to columns in `cols`
        arg.
    arguments:
        df: a dataframe of data needing to be transformed
        cols: a list of specific column names that need to be worked on
    returns: 
        a transformed dataframe
    '''
    # first create a copy so we arent working on the input dataframe
    output = df.copy()
    for col in cols:
        # map the number of units in each loan record to the value of each input column
        output[col] = output.index.map(
            lambda x: output.loc[x]['num_units'] if output[col].loc[x] else 0
            )
    return output

# map the unit count over certain column values to prepare for aggregation
df = unit_count_transformer(
    df, ['num_bedrooms_0-1', 'num_bedrooms_>=2', 'affordability_level_>100%',
         'affordability_level_>50, <=60%', 'affordability_level_>60, <=80%',
         'affordability_level_>80, <=100%', 'affordability_level_>=0, <=50%']
        )

# this multistage grouping and aggregation creates 1 record with counts of units in certain columns
df = df.groupby(
    # define grouping columns for record grouping
    ['year', 'enterprise_flag', 'record_number', 'census_tract_2020', 'tract_income_ratio',
     'date_of_morgage_note', 'purpose_of_loan', 'type_of_seller', 'federal_guarantee',
     'tenant_income_ind', 'affordability_cat', 'tot_num_units']
    # this next step identifies which columns we're going to sum up
    )[['num_units', 'num_bedrooms_0-1', 'num_bedrooms_>=2', 'affordability_level_>100%',
       'affordability_level_>50, <=60%', 'affordability_level_>60, <=80%',
       'affordability_level_>80, <=100%', 'affordability_level_>=0, <=50%']].agg('sum').reset_index()

print('Data aggregation yields a DataFrame containing aggregate counts of certain categories ',
      df.head())

# finally prepare remaining categorical columns for modeling by finishing one hot encoding
df = pd.get_dummies(
    df,
    columns=['census_tract_2020', 'tract_income_ratio', 'date_of_mortgage_note',
             'purpose_of_loan', 'type_of_seller', 'federal_guarantee', 'tenant_income_ind',
             'affordability_cat', 'tot_num_units'],
    drop_first=True
    )

# save engineered data
df.to_csv(f'{DATA_DIR}/preprocessed_data.csv')
## End script
