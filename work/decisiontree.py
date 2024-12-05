import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

# Load your dataset (replace 'fake_dataset.csv' with the correct path if needed)
df = pd.read_csv('fake_dataset.csv')

# Check the first few rows to ensure the data is loaded correctly
print(df.head())

# Create a Decision Tree Regressor model
decision_tree = DecisionTreeRegressor(random_state=42)

# Select the features (humidity, temperature) and the target variable (duration)
X = df[['humidity', 'temperature']]
y = df['duration']

# Fit the model
decision_tree.fit(X, y)

# Predict the target (duration) based on the features
df['predicted_duration'] = decision_tree.predict(X)

# Plotting the actual vs predicted durations
plt.figure(figsize=(8, 6))
plt.scatter(df['humidity'], df['duration'], color='blue', label='Actual')
plt.scatter(df['humidity'], df['predicted_duration'], color='green', label='Predicted')
plt.xlabel('Humidity')
plt.ylabel('Duration')
plt.title('Decision Tree Regressor: Actual vs Predicted Duration')
plt.legend()
plt.show()
