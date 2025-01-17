import pandas as pd
import matplotlib.pyplot as plt
import pycountry_convert as pc


def map_country_to_continent(country_name):
    try:
        if not country_name:
            return 'Unknown'

      
        country_name = country_name.title()

        country_alpha = pc.country_name_to_country_alpha2(country_name)

        
        continent_code = pc.country_alpha2_to_continent_code(country_alpha)

       
        continent_map = {
            'AF': 'Africa', 
            'AS': 'Asia', 
            'EU': 'Europe',
            'OC': 'Oceania', 
            'NA': 'North America', 
            'SA': 'South America'
        }
        return continent_map.get(continent_code, 'Unknown')
    except:
        return 'Unknown'

file_path = 'data/suicide-rate-male-female-who-mdb.csv'
data = pd.read_csv(file_path)


data['Continent'] = data['Entity'].apply(map_country_to_continent)

data_cleaned = data.dropna(subset=[
    'Age-standardized death rate from self-inflicted injuries per 100,000 population - Sex: Males - Age group: all ages',
    'Age-standardized death rate from self-inflicted injuries per 100,000 population - Sex: Females - Age group: all ages'
])


data_cleaned = data_cleaned.rename(columns={
    'Age-standardized death rate from self-inflicted injuries per 100,000 population - Sex: Males - Age group: all ages': 'Male Suicide Rate',
    'Age-standardized death rate from self-inflicted injuries per 100,000 population - Sex: Females - Age group: all ages': 'Female Suicide Rate'
})


data_cleaned = data_cleaned[data_cleaned['Continent'] != 'Unknown']


continent_avg = data_cleaned.groupby('Continent')[['Male Suicide Rate', 'Female Suicide Rate']].mean()


plt.figure(figsize=(10, 6))
continent_avg.plot(kind='bar', figsize=(12, 6), color=['green', 'pink'])
plt.title('Average Suicide Rates by Gender for Each Continent', fontsize=16)
plt.xlabel('Continent', fontsize=14)
plt.ylabel('Average Suicide Rate (per 100,000 population)', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
