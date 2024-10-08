# -*- coding: utf-8 -*-
"""lr_svm_nb.py
"""

from google.colab import drive
drive.mount('/content/drive')

# 2 Implementation
# 2.2 Tasks

# 1. Prepare dataset

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model,metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import PolynomialFeatures

# Load data
data = pd.read_csv('/content/drive/MyDrive/heart.csv')

# Fill missing values with the median of each column
data_filled = data.fillna(data.median())

# Separate the features and the target variable
X = data_filled.drop('target', axis=1)
y = data_filled['target']

# Adding a column of ones to X to include an intercept in the model
X = np.c_[np.ones(X.shape[0]), X]

# Split the data into training and testing sets (90% training, 10% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# 2. Train a Logistic Regression model (LR)

# Initialize logistic regression model
regr = linear_model.LogisticRegression(fit_intercept=False,max_iter=1000)

# Train a logistic regression model using training sets
regr.fit(X_train, y_train)

# Predicting on training and test datasets
y_pred_train = regr.predict(X_train)
y_pred_test = regr.predict(X_test)

# Calculate accuracy
accuracy_train = accuracy_score(y_train, y_pred_train)
accuracy_test = accuracy_score(y_test, y_pred_test)

# Calculate precision
precision_train = precision_score(y_train, y_pred_train)
precision_test = precision_score(y_test, y_pred_test)

# Compute Confusion Matrix
conf_matrix_train = confusion_matrix(y_train, y_pred_train)
conf_matrix_test = confusion_matrix(y_test, y_pred_test)

# Retrieve the model parameters (theta)
theta = regr.coef_
intercept = regr.intercept_

print("\nLogistic Regression Results:")
print("Training Accuracy:", accuracy_train)
print("Test Accuracy:", accuracy_test)
print("Training Precision:", precision_train)
print("Test Precision:", precision_test)
print("Training Confusion Matrix:\n", conf_matrix_train)
print("Test Confusion Matrix:\n", conf_matrix_test)
print("Intercept:", intercept)
print("Coefficients (Theta):", theta)

# 3. Train a Support Vector Machine Classifier (SVM)

C_values = [1, 10, 20]
kernels = ['linear', 'rbf']

for kernel in kernels:
    print(f"\nSVM with {kernel} kernel:")
    for C in C_values:
        print(f"\nC = {C}")
        svm = SVC(kernel=kernel, C=C, gamma='scale')

        # Train the SVM model using training sets
        svm.fit(X_train, y_train)

        # Predicting on training and test datasets
        y_pred_train_svm = svm.predict(X_train)
        y_pred_test_svm = svm.predict(X_test)

        # Calculate accuracy
        accuracy_train_svm = accuracy_score(y_train, y_pred_train_svm)
        accuracy_test_svm = accuracy_score(y_test, y_pred_test_svm)

        # Calculate precision
        precision_train_svm = precision_score(y_train, y_pred_train_svm)
        precision_test_svm = precision_score(y_test, y_pred_test_svm)

        # Compute Confusion Matrix
        conf_matrix_train_svm = confusion_matrix(y_train, y_pred_train_svm)
        conf_matrix_test_svm = confusion_matrix(y_test, y_pred_test_svm)

        print("Training Accuracy:", accuracy_train_svm)
        print("Test Accuracy:", accuracy_test_svm)
        print("Training Precision:", precision_train_svm)
        print("Test Precision:", precision_test_svm)
        print("Training Confusion Matrix:\n", conf_matrix_train_svm)
        print("Test Confusion Matrix:\n", conf_matrix_test_svm)

# 4. Train a Naive Bayes Classifier (NB)

# Initialize Gaussian Naive Bayes model
gnb = GaussianNB()

# Train a Gaussian Naive Bayes model using training sets
gnb.fit(X_train, y_train)

# Predicting on training and test datasets
y_pred_train_nb = gnb.predict(X_train)
y_pred_test_nb = gnb.predict(X_test)

# Calculate accuracy
accuracy_train_nb = accuracy_score(y_train, y_pred_train_nb)
accuracy_test_nb = accuracy_score(y_test, y_pred_test_nb)

# Calculate precision
precision_train_nb = precision_score(y_train, y_pred_train_nb)
precision_test_nb = precision_score(y_test, y_pred_test_nb)

# Compute Confusion Matrix
conf_matrix_train_nb = confusion_matrix(y_train, y_pred_train_nb)
conf_matrix_test_nb = confusion_matrix(y_test, y_pred_test_nb)

print("\nNaive Bayes Results:")
print("Training Accuracy:", accuracy_train_nb)
print("Test Accuracy:", accuracy_test_nb)
print("Training Precision:", precision_train_nb)
print("Test Precision:", precision_test_nb)
print("Training Confusion Matrix:\n", conf_matrix_train_nb)
print("Test Confusion Matrix:\n", conf_matrix_test_nb)

# BONUS
# 1. Feature Expansion for Logistic Regression

# Define degrees to test
degrees = [2, 3]

for degree in degrees:
    print(f"\nPolynomial Degree: {degree}")

    # Apply polynomial feature expansion
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)

    # Train a Logistic Regression model (LR) with expanded features
    # Increased max_iter and changed solver
    regr_poly = linear_model.LogisticRegression(fit_intercept=False, max_iter=5000, solver='liblinear')
    regr_poly.fit(X_train_poly, y_train)

    # Predicting on training and test datasets
    y_pred_train_poly = regr_poly.predict(X_train_poly)
    y_pred_test_poly = regr_poly.predict(X_test_poly)

    # Calculate accuracy
    accuracy_train_poly = accuracy_score(y_train, y_pred_train_poly)
    accuracy_test_poly = accuracy_score(y_test, y_pred_test_poly)

    # Calculate precision
    precision_train_poly = precision_score(y_train, y_pred_train_poly)
    precision_test_poly = precision_score(y_test, y_pred_test_poly)

    # Compute Confusion Matrix
    conf_matrix_train_poly = confusion_matrix(y_train, y_pred_train_poly)
    conf_matrix_test_poly = confusion_matrix(y_test, y_pred_test_poly)

    print("\nLogistic Regression with Polynomial Features Results:")
    print("Training Accuracy:", accuracy_train_poly)
    print("Test Accuracy:", accuracy_test_poly)
    print("Training Precision:", precision_train_poly)
    print("Test Precision:", precision_test_poly)
    print("Training Confusion Matrix:\n", conf_matrix_train_poly)
    print("Test Confusion Matrix:\n", conf_matrix_test_poly)

# 2. Train Logistic Regression models with regularization

C_values = [1, 5, 10]

for C in C_values:
    print(f"\nLogistic Regression with L2 regularization with C = {C}")

    # Initialize logistic regression model with L2 regularization
    regr_l2 = linear_model.LogisticRegression(penalty='l2', fit_intercept=False, max_iter=1000, C=C)

    # Train a logistic regression model using training sets
    regr_l2.fit(X_train, y_train)

    # Predicting on training and test datasets
    y_pred_train_l2 = regr_l2.predict(X_train)
    y_pred_test_l2 = regr_l2.predict(X_test)

    # Calculate accuracy
    accuracy_train_l2 = accuracy_score(y_train, y_pred_train_l2)
    accuracy_test_l2 = accuracy_score(y_test, y_pred_test_l2)

    # Calculate precision
    precision_train_l2 = precision_score(y_train, y_pred_train_l2)
    precision_test_l2 = precision_score(y_test, y_pred_test_l2)

    # Compute Confusion Matrix
    conf_matrix_train_l2 = confusion_matrix(y_train, y_pred_train_l2)
    conf_matrix_test_l2 = confusion_matrix(y_test, y_pred_test_l2)

    # Retrieve the model parameters (theta)
    theta_l2 = regr_l2.coef_
    intercept_l2 = regr_l2.intercept_

    print("\nLogistic Regression with L2 regularization Results:")
    print("Training Accuracy:", accuracy_train_l2)
    print("Test Accuracy:", accuracy_test_l2)
    print("Training Precision:", precision_train_l2)
    print("Test Precision:", precision_test_l2)
    print("Training Confusion Matrix:\n", conf_matrix_train_l2)
    print("Test Confusion Matrix:\n", conf_matrix_test_l2)
    print("Intercept:", intercept_l2)
    print("Coefficients (Theta):", theta_l2)

for C in C_values:
    print(f"\nLogistic Regression with L1 regularization with C = {C}")

    # Initialize logistic regression model with L1 regularization
    regr_l1 = linear_model.LogisticRegression(penalty='l1', solver='liblinear', fit_intercept=False, max_iter=1000, C=C)

    # Train a logistic regression model using training sets
    regr_l1.fit(X_train, y_train)

    # Predicting on training and test datasets
    y_pred_train_l1 = regr_l1.predict(X_train)
    y_pred_test_l1 = regr_l1.predict(X_test)

    # Calculate accuracy
    accuracy_train_l1 = accuracy_score(y_train, y_pred_train_l1)
    accuracy_test_l1 = accuracy_score(y_test, y_pred_test_l1)

    # Calculate precision
    precision_train_l1 = precision_score(y_train, y_pred_train_l1)
    precision_test_l1 = precision_score(y_test, y_pred_test_l1)

    # Compute Confusion Matrix
    conf_matrix_train_l1 = confusion_matrix(y_train, y_pred_train_l1)
    conf_matrix_test_l1 = confusion_matrix(y_test, y_pred_test_l1)

    # Retrieve the model parameters (theta)
    theta_l1 = regr_l1.coef_
    intercept_l1 = regr_l1.intercept_

    print("\nLogistic Regression with L1 regularization Results:")
    print("Training Accuracy:", accuracy_train_l1)
    print("Test Accuracy:", accuracy_test_l1)
    print("Training Precision:", precision_train_l1)
    print("Test Precision:", precision_test_l1)
    print("Training Confusion Matrix:\n", conf_matrix_train_l1)
    print("Test Confusion Matrix:\n", conf_matrix_test_l1)
    print("Intercept:", intercept_l1)
    print("Coefficients (Theta):", theta_l1)
