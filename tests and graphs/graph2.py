import pandas as pd
import matplotlib.pyplot as plt

data_cleaned = pd.DataFrame({
    'Entity': ['United States', 'India', 'France', 'Germany', 'Brazil', 'South Africa', 'Japan', 'Russia', 'China', 'Australia'],
    'Male Suicide Rate': [20, 15, 18, 17, 25, 22, 12, 30, 14, 10],
    'Female Suicide Rate': [8, 5, 10, 9, 12, 11, 7, 15, 6, 4],
    'Continent': ['North America', 'Asia', 'Europe', 'Europe', 'South America', 'Africa', 'Asia', 'Europe', 'Asia', 'Oceania']
})

#
top_countries = data_cleaned.nlargest(10, 'Male Suicide Rate')


fig, ax1 = plt.subplots(figsize=(12, 8))


male_scatter = ax1.scatter(
    top_countries['Entity'],
    top_countries['Male Suicide Rate'],
    color='orange',
    s=150,
    label='Male Suicide Rate',
    alpha=0.7
)
ax1.set_ylabel('Male Suicide Rate (per 100,000)', fontsize=14, color='orange', weight='bold')
ax1.tick_params(axis='y', labelcolor='orange')
ax1.set_xticks(range(len(top_countries['Entity'])))
ax1.set_xticklabels(top_countries['Entity'], rotation=45, ha='right')


female_scatter = ax2 = ax1.twinx()
female_scatter = ax2.scatter(
    top_countries['Entity'],
    top_countries['Female Suicide Rate'],
    color='purple',  
    s=150,
    label='Female Suicide Rate',
    alpha=0.7
)
ax2.set_ylabel('Female Suicide Rate (per 100,000)', fontsize=14, color='purple', weight='bold')
ax2.tick_params(axis='y', labelcolor='purple')

plt.title('Top 10 Countries by Male and Female Suicide Rates', fontsize=18, weight='bold')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)


fig.legend(
    handles=[male_scatter, female_scatter],  
    labels=['Male Suicide Rate', 'Female Suicide Rate'],
    loc="upper right",  
    fontsize=12,
    frameon=True  
)


plt.tight_layout()
plt.show()
