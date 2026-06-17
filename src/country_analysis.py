import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/netflix_titles.csv")

# Count countries
country_counts = (
    df["country"]
    .dropna()
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)

# Plot
plt.figure(figsize=(10,6))

country_counts.sort_values().plot(kind="barh")

plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.tight_layout()

plt.savefig("images/top_10_countries.png")

plt.show()