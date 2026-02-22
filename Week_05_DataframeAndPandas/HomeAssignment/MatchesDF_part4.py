import pandas as pd
#1.Reading csv file

df=pd.read_csv("Week_05/matches.csv")
subset = df[['Season', 'winner', 'win_by_runs', 'team1','team2']]

# 16. Filter matches played in IPL-2017 or IPL-2018. 
matches_2017_2018 = subset[df['Season'].isin(['IPL-2017','IPL-2018'])]
print(matches_2017_2018)
print("\n" + "*"*40 + "\n")

# 17. Filter matches where: • Season is IPL-2017 • Winner is Sunrisers Hyderabad 
s17winner = subset[(df['Season'] == "IPL-2017") & (df['winner'] == "Sunrisers Hyderabad")]
print(s17winner)
print("\n" + "*"*40 + "\n")

# 18. Filter matches where: • team1 is Mumbai Indians • AND Mumbai Indians won the match 
wonbyMI = subset[(df['team1'] == "Mumbai Indians") & (df['winner'] == "Mumbai Indians")]
print(wonbyMI)
print("\n" + "*"*40 + "\n")

# 19. Filter matches where: • Win by runs is greater than 30 • AND season is after IPL-2016 
wonGrt30_2016= subset[(df['win_by_runs'] > 30) & (df['Season'] > "IPL-2016")]
print(wonGrt30_2016)
print("\n" + "*"*40 + "\n")

# 20. Filter matches where: • Winner is not equal to team1 • AND winner is not equal to team2
winnerNotinTeam1_2= subset[(df['winner'] != df['team1'] ) & (df['winner'] != df['team2'])]
print(winnerNotinTeam1_2)
print("\n" + "*"*40 + "\n")