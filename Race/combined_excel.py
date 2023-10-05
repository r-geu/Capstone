#Combine race tables
import pandas as pd
combined_data = pd.concat([pd.read_excel(file_name) for file_name in ["Race_Black.xlsx", "Race_AIAN.xlsx", "Race_API.xlsx", "Race_Hispanic.xlsx", "Race_White.xlsx"]], ignore_index=True)
combined_data.to_excel("combined_race_data.xlsx", index=False)

#Remove unwanted columns
columns_to_drop = ['Unnamed: 11', 'Unnamed: 14','mmd_data (38)','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5', 'Unnamed: 6', 'Unnamed: 8', 'Unnamed: 10', 'mmd_data (41)', 'mmd_data (40)', 'mmd_data (37)',"mmd_data (43)", "Unnamed: 15", "Unnamed: 9","Unnamed: 7", "Unnamed: 1"]
combined_data.drop(columns=columns_to_drop, inplace=True)
combined_data.to_excel("combined_race_data.xlsx", index=False)

#Remove territories
values_to_remove = 'GUAM', 'NORTHERN MARIANAS', 'PUERTO RICO', 'VIRGIN ISLANDS', 'AMERICAN SAMOA'
combined_data = combined_data[~combined_data['Unnamed: 12'].isin(values_to_remove)]
combined_data.to_excel("combined_race_data.xlsx", index=False)

#Remove strings
df = pd.read_excel("combined_race_data.xlsx")
df = df[df['Unnamed: 13'] != 'primary_race']
df.to_excel("combined_race_data.xlsx", index=False)

#Combine age tables
import pandas as pd
combined_data = pd.concat([pd.read_excel(file_name) for file_name in ["Depression_65- 74.xlsx", "Depression_75- 84.xlsx", "Depression_85+.xlsx"]], ignore_index=True)
combined_data.to_excel("combined_age_data.xlsx", index=False)
