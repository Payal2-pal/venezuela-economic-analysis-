import pandas as pd
print("program started...")

# Load CSV file
df = pd.read_csv("venezuela_wdi_indicators.csv")

# Drop redundant column
df.drop(columns=["country_iso3"], inplace=True)

# Ensure correct data types
df["year"] = df["year"].astype(int)

numeric_cols = [
    "oil_rents_pct_gdp",
    "total_natural_resource_rents_pct_gdp",
    "fuel_exports_pct_merch_exports",
    "ores_and_metals_exports_pct_merch_exports",
    "gdp_current_usd",
    "gdp_growth_pct"
]

df[numeric_cols] = df[numeric_cols].astype(float)

# Rename columns
df.rename(columns={
    "year": "Year",
    "oil_rents_pct_gdp": "Oil Rents (% of GDP)",
    "total_natural_resource_rents_pct_gdp": "Total Natural Resource Rents (% of GDP)",
    "fuel_exports_pct_merch_exports": "Fuel Exports (% of Merchandise Exports)",
    "ores_and_metals_exports_pct_merch_exports": "Ores & Metals Exports (% of Merchandise Exports)",
    "gdp_current_usd": "GDP (Current USD)",
    "gdp_growth_pct": "GDP Growth (%)"
}, inplace=True)

# Sort by Year
df.sort_values(by="Year", inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned data
df.to_csv("venezuela_cleaned_data.csv", index=False)

print("Data cleaned successfully!")
