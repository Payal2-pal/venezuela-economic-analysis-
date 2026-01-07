import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("venezuela_cleaned_data.csv")

# GDP Trend
plt.figure()
plt.plot(df["Year"], df["GDP (Current USD)"])
plt.title("GDP of Venezuela Over Time")
plt.xlabel("Year")
plt.ylabel("GDP (Current USD)")
plt.savefig("gdp_trend.png")
plt.show()

# GDP Growth Trend
plt.figure()
plt.plot(df["Year"], df["GDP Growth (%)"])
plt.title("GDP Growth Rate of Venezuela")
plt.xlabel("Year")
plt.ylabel("GDP Growth (%)")
plt.savefig("gdp_growth.png")
plt.show()

# -------- GRAPH 2: GDP Growth --------
plt.figure()
plt.plot(df["Year"], df["GDP Growth (%)"])
plt.title("GDP Growth Rate of Venezuela")
plt.xlabel("Year")
plt.ylabel("GDP Growth (%)")
plt.savefig("gdp_growth.png")
plt.close()
