import pandas as pd
import matplotlib.pyplot as plt

# Read unemployment data
data = pd.read_csv("unemployment_analysis/unemployment.csv")

# Remove extra spaces from column names
data.columns = data.columns.str.strip()

# Display data
print("\n===== UNEMPLOYMENT DATA =====")
print(data)

# Calculate average unemployment rate by state
average_rate = data.groupby("state")["unemployment_Rate"].mean()

print("\n===== STATE-WISE AVERAGE UNEMPLOYMENT RATE =====")
print(average_rate.round(2))

# Find the state with the highest average rate
highest_state = average_rate.idxmax()
highest_rate = average_rate.max()

print("\nHighest average unemployment rate:")
print(highest_state, ":", round(highest_rate, 2), "%")

# Create a large, professional graph
plt.figure(figsize=(12, 7))

bars = average_rate.sort_values(ascending=False).plot(
    kind="bar",
    color=["#2563EB", "#0D9488", "#F59E0B"],
    edgecolor="black",
    width=0.65
)

# Show percentage above each bar
for bar in bars.patches:
    height = bar.get_height()
    bars.annotate(
        f"{height:.2f}%",
        (bar.get_x() + bar.get_width() / 2, height),
        ha="center",
        va="bottom",
        fontsize=12,
        fontweight="bold"
    )

plt.title(
    "State-wise Average Unemployment Rate (2021–2024)",
    fontsize=17,
    fontweight="bold",
    pad=20
)
plt.xlabel("State", fontsize=13, fontweight="bold")
plt.ylabel("Average Unemployment Rate (%)", fontsize=13)
plt.xticks(rotation=0, fontsize=11)
plt.yticks(fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()

plt.savefig("unemployment_graph.png", dpi=300, bbox_inches="tight")
plt.show()