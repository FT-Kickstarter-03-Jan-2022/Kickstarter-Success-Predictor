import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from category_encoders import OrdinalEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
import pickle

df = pd.read_csv('kickstarter2.csv')

df["status"].replace({"failed": "0", "successful": "1"}, inplace=True)

df.set_index(df['Unnamed: 0'])

df = df.drop(columns = [ 'spotlight', 'backers_count', 'usd_pledged', 'Unnamed: 0'])

target = 'status'
X,y = df.drop(columns = target), df[target]

X_train, X_val, y_train, y_val = train_test_split(X, y, train_size=0.80, test_size=0.20, random_state=42)

print('The baseline accuracy is ', y_train.value_counts(normalize=True).max())

model_xgb = make_pipeline(
    OrdinalEncoder(),
    SimpleImputer(),
    XGBClassifier(random_state=42,n_estimators=1000, n_jobs=-1)
)

model_xgb.fit(X_train,y_train)

print('Training Accuracy', model_xgb.score(X_train, y_train))
print('Validation Accuracy', model_xgb.score(X_val, y_val))



importances = model_xgb.named_steps['xgbclassifier'].feature_importances_
feature_names = X_train.columns
feat_imp = pd.Series(data=importances, index=feature_names).sort_values()
feat_imp.tail(10).plot(kind='barh')
plt.xlabel('Gini Importance')
plt.ylabel('Feature')

country_code = 'us'
month_created = 11
category = 'plays'
currency_code = 'usd'
project_length = 5251394
goal = 60000
staff_pick = 0

test = [{'country_code': country_code, 'month_created': month_created, 'category': category, 'currency_code': currency_code, 'project_length': project_length, 'goal': goal, 'staff_pick': staff_pick}]

test = pd.DataFrame(test)

print(test)

print(model_xgb.predict(test))

with open('grb_pickle', 'wb') as f:
    pickle.dump(model_xgb, f)

with open('grb_pickle', 'rb') as f:
   model=pickle.load(f)
