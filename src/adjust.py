import pandas as pd

# Read the CSV file
df = pd.read_csv('farm_dataset_original.csv')

# Update the 'duration' column based on the 'temperature' column
a = 0.5  # multiplier
b = 5    # offset
df['duration'] = df['temperature'] * a + b

# Save the updated DataFrame to a new CSV file
df.to_csv('farm_dataset_updated.csv', index=False)

print("The 'duration' column has been updated and saved to 'updated_farm_dataset.csv'.")
