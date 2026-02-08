import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("netflix_titles.csv")

print("Dataset shape:", df.shape)
print(df.head())

# count movies vs tv shows
type_count = df['type'].value_counts()
print(type_count)

# plot
type_count.plot(kind='bar', title="Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# top countries
top_country = df['country'].value_counts().head(10)
print(top_country)

top_country.plot(kind='bar', title="Top 10 content countries")
plt.show()
