#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 9 16:48:53 2024

@author: andreapaloschavez
"""

import pandas as pd

data_path = '/Users/andreapaloschavez/Library/CloudStorage/OneDrive-Avantus/CS504/python/raw_19-23.csv'
csv = pd.read_csv(data_path)
df = pd.DataFrame(csv)

# Check the first few rows of the CSV data
df.head()

# Check the data types and missing values in the data
df_csv_info = df.info()

# Check the percentage of missing values per column
missing_values = df.isnull().mean() * 100
df_csv_info, missing_values

# We find that the 'underserved_areas_ind' column is entirely null
# so we drop it from the dataset
df.drop('underserved_areas_ind', axis=1, inplace=True)

# Check the last few rows of the data
df.tail()

# The columns with numerical data (like num_units, num_bedrooms, 
# and tract_income_ratio) seem like potential candidates for 
# independent variables in a linear regression model. 
# However, we need to ensure that these variables are 
# continuous and not categorical.


# Update target variable to 'tract_income_ratio'
target_variable = 'tract_income_ratio'
independent_variables = ['num_bedrooms', 'num_units', 'tract_income_ratio', #<- data leakage here in target variables
                          'tot_num_units']

# Check the correlation between the target variable and independent variables
correlation_matrix = df[independent_variables + [target_variable]].corr()

correlation_matrix

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Prepare the data for regression
X = df[independent_variables]  # Independent variables
y = df[target_variable]  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate performance metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

mse, r2
# MSE is an extremely small value, essentially close to zero. 
# It indicates that the model's predictions are almost identical to the 
# actual values in the test set. 
# overfitting or perfect collinearity between features and the target?

# R2 -- model explains 100% of the variance in the target variab,
# a high correlation between the independent variables and the target
