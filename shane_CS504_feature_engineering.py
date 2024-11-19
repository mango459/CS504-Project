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
mapped_data = mapped_data[mapped_data.year > (2023 - 5)]

# one hot encode certain columns
df = pd.get_dummies(mapped_data, columns=['num_bedrooms', 'affordability_level'])

# refine column names
df.columns = df.columns.str.strip()

# define a helper function
def unit_count_transformer(df: pd.DataFrame, cols=list[str]) -> pd.DataFrame:
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
     'date_of_mortgage_note', 'purpose_of_loan', 'type_of_seller', 'federal_guarantee',
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
    columns=['enterprise_flag', # 'census_tract_2020', # commented out to leave as a categorical for testing ordinal regressors.
            #  'tract_income_ratio',
             'date_of_mortgage_note',
             'purpose_of_loan', 'type_of_seller', 'federal_guarantee', 'tenant_income_ind',
             # 'affordability_cat', # commented out to leave as a categorical for testing ordinal regressors.
             'tot_num_units']
    )

census_tract_2020 = {'<10%': '1', '>=10%, <30%': '2', '>=30% <100%': '3', 'NaN': '9'}
affordability_cat = {'>=20%, <40%': '1', '<20%, >=40%': '2', '>=20%, >=40%': '3',
                      '<20%, <40%': '4'}
tract_income_ratio, = {'>0, <=80%': '1', '>10, <=120%': '2', '>120%': '3'},

# remap ordinal values over the string values for modeling
df.census_tract_2020 = df.census_tract_2020.map(lambda x: census_tract_2020.get(x))
df.affordability_cat = df.affordability_cat.map(lambda x: affordability_cat.get(x))
df.tract_income_ratio = df.tract_income_ratio.map(lambda x: tract_income_ratio.get(x))

# create simple flag to tell the model about covid
df['after_covid_ind'] = df.year >= 2020
df.columns = df.columns.str.strip().str.replace(' - ', '-')

# create simple count of number of affordable units so that a predictor can predict the number of
# affordabile units based on other inputs.
df['num_affordable_units'] = df[['affordability_level_>=0, <=50%', 'affordability_level_>50, <=60%',
                                 'affordability_level_>60, <=80%']].sum(axis=1)

# save engineered data
df.to_csv(f'{DATA_DIR}/preprocessed_data.csv', index=False)
## End script
