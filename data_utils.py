import pandas as pd

def load_data(filepath):
    """Load data from a CSV file and clean it."""
    data = pd.read_csv('thimmayapalli.csv',encoding='latin1')
    data['Gender'] = data['Gender'].str.strip()  # Strip whitespace from the 'Gender' column
    return data

def search_by_name(data, name):
    """Search and return records matching the given name."""
    filtered_data = data[data['Name'].str.contains(name, case=False)]
    return filtered_data, len(filtered_data)

def filter_by_gender(data, gender):
    """Filter records based on gender."""
    return data[data['Gender'].str.lower() == gender.lower()]

def people_in_age_range(data, min_age, max_age):
    """List all people within a specified age range."""
    filtered_data = data[(data['Age'] >= min_age) & (data['Age'] <= max_age)]
    return filtered_data, len(filtered_data)

def search_by_names(data, input_names):
    """Search and return records matching any of the input names."""
    # Split the input string into names, strip spaces, and form a regex pattern
    names_list = [name.strip() for name in input_names.split(',')]
    pattern = '|'.join(names_list)
    filtered_data = data[data['Name'].str.contains(pattern, case=False, na=False)]
    return filtered_data, len(filtered_data)
