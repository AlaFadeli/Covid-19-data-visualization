
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd 
from matplotlib.ticker import FuncFormatter 


# Apply a seaborn style
sns.set(style="whitegrid")

# Data
global_gdp = {
    "2021": 97153.18,
    "2020": 85272.68,
    "2019": 87777.40
}

# Convert data to DataFrame
gdp_data = pd.DataFrame(list(global_gdp.items()), columns=['Year', 'GDP ($ Billion)'])

# Sort data by Year to ensure correct plotting order
gdp_data['Year'] = pd.to_datetime(gdp_data['Year'], format='%Y')
gdp_data = gdp_data.sort_values('Year')

fig, ax = plt.subplots(figsize=(12, 7))  # Adjust figure size for better readability

# Create a line plot with improved style
sns.lineplot(x=gdp_data['Year'], y=gdp_data['GDP ($ Billion)'], marker='o', palette="viridis", linewidth=2.5, markersize=8, ax=ax)

def billions_formatter(x, pos):
    """Formatter function to display y-axis values in billions."""
    return f'{x * 1e-3:.1f}B'

# Apply the custom formatter to the y-axis
ax.yaxis.set_major_formatter(FuncFormatter(billions_formatter))

# Customization
plt.title("Global GDP Over Years", fontsize=18, fontweight='bold', pad=20, backgroundcolor='#e0e0e0')
plt.xlabel("Year", fontsize=14, fontweight='bold', labelpad=15)
plt.ylabel("GDP ($ Billion)", fontsize=14, fontweight='bold', labelpad=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add gridlines for y-axis for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7, linewidth=0.7)

# Add a background color
ax.set_facecolor('#f5f5f5')

# Improve layout
plt.tight_layout()

# Save the plot to a PNG file
plt.savefig('global_gdp_line_chart.png')

# Display the plot
plt.show()

