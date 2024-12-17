import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the data
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# Handling Missing Values
imputer = SimpleImputer(strategy='median')
train_data['LoanAmount'] = imputer.fit_transform(train_data[['LoanAmount']])
train_data['Loan_Amount_Term'] = imputer.fit_transform(train_data[['Loan_Amount_Term']])
train_data['Credit_History'] = imputer.fit_transform(train_data[['Credit_History']])

test_data['LoanAmount'] = imputer.fit_transform(test_data[['LoanAmount']])
test_data['Loan_Amount_Term'] = imputer.fit_transform(test_data[['Loan_Amount_Term']])
test_data['Credit_History'] = imputer.fit_transform(test_data[['Credit_History']])

# Fill categorical missing values with the mode
for col in ['Gender', 'Married', 'Dependents', 'Self_Employed']:
    train_data[col] = train_data[col].fillna(train_data[col].mode()[0])
    test_data[col] = test_data[col].fillna(test_data[col].mode()[0])

# Label Encoding for Categorical Columns
encoder = LabelEncoder()
for col in ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area', 'Loan_Status']:
    train_data[col] = encoder.fit_transform(train_data[col])
for col in ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']:
    test_data[col] = encoder.fit_transform(test_data[col])

for dataset in [train_data, test_data]:
    dataset['Dependents'] = dataset['Dependents'].replace('3+', 3).astype(float)

# Target Variable
X = train_data.drop(columns=['Loan_ID', 'Loan_Status'])
y = train_data['Loan_Status']
X_test = test_data.drop(columns=['Loan_ID'])

# Split data into train and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42, n_estimators=100)
model.fit(X_train, y_train)

y_pred_valid = model.predict(X_valid)
accuracy = accuracy_score(y_valid, y_pred_valid)

print(f'Validation Accuracy: {accuracy}')

# Predict on the test data
y_pred_test = model.predict(X_test)

final_predictions = pd.DataFrame({
    'Loan_ID': test_data['Loan_ID'],
    'Loan_Status': ['Y' if pred == 1 else 'N' for pred in y_pred_test]
})

final_predictions.to_csv('final_submission.csv', index=False)
print('Submission file saved as final_submission.csv')