import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = "nuforc_reports.csv"

# Turn file into pandas dataframe
df = pd.read_csv(data)

# Remove date information from the stats section

list = []
for i in range(len(df["stats"])):
    j = df.stats[i]
    list.append(j[11:27])
# print(list)

df["date_reported"] = list
# print(df.date_reported)
    
# Send cleaned dataframe to new CSV
df.to_csv("nuforc_cleaned.csv", index=False)