import pandas as pd
path = "/home/xetra/AlphaGoldmine/Data/Calendar/Calendar.csv"


t = pd.read_csv(path)
print(t["id"])