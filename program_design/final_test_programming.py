import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_name = "billionaires.csv"
csv_data = pd.read_csv(file_name, header=None)

# print(csv_data) # type : pandas.DataFrame
# 1. year value missing => erase
# 2. year 당 객체 갯수를 그래프로.

csv_new = csv_data[[0, 3]]
# print(csv_new)

# erasing rows which has 0 value on founded year
erase = [0]
for i in range(csv_new.shape[0]):
    if csv_new.loc[i][3] == "0":
        erase.append(i)

dict = {}
csv_new = csv_new.drop(erase, 0)
for i in range(csv_new.shape[0]):
    try:
        dict[csv_new.loc[i][3]] += 1
    except KeyError:
        try:
            dict[csv_new.loc[i][3]] = 1
        except:
            pass

newData = pd.DataFrame(dict.items(), columns=['Date', 'num of people'])
newData = newData.sort_values(by=["Date"])
newData = newData.set_index(["Date"])

print(newData)
graph = newData.plot()
plt.show()


