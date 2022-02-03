import pandas as pd
import numpy as np

# encoding, preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
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

model_logr = make_pipeline(
    OneHotEncoder(use_cat_names=True),
    StandardScaler(),
    LogisticRegression(max_iter=10000),
)

model_logr.fit(X_train, y_train)


if __name__ == "__main__":
    filename = "logistic_regression_model"
    pickle.dump(model_logr, open(os.getcwd() + "\\models\\" + filename, "wb"))

