import matplotlib.pyplot as plt
from covid_analysis import CovidAnalysis

class covidVisualization(CovidAnalysis):
    def __init__(self, file_path):
        super().__init__(file_path)

    def bar_chart_top_10(self):
        data = self.get_top_n('Confirmed', 10)
        data = data.sort_values('Confirmed', ascending=True)
        
        plt.figure(figsize=(10, 6))
        plt.bar(data['Country/Region'], data['Confirmed'], color='skyblue')
        plt.title('Top 10 Countries by Confirmed Cases')
        plt.xlabel('Country/Region')
        plt.ylabel('No. of Confirmed Cases')
        plt.tight_layout()
        plt.show()
    
    def pie_chart_deaths_by_region(self):
        region_deaths = self.df.groupby('WHO Region')['Deaths'].sum()
        plt.figure(figsize=(8, 8))
        plt.pie(region_deaths, labels=region_deaths.index, autopct='%1.1f%%', startangle=90)
        plt.title('Global Death Distribution by WHO Region')
        plt.show()

    def line_chart_top_5(self):
        data = self.get_top_n('Confirmed', 5)
        plt.figure(figsize=(10, 6))
        plt.plot(data['Country/Region'], data['Confirmed'], marker='o', label='Confirmed', color='blue')
        plt.plot(data['Country/Region'], data['Deaths'], marker='s', label='Deaths', color='red')
        plt.xlabel('Country/Region')
        plt.ylabel('Death Count')
        plt.title('Confirmed vs Deaths: Top 5 Countries')
        plt.legend()
        plt.show()

    def scatter_confirmed_vs_recovered(self):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.df['Confirmed'], self.df['Recovered'], alpha=0.5, c='green')
        plt.title('Scatter Plot: Confirmed vs Recovered')
        plt.xlabel('Confirmed Cases')
        plt.ylabel('Recovered Cases')
        plt.show()

    def histogram_deaths(self):
        plt.figure(figsize=(10, 6))
        plt.hist(self.df['Deaths'], bins=30, color='crimson', edgecolor='black')
        plt.title('Histogram of Death Counts')
        plt.xlabel('Deaths')
        plt.ylabel('Count of Countries')
        plt.show()

    def stacked_bar_5_countries(self, selection=['US', 'Brazil', 'India', 'Russia', 'South Africa']):
        data = self.df[self.df['Country/Region'].isin(selection)]
        countries = data['Country/Region']
        confirmed = data['Confirmed']
        deaths = data['Deaths']
        recovered = data['Recovered']

        plt.bar(countries, confirmed, label='Confirmed', color='skyblue')
        plt.bar(countries, deaths, bottom=confirmed, label='Deaths', color='red')
        plt.bar(countries, recovered, bottom=confirmed + deaths, label='Recovered', color='green')

        plt.title('Stacked Cases for Selected Countries')
        plt.xlabel('Countries')
        plt.ylabel('Count')
        plt.show()

    def box_plot_confirmed(self):
        regions = self.df['WHO Region'].unique()
        data_to_plot = [self.df[self.df['WHO Region'] == reg]['Confirmed'] for reg in regions]
        
        plt.figure(figsize=(12, 6))
        plt.boxplot(data_to_plot, tick_labels=regions)
        plt.yscale('log')
        plt.title('Confirmed Cases across Regions (Log Scale)')
        plt.xticks(rotation=45)
        plt.show()

    def trend_line_india_vs_country(self, other_country="US"):
        india_data = self.df[self.df['Country/Region'] == 'India']['Confirmed'].values[0]
        other_data = self.df[self.df['Country/Region'] == other_country]['Confirmed'].values[0]
        
        plt.figure(figsize=(8, 6))
        plt.bar(['India', other_country], [india_data, other_data], color=['orange', 'blue'])
        plt.title(f'Confirmed Cases: India vs {other_country}')
        plt.ylabel('Confirmed Cases')
        plt.show()


if __name__ == "__main__":
    viz = covidVisualization('Week_06_matplotlib/country_wise_latest.csv')
    # viz.bar_chart_top_10()
    # viz.pie_chart_deaths_by_region()
    # viz.line_chart_top_5()
    # viz.scatter_confirmed_vs_recovered()
    # viz.histogram_deaths()
    # viz.stacked_bar_5_countries()
    viz.box_plot_confirmed()
    viz.trend_line_india_vs_country("US")
