
### Dataset Overview
# Load the dataset
import pandas as pd
house_data = pd.read_csv('House_Pricing.csv')

# Display basic information
print("Dataset Information:")
print(house_data.info())

# Display descriptive statistics
print("Dataset Description:")
print(house_data.describe())

### Duplicate Removal
# Check for duplicate rows and remove them
print(f"Duplicate rows before removal: {house_data.duplicated().sum()}")
house_data = house_data.drop_duplicates()
print(f"Duplicate rows after removal: {house_data.duplicated().sum()}")

# Check for duplicate columns and drop them
duplicate_columns = house_data.T.duplicated()
print(f"Duplicate columns: {duplicate_columns.sum()}")
house_data = house_data.loc[:, ~duplicate_columns]

### Handling Missing Values
# Identify missing values in each column
print("Missing Values per Column:")
print(house_data.isnull().sum())

# Handle missing values
# Numerical: Impute with mean
numerical_cols = house_data.select_dtypes(include=['float64', 'int64']).columns
for col in numerical_cols:
    if house_data[col].isnull().sum() > 0:
        house_data[col].fillna(house_data[col].mean(), inplace=True)

# Categorical: Impute with mode
categorical_cols = house_data.select_dtypes(include=['object']).columns
for col in categorical_cols:
    if house_data[col].isnull().sum() > 0:
        house_data[col].fillna(house_data[col].mode()[0], inplace=True)

### Scaling Numerical Variables
from sklearn.preprocessing import MinMaxScaler

# Exclude target variable 'SalePrice'
numerical_cols = house_data.select_dtypes(include=['float64', 'int64']).columns.drop('SalePrice')

# Apply Min-Max Scaling
scaler = MinMaxScaler()
house_data[numerical_cols] = scaler.fit_transform(house_data[numerical_cols])

### Encoding Categorical Variables
from sklearn.preprocessing import LabelEncoder

# Identify categorical columns
categorical_cols = house_data.select_dtypes(include=['object']).columns

# Apply One-Hot Encoding for nominal variables
house_data = pd.get_dummies(house_data, columns=categorical_cols, drop_first=True)

### Outlier Removal
# Using IQR method for outlier detection
for col in numerical_cols:
    Q1 = house_data[col].quantile(0.25)
    Q3 = house_data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    house_data = house_data[(house_data[col] >= lower_bound) & (house_data[col] <= upper_bound)]

### Train-Test Split
from sklearn.model_selection import train_test_split

# Define target variable
X = house_data.drop(columns=['SalePrice'])
y = house_data['SalePrice']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training data: {X_train.shape}, Testing data: {X_test.shape}")
