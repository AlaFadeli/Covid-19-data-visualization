import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns

# Apply a seaborn style
sns.set(style="whitegrid")

# Data
unemployment_rate = {
    "Dec 2019": 3.9,
    "Jan 2020": 3.6,
    "Apr 2020": 14.8,
    "June 2020": 11.0,
    "July 2020": 10.2,
    "Sept 2020": 7.8,
    "Jan 2021": 6.4,
    "Aug 2021": 5.1
}

# Convert data to DataFrame
unemployment_data = pd.DataFrame(list(unemployment_rate.items()), columns=['Date', 'Unemployment Rate (%)'])

# Convert 'Date' to datetime format with correct format string
unemployment_data['Date'] = pd.to_datetime(unemployment_data['Date'], format='%b %Y', errors='coerce')

# Handle any parsing errors by checking for NaT values and converting them manually
unemployment_data['Date'].fillna(pd.to_datetime(unemployment_data['Date'], format='%B %Y', errors='coerce'), inplace=True)

# Sort data by Date
unemployment_data = unemployment_data.sort_values('Date')

fig, ax = plt.subplots(figsize=(12, 7))  # Adjust figure size for better readability

# Create a line plot with improved style
sns.lineplot(x=unemployment_data['Date'], y=unemployment_data['Unemployment Rate (%)'], marker='o', palette="viridis", linewidth=2.5, markersize=8, ax=ax)

def percentage_formatter(x, pos):
    """Formatter function to display y-axis values as percentages."""
    return f'{x:.1f}%'

# Apply the custom formatter to the y-axis
ax.yaxis.set_major_formatter(FuncFormatter(percentage_formatter))

# Customization
plt.title("Unemployment Rate Over Time", fontsize=18, fontweight='bold', pad=20, backgroundcolor='#e0e0e0')
plt.xlabel("Date", fontsize=14, fontweight='bold', labelpad=15)
plt.ylabel("Unemployment Rate (%)", fontsize=14, fontweight='bold', labelpad=15)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

# Add gridlines for y-axis for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7, linewidth=0.7)

# Add a background color
ax.set_facecolor('#f5f5f5')

# Improve layout
plt.tight_layout()

# Save the plot to a PNG file
plt.savefig('unemployment_rate_line_chart.png')

# Display the plot
plt.show()

