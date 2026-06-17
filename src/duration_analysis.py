import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/netflix_titles.csv")

# Select Movies only
movies = df[df["type"] == "Movie"].copy()

# Extract duration number
movies["duration_num"] = (
    movies["duration"]
    .str.extract(r'(\d+)')
    .astype(float)
)

# Plot histogram
plt.figure(figsize=(10,6))

plt.hist(
    movies["duration_num"].dropna(),
    bins=30
)

plt.title("Movie Duration Distribution")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")

plt.grid(True)

plt.savefig("images/movie_duration_distribution.png")
plt.close()

print("Movie duration chart saved successfully!")