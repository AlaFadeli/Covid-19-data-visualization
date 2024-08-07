
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns

# Apply a seaborn style
sns.set(style="whitegrid")

# Data
c19_cases_by_country = {
    "USA": 111820082,
    "India": 45035393,
    "France": 40138560,
    "Germany": 38828995,
    "Brazil": 38743918,
    "S. Korea": 34571873,
    "Japan": 33803572,
    "Italy": 26723249,
    "UK": 24910387,
    "Russia": 24124215
}

# Plot
categories = list(c19_cases_by_country.keys())
values = list(c19_cases_by_country.values())

fig, ax = plt.subplots(figsize=(12, 7))  # Adjust figure size for better readability

# Create a bar plot with improved style
bars = ax.bar(categories, values, color=sns.color_palette("viridis", len(categories)), edgecolor='w', linewidth=1.2)

# Add value labels on top of bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1e6, f'{yval * 1e-6:.1f}M', ha='center', va='bottom', fontsize=10, color='black', weight='bold')

def millions_formatter(x, pos):
    """Formatter function to display y-axis values in millions."""
    return f'{x * 1e-6:.1f}

