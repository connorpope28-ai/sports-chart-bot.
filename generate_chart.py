import matplotlib.pyplot as plt

# Sample MLB over/under weather index data
parks = ["Wrigley", "Fenway", "Coors", "Yankee"]
wind_out_mph = [14, 8, 4, 11]

plt.figure(figsize=(8, 4.5))
plt.bar(parks, wind_out_mph, color="#1d70b8")
plt.title("Outfield Wind Speed (mph) - Today's Slate")
plt.ylabel("Wind Out (mph)")
plt.tight_layout()

# Save chart image
plt.savefig("daily_chart.png", dpi=300)
print("Chart created successfully!")
