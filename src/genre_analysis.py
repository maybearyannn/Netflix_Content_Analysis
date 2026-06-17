import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/netflix_titles.csv")

# Extract genres
genres = (
    df["listed_in"]
    .str.split(", ")
    .explode()
)

# Top 10 genres
genre_counts = genres.value_counts().head(10)

# Plot
plt.figure(figsize=(10,6))

genre_counts.sort_values().plot(kind="barh")

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")

plt.tight_layout()
print(genre_counts)
plt.savefig("images/top_10_genres.png")

plt.close()