#combine Race tables
import pandas as pd

combined_data = pd.concat([pd.read_excel(file_name) for file_name in ["Race_Black.xlsx", "Race_AIAN.xlsx","Race_Hispanic.xlsx", "Race_White.xlsx"]], ignore_index=True)

combined_data.to_excel("combined_race_data.xlsx", index=False)

#remove unwanted columns
columns_to_drop = ['Unnamed: 11', 'Unnamed: 14','mmd_data (38)','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5', 'Unnamed: 6', 'Unnamed: 8', 'Unnamed: 10', 'mmd_data (39)', 'mmd_data (41)', 'mmd_data (40)', 'mmd_data (37)']

combined_data.drop(columns=columns_to_drop, inplace=True)

combined_data.to_excel("combined_race_data.xlsx", index=False)
