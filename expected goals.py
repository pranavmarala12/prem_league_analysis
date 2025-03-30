# goal is to graph xG and Gls to see which two are the closest together

# import pandas for data visualization

import pandas as pd
file_path = 'premier-player-23-24.csv'
df = pd.read_csv(file_path)

# print first 5 rows of data and then print a list of all columns
#print(df.head())
#print(df.columns.tolist())

import matplotlib.pyplot as plt
import numpy as np

Players = df['Player']
Goals = df['Gls']
Expected_Goals = df['xG']

df_sorted = df.sort_values(by="Gls", ascending=False).head(10)
Players = df_sorted["Player"]
Goals = df_sorted["Gls"]
Expected_Goals = df_sorted["xG"]

plt.figure(figsize=(10,6))
index = np.arange(len(Players))
bar_width = 0.35
plt.bar(index, Goals, bar_width, label="Goals")
plt.bar(index + bar_width, Expected_Goals, bar_width, label="Expected Goals")
plt.xlabel("Players")
plt.ylabel("Goals vs. Expected Goals")
plt.title("Goals vs. Expected Goals for top 10 scorers")
plt.xticks(index + bar_width / 2, Players, rotation=45, ha="right")
plt.legend()
plt.tight_layout()
plt.show()
