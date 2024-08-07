
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns

# Apply a seaborn style
sns.set(style="whitegrid")

# Data

top_10_countries_by_deaths = {
    "United States": 1173000,
    "Brazil": 735000,
    "India": 530000,
    "Mexico": 340000,
    "Russia": 330000,
    "Peru": 280000,
    "Indonesia": 270000,
    "Turkey": 260000,
    "Italy": 240000,
    "United Kingdom": 230000
}

# Plot
categories = list(top_10_countries_by_deaths.keys())
values = list(top_10_countries_by_deaths.values())

fig, ax = plt.subplots(figsize=(12, 7))  # Adjust figure size for better readability

# Create a bar plot with improved style
bars = ax.bar(categories, values, color=sns.color_palette("viridis", len(categories)), edgecolor='w', linewidth=1.2)

# Add value labels on top of bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1e7, f'{yval * 1e-6:.1f}M', ha='center', va='bottom', fontsize=10, color='black', weight='bold')

def millions_formatter(x, pos):
    """Formatter function to display y-axis values in millions."""
    return f'{x * 1e-6:.1f}M'

# Apply the custom formatter to the y-axis
ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))

# Customization
plt.title("Top 10 Countries by Covid Deaths", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Country", fontsize=14, fontweight='bold', labelpad=15)
plt.ylabel("Deaths", fontsize=14, fontweight='bold', labelpad=15)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

# Add gridlines for y-axis for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7, linewidth=0.7)

# Add a background color
ax.set_facecolor('#f5f5f5')

# Add a title background
plt.title("Top 10 Countries by Deaths", fontsize=18, fontweight='bold', backgroundcolor='#e0e0e0')

# Improve layout
plt.tight_layout()

# Save the plot to a PNG file
plt.savefig('second_plot.png')

# Display
plt.show()
plt.savefig('plot2.png')

# Display
plt.show()
