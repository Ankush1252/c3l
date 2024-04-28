import pandas as pd

data_url = "C:/Users/Ankush/Downloads/Weather.csv"
df = pd.read_csv(data_url)
years = df['YEAR'].unique()


# Function to find hottest/coolest year based on a flag (is_hottest)
def find_extreme_year(years, data, is_hottest=True):
    # Initialize variables
    extreme_year = None
    extreme_temp = float('-inf') if is_hottest else float('inf')
    # Loop through unique years
    for year in years:
        # Filter data for that year
        year_data = data[data['YEAR'] == year]
        # Calculate average temperature across all months
        avg_temp = year_data.mean().mean()
        # Update extreme values if necessary
        if (is_hottest and avg_temp > extreme_temp) or (not is_hottest and avg_temp < extreme_temp):
            extreme_year = year
            extreme_temp = avg_temp
    return extreme_year


# Find hottest year
hottest_year = find_extreme_year(years.copy(), df.copy())
# Find coolest year
coolest_year = find_extreme_year(years.copy(), df.copy(), False)

print(f"Hottest Year: {hottest_year}")
print(f"Coolest Year: {coolest_year}")
