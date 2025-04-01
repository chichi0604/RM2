import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/Results_21Mar2022.csv")

print("Column names:", df.columns.tolist())
print(df.head())

indicators = [
    "mean_ghgs",
    "mean_land",
    "mean_watscar",
    "mean_eut",
    "mean_ghgs_ch4",
    "mean_ghgs_n2o",
    "mean_bio",
    "mean_watuse",
    "mean_acid"
]

# Drop rows with missing values in any of the selected columns or the diet group
df = df.dropna(subset=indicators + ['diet_group'])

# Group by diet group and calculate mean values for each indicator
grouped = df.groupby('diet_group')[indicators].mean().reset_index()
print("\nMean values for each diet group:\n", grouped)

# Apply log transformation to each indicator to reduce scale differences
for col in indicators:
    grouped[col] = np.log1p(grouped[col])

# Normalize each indicator to range [0, 1] using Min-Max normalization
for col in indicators:
    min_val = grouped[col].min()
    max_val = grouped[col].max()
    grouped[col] = (grouped[col] - min_val) / (max_val - min_val)

print("\nLog-transformed and normalized data:")
print(grouped)

# Radar chart setup
N = len(indicators)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]  # Complete the loop

plt.figure(figsize=(10, 8))
ax = plt.subplot(111, polar=True)

# Set axis labels and format
plt.xticks(angles[:-1], indicators, fontsize=10)
ax.set_rlabel_position(30)
plt.yticks([0.2, 0.4, 0.6, 0.8], ["0.2", "0.4", "0.6", "0.8"], color="grey", size=9)
plt.ylim(0, 1)

# Plot each diet group
for idx, row in grouped.iterrows():
    values = row[indicators].tolist()
    values += values[:1]  # Close the loop
    ax.plot(angles, values, linewidth=2, label=row['diet_group'])
    ax.fill(angles, values, alpha=0.1)

plt.title("Radar Chart of Environmental Impact by Diet Type", size=16, y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.show()
