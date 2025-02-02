# -*- coding: utf-8 -*-
"""linear regression and logistic regression

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cY9mDaWqOJwQdG0K2Q5N168-02ta28sd
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

diabetes_data=pd.read_csv('/content/sample_data/diabetes.csv')
diabetes_data.head()

diabetes_data=pd.read_csv('/content/sample_data/diabetes.csv')
diabetes_data.tail()

diabetes_data.describe().T

diabetes_data.info()

diabetes_data.hist(figsize=(20,20))

from pandas.plotting import scatter_matrix
scatter_matrix(diabetes_data,figsize=(25,25))

"""# New section"""

sns.heatmap(diabetes_data.corr(), annot=True, cmap='RdYlGn')

sns.heatmap(diabetes_data_copy.corr(), annot=True, cmap='RdYlGn')

from sklearn.preprocessing import StandardScaler
std_scaler=StandardScaler()
X =  pd.DataFrame(std_scaler.fit_transform(diabetes_data_copy.drop(["Outcome"],axis = 1),),
        columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age'])
y=diabetes_data_copy['Outcome']
X.head()

plt.figure(figsize=(12,5))
p = sns.lineplot(train_scores,marker='*',label='Train Score')
p = sns.lineplot(test_scores,marker='o',label='Test Score')

# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix, classification_report

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

# Convert to a pandas DataFrame for easier manipulation
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = pd.Series(diabetes.target)

# Split the data for linear regression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Predict using the test set
y_pred_linear = linear_model.predict(X_test)

# Evaluate the Linear Regression model
mse = mean_squared_error(y_test, y_pred_linear)
print("Mean Squared Error (Linear Regression):", mse)

# Plot the Linear Regression results
plt.scatter(y_test, y_pred_linear)
plt.xlabel("True Values")
plt.ylabel("Predicted Values")
plt.title("Linear Regression: True vs Predicted")
plt.show()

# Binary Classification (for logistic regression)
# Assume we create a binary target for classification
# For example, predict whether the diabetes progression value is above the median (1) or below (0)
y_binary = (y > np.median(y)).astype(int)

# Split the data for logistic regression
X_train_log, X_test_log, y_train_log, y_test_log = train_test_split(X, y_binary, test_size=0.2, random_state=42)

# Train the Logistic Regression model
logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(X_train_log, y_train_log)

# Predict using the test set
y_pred_logistic = logistic_model.predict(X_test_log)

# Evaluate the Logistic Regression model
accuracy = accuracy_score(y_test_log, y_pred_logistic)
print("Accuracy (Logistic Regression):", accuracy)

# Confusion matrix and classification report
print("Confusion Matrix:\n", confusion_matrix(y_test_log, y_pred_logistic))
print("Classification Report:\n", classification_report(y_test_log, y_pred_logistic))

# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

# Step 2: Load the diabetes dataset
path = '/content/sample_data/diabetes.csv'
column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
data = pd.read_csv(url, names=column_names)

# Step 3: Data Exploration
print(data.head())
print(data.describe())
print(data.info())

# Check for missing values
print("Missing values:\n", data.isnull().sum())

# Step 4: Preprocess the data
# Separate features and target
X = data.drop(columns='Outcome')  # Features
y_classification = data['Outcome']  # Target for Logistic Regression (binary)
y_regression = data['Glucose']  # Target for Linear Regression (continuous)

# Standardize the features for Logistic Regression
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into train and test sets
X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X_scaled, y_classification, test_size=0.2, random_state=42)
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_scaled, y_regression, test_size=0.2, random_state=42)

# Step 5: Build and train the models

# 5.1 Linear Regression Model (Predict continuous variable: Glucose level)
lin_reg = LinearRegression()
lin_reg.fit(X_train_reg, y_train_reg)

# 5.2 Logistic Regression Model (Predict binary outcome: Diabetes or not)
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train_class, y_train_class)

# Step 6: Evaluate the models

# 6.1 Evaluate Linear Regression
y_pred_reg = lin_reg.predict(X_test_reg)
mse = mean_squared_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)
print("\nLinear Regression:")
print(f"Mean Squared Error: {mse}")
print(f"R-Squared: {r2}")

# 6.2 Evaluate Logistic Regression
y_pred_class = log_reg.predict(X_test_class)
accuracy = accuracy_score(y_test_class, y_pred_class)
conf_matrix = confusion_matrix(y_test_class, y_pred_class)
class_report = classification_report(y_test_class, y_pred_class)
print("\nLogistic Regression:")
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)

# Optional: Visualize predictions
# Linear Regression: Plot predicted vs actual values
plt.scatter(y_test_reg, y_pred_reg)
plt.xlabel('Actual Glucose Level')
plt.ylabel('Predicted Glucose Level')
plt.title('Linear Regression: Actual vs Predicted')
plt.show()

# Logistic Regression: Confusion matrix heatmap
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Logistic Regression Confusion Matrix')
plt.show()

def linear_regression(x, y):

    if len(x) != len(y):
        raise ValueError("x and y must have the same number of elements.")

    n = len(x)


    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi ** 2 for xi in x)


    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y - m * sum_x) / n


    return m, b


x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

m, b = linear_regression(x, y)

print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")


def predict(x_val, m, b):
    return m * x_val + b


x_val = 6
predicted_y = predict(x_val, m, b)
print(f"Predicted value for x = {x_val}: {predicted_y}")

import os
print(os.listdir('/content'))

import pandas as pd


df = pd.read_csv('/diabetes.csv')

print(df.head())

