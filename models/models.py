"""
Run this file to export logistic regression and random forest models 
"""

import pandas as pd
import numpy as np

# encoding, preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from category_encoders import OneHotEncoder, OrdinalEncoder

# sklearn & modelling
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline

# metrics
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import precision_score, recall_score

# saving model
import pickle
import os

df = pd.read_csv(os.getcwd() + r"\\Dataset\\kickstarter2.csv", index_col=0)


def wrangle(df: pd.DataFrame):
    # drop leaky columns
    df = df.drop(
        columns=["usd_pledged"]
    )  # info not known when making predictions?
    df = df.drop(
        columns=["backers_count"]
    )  # info not known when making predictions?
    df = df.drop(columns="spotlight")  # directly correlated with target

    # encode binary columns
    df["status"] = df["status"].isin(["successful"]).astype(int)
    df["staff_pick"] = df["staff_pick"].astype(int)

    # categorical variables
    df["month_created"] = df["month_created"].astype(object)

    return df


df_ks = wrangle(df)

target = "status"
X = df_ks.drop(columns=target)
y = df_ks[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# logistic regression model
model_logr = make_pipeline(
    OneHotEncoder(use_cat_names=True),
    StandardScaler(),
    LogisticRegression(max_iter=10000),
)

model_logr.fit(X_train, y_train)

# random forest model: CV search already performed
model_rf = make_pipeline(
    OrdinalEncoder(),
    RandomForestClassifier(
        n_estimators=150,
        criterion="gini",
        max_depth=45,
        min_samples_leaf=4,
        min_samples_split=8,
        n_jobs=-1,
    ),
)

model_rf.fit(X, y)

if __name__ == "__main__":
    logr_filename = "logistic_regression_model"
    pickle.dump(
        model_logr, open(os.getcwd() + "\\models\\" + logr_filename, "wb")
    )

    rf_filename = "random_forest_model"
    pickle.dump(
        model_logr, open(os.getcwd() + "\\models\\" + rf_filename, "wb")
    )
