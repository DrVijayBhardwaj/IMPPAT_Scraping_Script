import openpyxl
import requests
import os
import csv
import time

# Load the Excel sheet
wb = openpyxl.load_workbook('IMPPAT_identifier_no_duplicte.xlsx')
sheet = wb.active

# Create the directory to store SDF files if it doesn't exist
if not os.path.exists('sdf_files'):
    os.makedirs('sdf_files')

# Initialize a list to store download status
download_status_list = []

# Iterate over the rows in the sheet
for row in sheet.iter_rows():
    # Get the compound name from column B of the current row
    compound_name = row[1].value
    
    # Check if compound_name is not None and not an empty string
    if compound_name:
        # Construct the download link for the SDF file
        sdf_url = f'https://cb.imsc.res.in/imppat/images/3D/SDF/{compound_name}_3D.sdf'
        
        # Download the SDF file
        sdf_response = requests.get(sdf_url)
        
        # If the download was successful, save the SDF file to disk
        if sdf_response.status_code == 200:
            with open(os.path.join('sdf_files', f'{compound_name}.sdf'), 'wb') as f:
                f.write(sdf_response.content)
            print(f'Downloaded SDF for {compound_name}')
            download_status = 'Downloaded'
        else:
            print(f'Failed to download SDF for {compound_name}')
            download_status = 'Not Downloaded'
        
        # Append compound name and download status to the list
        download_status_list.append([compound_name, download_status])
        
        # Write download status to a CSV file and flush the buffer
        with open('download_status.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Compound', 'Download Status'])
            writer.writerows(download_status_list)
            file.flush()
        
        # Add a delay to view the CSV file
        time.sleep(5)  # Adjust the delay time as needed
