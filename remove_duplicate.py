import pandas as pd

# Load the Excel file
df = pd.read_excel('IMPPAT_identifier.xlsx')

# Define the name of the column containing the IMPPAT identifier
column_name = 'IMPPAT Phytochemical identifier'  # Replace 'YourColumnName' with the actual column name

# Remove duplicates from the specified column
df_cleaned = df.drop_duplicates(subset=[column_name], keep='first')

# Save the cleaned data to a new Excel file
df_cleaned.to_excel('cleaned_excel_file.xlsx', index=False)

