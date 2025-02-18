import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from skl2onnx import to_onnx
import pickle

train = pd.read_csv('../data/churn_train.csv')

train = train.dropna()

train = train.drop(columns=[
    'CustomerID',
    'Age',
    'Tenure',
    'Usage Frequency',
    'Payment Delay',
    'Total Spend',
    'Last Interaction'
])

X = train[[
    'Gender',
    'Subscription Type',
    'Contract Length'
]]

y = train['Churn']


encoder = OneHotEncoder(handle_unknown='ignore')
encoded = encoder.fit_transform(X)
data_ohe = pd.DataFrame(
    encoded.toarray(),
    columns=encoder.get_feature_names_out(),
    dtype=int
)

print(data_ohe.info())

X_train, X_test, y_train, y_test = train_test_split(
    data_ohe, y, random_state=42, train_size=0.70
)

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=25
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

y_proba = model.predict_proba(X_test)


acc = accuracy_score(y_pred, y_test)
cr = classification_report(y_pred, y_test)

print('Accuracy: {}%'.format(acc*100))
print('\nClassification Report:\n {}'.format(cr))

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

X = pd.get_dummies(X)  # variáveis categóricas para numéricas
X = X.astype(np.float32)
X_np = X.to_numpy().astype(np.float32) 
onx = to_onnx(model, X_np[:1], target_opset=12)
with open("filename.onnx", "wb") as f:
    f.write(onx.SerializeToString())