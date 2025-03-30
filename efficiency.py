import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("premier-player-23-24.csv")

# create a column in the DataFrame called Player Efficiency to eventually call as the metric for the calculation
df["Player Efficiency"] = df["Min"] // df["Gls"]

top_20_efficiency = df[["Player", "Min", "Gls", "Player Efficiency"]].sort_values(by="Gls", ascending=False).head(20)
print(top_20_efficiency)

plt.figure(figsize=(14,8))
plt.bar(top_20_efficiency["Player"], top_20_efficiency["Player Efficiency"], color='dodgerblue')
plt.title("Most Efficient Scorers in the Premier League: 2023-2024", fontsize = 15)
plt.ylabel("Minutes per goal", fontsize = 10)
plt.xticks(rotation=45, ha='right', fontsize = 7)
plt.show()
plt.subplots_adjust(bottom=0.5)
plt.tight_layout()