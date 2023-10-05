import pandas as pd
combined_data = pd.DataFrame()
for file_name in ["Race_Black.xlsx", "Race_Hispanic.xlsx", "Race_White.xlsx"]:
    race_data = pd.read_excel(file_name)
    combined_data = combined_data.append(race_data, ignore_index=True)

combined_data.to_excel("combined_race_data.xlsx", index=False)

import os
print("Current Directory:", os.getcwd())

import os

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

print("Script Directory:", script_directory)
