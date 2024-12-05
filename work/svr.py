import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVR
import numpy as np

# Load your dataset (replace 'fake_dataset.csv' with the correct path if needed)
df = pd.read_csv('fake_dataset.csv')

# Check the first few rows to ensure the data is loaded correctly
print(df.head())

# Create a Support Vector Regressor model
svr = SVR(kernel='rbf')

# Select the features (humidity, temperature) and the target variable (duration)
X = df[['humidity', 'temperature']]
y = df['duration']

# Fit the model
svr.fit(X, y)

# Predict the target (duration) based on the features
df['predicted_duration_svr'] = svr.predict(X)

# Plotting the actual vs predicted durations
plt.figure(figsize=(8, 6))
plt.scatter(df['humidity'], df['duration'], color='blue', label='Actual')
plt.scatter(df['humidity'], df['predicted_duration_svr'], color='red', label='Predicted (SVR)')
plt.xlabel('Humidity')
plt.ylabel('Duration')
plt.title('Support Vector Regressor: Actual vs Predicted Duration')
plt.legend()
plt.show()
