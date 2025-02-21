import pandas as pd

data = pd.read_csv("../data/churn_train.csv")

data = data[[
    'Gender',
    'Subscription Type',
    'Contract Length',
    'Churn'
]]

data = data[(data["Subscription Type"] != "Standard") & (data["Contract Length"] != "Quarterly")]
data['Gender'] = data['Gender'].replace('Male', 0)
data['Gender'] = data['Gender'].replace('Female', 1)
data['Subscription Type'] = data['Subscription Type'].replace('Basic', 0)
data['Subscription Type'] = data['Subscription Type'].replace('Premium', 1)
data['Contract Length'] = data['Contract Length'].replace('Monthly', 0)
data['Contract Length'] = data['Contract Length'].replace('Annual', 1)

print(data['Gender'].value_counts())
print(data['Subscription Type'].value_counts())
print(data['Contract Length'].value_counts())
print('-'*50)
print(data.info())

data.to_csv("../data/churn.csv", index=False)