import pandas as pd

data = pd.read_csv ("train.csv")
print(data.head())
print(data.isnull().sum())

# Eksikleri doldur
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])
data = data.drop('Cabin', axis=1)

# Kategorik verileri dönüştür
data['Sex'] = data['Sex'].map({'male':0, 'female':1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Özellikleri ve hedefi ayır
X = data.drop(['Survived', 'Name', 'Ticket', 'PassengerId'], axis=1)
y = data['Survived']

print(X.head())
print(y.head())

