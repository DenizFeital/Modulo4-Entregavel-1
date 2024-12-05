import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load your dataset (replace 'fake_dataset.csv' with the correct path if needed)
df = pd.read_csv('fake_dataset.csv')

# Check the first few rows to ensure the data is loaded correctly
print(df.head())

# Create a LabelEncoder to convert the categorical nutrient values into numeric labels
le = LabelEncoder()
df['nutrients_encoded'] = le.fit_transform(df['nutrients'])  # Convert 'nutrients' to numeric values

# Create a Random Forest Regressor model
rfr = RandomForestRegressor(n_estimators=100, random_state=0)

# Select the features (humidity, temperature) and the target variable (encoded nutrients)
X = df[['humidity', 'temperature']]
y = df['nutrients_encoded']  # Use the encoded nutrients column

# Fit the model
rfr.fit(X, y)

# Predict the target (nutrients) based on the features
df['predicted_nutrients_rfr'] = rfr.predict(X)

# Plotting the actual vs predicted nutrients
plt.figure(figsize=(8, 6))
plt.scatter(df['humidity'], df['nutrients_encoded'], color='blue', label='Actual')
plt.scatter(df['humidity'], df['predicted_nutrients_rfr'], color='red', label='Predicted (RFR)')
plt.xlabel('Humidity')
plt.ylabel('Encoded Nutrients')
plt.title('Random Forest Regressor: Actual vs Predicted Nutrients (Encoded)')
plt.legend()
plt.show()
