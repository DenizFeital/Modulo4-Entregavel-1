import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load your dataset
df = pd.read_csv('fake_dataset.csv')

# Check the first few rows to ensure the data is loaded correctly
print(df.head())

# Create a Linear Regression model
linear_reg = LinearRegression()

# Select the features (humidity, temperature) and the target variable (target)
X = df[['humidity', 'temperature']]  # Features
y = df['target']  # Target variable

# Fit the model
linear_reg.fit(X, y)

# Predict the target based on the features
df['predicted_target'] = linear_reg.predict(X)

# Plotting the actual vs predicted target
plt.figure(figsize=(8, 6))
plt.scatter(df['humidity'], df['target'], color='blue', label='Actual')
plt.scatter(df['humidity'], df['predicted_target'], color='red', label='Predicted')
plt.xlabel('Humidity')
plt.ylabel('Target')
plt.title('Linear Regression: Actual vs Predicted Target (Humidity)')
plt.legend()
plt.show()

