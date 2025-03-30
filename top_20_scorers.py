# imported numpy , pandas , and seaborn
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("premier-player-23-24.csv")

# print(df.head()) --> shows first 5 rows of data set

#print list of columns to identify which ones contain goals data
# print(df.columns)

top_goal_scorers = df.sort_values(by="Gls", ascending=False).head(20)

print(top_goal_scorers[["Player","Gls"]])

plt.figure(figsize=(10,6))
plt.bar(top_goal_scorers["Player"], top_goal_scorers["Gls"], color = ('dodgerblue'))
plt.xlabel("Player Name")
plt.ylabel("Total Goals")
plt.title("Top 20 Premier League Goal Scorers: 2023-2024")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()