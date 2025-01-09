import pandas as pd
import matplotlib.pyplot as plt

# Example dataset (replace this with your actual data)
data_cleaned = pd.DataFrame({
    'Entity': ['United States', 'India', 'France', 'Germany', 'Brazil', 'South Africa', 'Japan', 'Russia', 'China', 'Australia'],
    'Male Suicide Rate': [20, 15, 18, 17, 25, 22, 12, 30, 14, 10],
    'Female Suicide Rate': [8, 5, 10, 9, 12, 11, 7, 15, 6, 4],
    'Continent': ['North America', 'Asia', 'Europe', 'Europe', 'South America', 'Africa', 'Asia', 'Europe', 'Asia', 'Oceania']
})

# Extract the top 10 countries with the highest male suicide rates
top_countries = data_cleaned.nlargest(10, 'Male Suicide Rate')

# Create a dual-axis plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot male suicide rates on the first y-axis
male_scatter = ax1.scatter(
    top_countries['Entity'],
    top_countries['Male Suicide Rate'],
    color='orange',  # Male points
    s=150,
    label='Male Suicide Rate',
    alpha=0.7
)
ax1.set_ylabel('Male Suicide Rate (per 100,000)', fontsize=14, color='orange', weight='bold')
ax1.tick_params(axis='y', labelcolor='orange')
ax1.set_xticks(range(len(top_countries['Entity'])))
ax1.set_xticklabels(top_countries['Entity'], rotation=45, ha='right')

# Create a second y-axis for female suicide rates
female_scatter = ax2 = ax1.twinx()
female_scatter = ax2.scatter(
    top_countries['Entity'],
    top_countries['Female Suicide Rate'],
    color='purple',  # Female points
    s=150,
    label='Female Suicide Rate',
    alpha=0.7
)
ax2.set_ylabel('Female Suicide Rate (per 100,000)', fontsize=14, color='purple', weight='bold')
ax2.tick_params(axis='y', labelcolor='purple')

# Add title and grid
plt.title('Top 10 Countries by Male and Female Suicide Rates', fontsize=18, weight='bold')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Move the legend to the top-right corner inside the graph
fig.legend(
    handles=[male_scatter, female_scatter],  # Use the scatter plots for the legend
    labels=['Male Suicide Rate', 'Female Suicide Rate'],
    loc="upper right",  # Position legend in the top-right corner inside the graph
    fontsize=12,
    frameon=True  # Add a border around the legend for clarity
)

# Adjust layout
plt.tight_layout()
plt.show()
