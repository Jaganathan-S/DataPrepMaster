pip install pandas
pip install numpy

import pandas as pd
import numpy as np

def create_sample_data():
    data = {
        'date_column': pd.date_range(start='2023-01-01', periods=10, freq='D'),
        'status_column': ['Active', 'Inactive', np.nan, 'Active', 'Inactive', 'Pending', 'Active', 'Pending', np.nan, 'Inactive'],
        'numerical_column': [10, 20, np.nan, 30, 40, np.nan, 50, 60, 70, 80]
    }
    df = pd.DataFrame(data)
    df.to_csv('/path/to/your/directory/sample_data.csv', index=False)  
    print("Sample data created and saved to 'sample_data.csv'.")

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def handle_missing_values(data):
    for column in data.columns:
        if data[column].dtype == 'object':
            mode_value = data[column].mode()[0]
            data[column].fillna(mode_value, inplace=True)
        else:
            mean_value = data[column].mean()
            data[column].fillna(mean_value, inplace=True)
    print("Missing values handled.")
    return data

def convert_data_types(data):
    data['date_column'] = pd.to_datetime(data['date_column'], errors='coerce')
    print("Data types converted.")
    return data

def transform_data(data):
    if 'numerical_column' in data.columns:
        data['numerical_column'] = (data['numerical_column'] - data['numerical_column'].mean()) / data['numerical_column'].std()
        print("Data transformation applied.")
    return data

def save_cleaned_data(data, output_path):
    try:
        data.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}.")
    except Exception as e:
        print(f"Error saving data: {e}")

def main():
    create_sample_data()
    input_file = '/path/to/your/directory/sample_data.csv'  
    output_file = '/path/to/your/directory/cleaned_data.csv' 

    data = load_data(input_file)
    if data is not None:
        data = handle_missing_values(data)
        data = convert_data_types(data)
        data = transform_data(data)
        save_cleaned_data(data, output_file)

if __name__ == "__main__":
    main()
