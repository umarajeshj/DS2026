import pandas as pd
#1.Reading csv file
try:
    df=pd.read_csv("Week_05/matches.csv")
except FileNotFoundError:
    print("Error reading file")
    exit()

subset = df[['Season', 'winner', 'win_by_runs', 'win_by_wickets','venue']]

# 11. Filter all matches played in the IPL-2017 season. 
matches_2017 = subset[df['Season'] == 'IPL-2017']
print(matches_2017)
print("\n" + "*"*40 + "\n")

# 12. Filter all matches won by Mumbai Indians. 
winner_MI = subset[df['winner'] == 'Mumbai Indians']
print(winner_MI)
print("\n" + "*"*40 + "\n")

# 13. Filter matches where the win was by more than 50 runs. 
won = subset[df['win_by_runs'] > 50]
print(won)
print("\n" + "*"*40 + "\n")

# 14. Filter matches where the win was by more than 7 wickets. 
wickets = subset[df['win_by_wickets'] > 7]
print(wickets)
print("\n" + "*"*40 + "\n")

# 15. Filter matches played at Wankhede Stadium.
venue = subset[df['venue'] == 'Wankhede Stadium']
print(venue)
print("\n" + "*"*40 + "\n")