import csv
import pandas as pd

weather = pd.read_csv(r"weather\weather_data.csv")
print(weather.day)
print(weather['temp'].max())