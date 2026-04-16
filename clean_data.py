import pandas as pd

df = pd.read_csv("data/books_raw.csv")

# Clean price (robust)
df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True).astype(float)

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

df.to_csv("data/books_cleaned.csv", index=False)

print("✅ Cleaning done!")