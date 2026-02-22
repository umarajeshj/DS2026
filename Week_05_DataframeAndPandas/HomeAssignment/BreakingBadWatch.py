import pandas as pd

# Create a Pandas Series named watch_time using a dictionary
badWatchdata = {'Breaking Bad': 12.5, 'Dark': 8.0, 'Money Heist': 15.2, 'Friends': 6.3}
watch_time = pd.Series(badWatchdata)

# Print sorted Series .by values(ascending) .by index(alphabetical)
print(watch_time.sort_values())
print(watch_time.sort_index())

#Add another entry for Dark with value 8.0
#Add duplicate data
new_entry = pd.Series({'Dark': 8.0})
watch_time = pd.concat([watch_time, new_entry])
print("\nUpdated Series with Duplicate:")
print(watch_time)

#  11. Remove duplicate values
cleaned_watch_time = watch_time.drop_duplicates()
print("\nSeries after removing duplicates:")
print(cleaned_watch_time)

print("\n" + "*"*20 + "Excercise 3 "+"*"*20 +"\n")
# Create two Pandas Series:
season1_data = {'Breaking Bad': 6.0, 'Dark': 4.0, 'Money Heist': 7.5}
season2_data = {'Breaking Bad': 6.5, 'Dark': 4.0, 'Money Heist': 7.7}

season1 = pd.Series(season1_data)
season2 = pd.Series(season2_data)

#Arithmentic operations
print("Addition:\n", season1 + season2)
print("\nSubtraction:\n", season2 - season1)
print("\nMultiplication:\n", season1 * season2)
print("\nDivision:\n", season2 / season1)

#Total watch time
total_watch_time = season1.add(season2)
print("\nTotal Watch Time per Show:\n", total_watch_time)

print("\n" + "*"*20 + "Excercise 4 "+"*"*20 +"\n")
# Create Series
usage_data = pd.Series([20, 30, None, 20, 50, None, 30])

# Find Nulls
print("Total Null Values:", usage_data.isnull().sum())
print("Positions of Nulls:\n", usage_data[usage_data.isnull()].index.tolist())

# Remove Nulls and Duplicates
cleaned_data = usage_data.dropna().drop_duplicates()

# Print Cleaned Series
print("\nCleaned Series (No Nulls, No Duplicates):")
print(cleaned_data)

total_run = cleaned_data.sum()
print(f"Total runtime : {total_run}")

long_ep = cleaned_data[cleaned_data > 50]
print(f"Episodes > 50 : \n{long_ep}")

short_ep = cleaned_data[cleaned_data < 48]
print(f"Episodes < 48 : \n{short_ep}")

max_time = cleaned_data.max()
min_time = cleaned_data.min()
print(f"Min and Max episode time : {min_time},{max_time}")

longest_ep_name = cleaned_data.idxmax()
shortest_ep_name = cleaned_data.idxmin()
print(f"longest and shortest episode : {longest_ep_name},{shortest_ep_name}")

exactly_47 = (cleaned_data == 47).sum()
print(f"Episodes exact 47 mins: {exactly_47}")

between_45_50 = cleaned_data[cleaned_data.between(45, 50)]
print(f"Episodes between 45 and 50 mins: {between_45_50}")

hours = total_run // 60
mins = total_run % 60
print(f"Runtime after hrs n mins conversion: {hours}h {mins}m")

#Comparison
s1_long = (season1 > 50).sum()
s2_long = (season2 > 50).sum()
winner = "Season 1" if s1_long > s2_long else "Season 2"
print(winner)