import matplotlib.pyplot as plt

# Hypothetical data for user satisfaction by location
locations = ["Urban", "Rural", "Suburban"]
satisfaction = [80, 65, 70]  # Satisfaction percentages

plt.figure(figsize=(6,4))
plt.bar(locations, satisfaction, color=["#1f77b4", "#ff7f0e", "#2ca02c"])
plt.ylim(0, 100)
plt.title("User Satisfaction with Culturally Adapted Features")
plt.xlabel("Location")
plt.ylabel("Satisfaction (%)")

plt.savefig("cultural_bar_chart.png", dpi=300)
plt.show()