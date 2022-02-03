"""
Loads a simple logistic regression model and random forest model for the 
kickstarter dataset.

To use the models in this folder, copy and paste this code except __main__

Model names:
model_logr
model_rf
"""

import pickle, os

import pandas as pd
import numpy as np

# encoding, preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, cross_val_score
from category_encoders import OneHotEncoder

# sklearn & modelling
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# metrics
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import precision_score, recall_score

# visualization
import matplotlib.pyplot as plt

# saving model
import pickle

model_logr = pickle.load(
    open(os.getcwd() + r"\\models\\logistic_regression_model", "rb")
)


if __name__ == "__main__":
    # testing with input, ORDER HAS TO MATCH FITTED DATA
    country = ["usa", "usa"]
    month = [9, 10]
    category = ["plays", "plays"]
    currency = ["usd", "usd"]
    length = [123456, 654321]
    goal = [50000, 1000000]
    staff_pick = [1, 0]

    test_input = pd.DataFrame(
        data={
            "country_code": country,
            "month_created": month,
            "category": category,
            "currency_code": currency,
            "project_length": length,
            "goal": goal,
            "staff_pick": staff_pick,
        }
    )

    print(model_logr.predict(test_input))

