import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/netflix_titles.csv")

# Create pivot table
pivot = pd.pivot_table(
    df,
    index="release_year",
    columns="type",
    aggfunc="size",
    fill_value=0
)

plt.figure(figsize=(12,8))

sns.heatmap(
    pivot.tail(20),
    cmap="YlGnBu"
)

plt.title("Movies and TV Shows Added by Release Year")

plt.savefig("images/heatmap_release_year.png")
plt.close()

print("Heatmap saved successfully!")