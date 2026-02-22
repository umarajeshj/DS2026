import pandas as pd

app_names = ["Instagram","Youtube","Chrome","Maps","Whatsapp"]
batterDrain_values = [18, 25, 10, 30, 7]

#Create Panda series-app_name as index,battery_drain as values
battery_drain = pd.Series(list(batterDrain_values),index=app_names)

#Print the series
print(battery_drain)

#Print battery drain value of Instagram
print(battery_drain.loc['Instagram'])

#Print values and index
print(f"Values:{battery_drain.values}")
print(f"Index:{battery_drain.index}")

#Update index only first 3 values are kept(all uppercase)
battery_drain.index = battery_drain.index.str[:3].str.upper()
print(battery_drain)

#Use iloc,print first and last value     
print(battery_drain.iloc[0])
print(battery_drain.iloc[-1])

#Use loc,print value of Youtube, print values fron Instagram to Chrome
print(battery_drain.loc["YOU"])
print(battery_drain.loc["INS":"CHR"])

