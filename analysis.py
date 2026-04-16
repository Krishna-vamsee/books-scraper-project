import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/books_cleaned.csv")

print("Total Books:", len(df))
print("\nAverage Price:", df["Price"].mean())

# Most expensive books
top_books = df.sort_values(by="Price", ascending=False).head(5)
print("\nTop 5 Expensive Books:\n", top_books)

# Price Distribution
plt.hist(df["Price"], bins=20)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

# Ratings Distribution
df["Rating"].value_counts().sort_index().plot(kind="bar")
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.show()

# Avg Price per Rating
df.groupby("Rating")["Price"].mean().plot(kind="bar")
plt.title("Average Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price")
plt.show()