import pandas as pd

# Path to your JSON file
json_file_path = '/Users/jolly/Downloads/Del_batch5_11:1_reworkpath/batch5.6_TOYOTA82_2019_08_23__17_24_41_delivery_06030.json'

# Load JSON data from the file into a DataFrame
df = pd.read_json(json_file_path)

# Display the DataFrame
print(df)

# Summary statistics
print(df.describe())

# Filter data
speed_limit_signs = df[df['type'] == 'Speed Limit']
print(speed_limit_signs)

