import pandas as pd

# Load Excel file into pandas DataFrame

excel_file = 'mess.xlsx'  # Replace with your Excel file path
df = pd.read_excel(excel_file)

# Process your data here (perform any necessary operations on the DataFrame)

# Convert DataFrame to JSON
json_data = df.to_json(orient='records')

# Save JSON data to a file
output_json_file = 'output.json'
with open(output_json_file, 'w') as json_file:
    json_file.write(json_data)

print(f"Excel data has been processed and converted to JSON. Saved as '{output_json_file}'")
