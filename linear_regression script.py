# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 17:38:35 2024

@author: apaige
"""

 # Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os

# Step 1: Load your dataset from Excel
file_path = os.path.expanduser('C:/Users/apaige/Downloads/preprocessed_data.xlsx')
df = pd.read_excel(file_path)


# Option 1: Drop rows with missing values
df = df.dropna()

# Step 3: One-hot encode True/False columns and categorical variables
# Use get_dummies to convert categorical columns to dummy variables
df = pd.get_dummies(df, drop_first=True)

# Step 4: Select your target variable
target = 'num_affordable_units'  # Example target column (update this as needed)

# Step 5: Define your independent variables (features)
# You can manually select features or use all columns except the target
features = df.drop(columns=[target])

# Step 6: Split the data into training and testing sets (80% train, 20% test)
X = features
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Standardize the features (optional but recommended)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 8: Fit a linear regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Step 9: Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Step 10: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation results
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
