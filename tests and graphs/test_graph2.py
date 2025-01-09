import unittest
import matplotlib.pyplot as plt
import pandas as pd


file_path = 'data/suicide-rate-male-female-who-mdb.csv'
data_raw = pd.read_csv(file_path)


data_cleaned = data_raw.rename(columns={
    'Age-standardized death rate from self-inflicted injuries per 100,000 population - Sex: Males - Age group: all ages': 'Male Suicide Rate',
    'Age-standardized death rate from self-inflicted injuries per 100,000 population - Sex: Females - Age group: all ages': 'Female Suicide Rate'
})
data_cleaned = data_cleaned.dropna(subset=['Male Suicide Rate', 'Female Suicide Rate'])
data_cleaned = data_cleaned.loc[data_cleaned.groupby('Entity')['Year'].idxmax()]
data_cleaned = data_cleaned[['Entity', 'Male Suicide Rate', 'Female Suicide Rate']]
data_cleaned['Male Suicide Rate'] = pd.to_numeric(data_cleaned['Male Suicide Rate'], errors='coerce')
data_cleaned['Female Suicide Rate'] = pd.to_numeric(data_cleaned['Female Suicide Rate'], errors='coerce')
data_cleaned = data_cleaned.dropna(subset=['Male Suicide Rate', 'Female Suicide Rate'])


def create_plot(data_cleaned):
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

  
    ax1.set_title('Top 10 Countries by Male and Female Suicide Rates', fontsize=18, weight='bold')

   
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

   
    fig.legend(
        handles=[male_scatter, female_scatter],  
        labels=['Male Suicide Rate', 'Female Suicide Rate'],
        loc="upper right",  
        fontsize=12,
        frameon=True  
    )

    plt.tight_layout()

    return fig, ax1, ax2

class TestGraphPlot(unittest.TestCase):
    def setUp(self):
        """Set up the plot for testing."""
        self.fig, self.ax1, self.ax2 = create_plot(data_cleaned)

    def test_title(self):
        """Test if the title is set correctly."""
        self.assertEqual(self.ax1.get_title(), 'Top 10 Countries by Male and Female Suicide Rates')

    def test_yaxis_labels(self):
        """Test if the y-axis labels are correct."""
        self.assertEqual(self.ax1.get_ylabel(), 'Male Suicide Rate (per 100,000)')
        self.assertEqual(self.ax2.get_ylabel(), 'Female Suicide Rate (per 100,000)')

    def test_xaxis_labels(self):
        """Test if the x-axis has correct labels."""
        x_labels = [label.get_text() for label in self.ax1.get_xticklabels()]
        expected_labels = data_cleaned.nlargest(10, 'Male Suicide Rate')['Entity'].tolist()
        self.assertListEqual(x_labels, expected_labels)

    def test_legend(self):
        """Test if the legend is present and has correct labels."""
        legend = self.fig.legends[0]  
        legend_texts = [text.get_text() for text in legend.get_texts()]
        self.assertIn('Male Suicide Rate', legend_texts)
        self.assertIn('Female Suicide Rate', legend_texts)

    def test_scatter_points(self):
        """Test if the scatter points are plotted correctly."""
      
        male_points = len(self.ax1.collections[0].get_offsets())
        female_points = len(self.ax2.collections[0].get_offsets())
        self.assertEqual(male_points, 10)  
        self.assertEqual(female_points, 10)  

    def tearDown(self):
        """Close the plot after each test."""
        plt.close(self.fig)


if __name__ == '__main__':
    unittest.main()
