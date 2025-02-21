import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

train = pd.read_csv('../data/churn.csv')

train = train.dropna()

X = train[[
    'Gender',
    'Subscription Type',
    'Contract Length'
]]

y = train['Churn']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, train_size=0.70
)

model = RandomForestClassifier(
    n_estimators=10
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

acc = accuracy_score(y_pred, y_test)
cr = classification_report(y_pred, y_test)

print('Accuracy: {}%'.format(acc*100))
print('\nClassification Report:\n {}'.format(cr))