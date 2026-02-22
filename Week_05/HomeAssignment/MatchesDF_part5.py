import pandas as pd
#1.Reading csv file

df=pd.read_csv("Week_05/matches.csv")
subset = df[['Season', 'winner', 'win_by_runs', 'venue']]

# 21. Filter matches where the winner is either: • Mumbai Indians • Chennai Super Kings 
winnerIsin = subset[df['winner'].isin(['Mumbai Indians','Chennai Super Kings'])]
print(winnerIsin)
print("\n" + "*"*40 + "\n")

# 22. Filter matches excluding Mumbai Indians and Chennai Super Kings. 
excludingWinner = subset[~df['winner'].isin(['Mumbai Indians','Chennai Super Kings'])]
print(excludingWinner)
print("\n" + "*"*40 + "\n")

# 23. Filter matches where the venue is not: • Eden Gardens • Wankhede Stadium 
notVenue = subset[~df['venue'].isin(['Eden Gardens','Wankhede Stadium'])]
print(notVenue)
print("\n" + "*"*40 + "\n")