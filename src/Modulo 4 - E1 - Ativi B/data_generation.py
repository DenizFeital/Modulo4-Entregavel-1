import pandas as pd

def generate_data():
    # Read data from the CSV file
    data = pd.read_csv('farm_dataset_original.csv')
    return data

dataset = generate_data()

