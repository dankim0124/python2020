import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def getCSV_AVG_Wait(fileLoc):

    df = pd.read_csv(fileLoc+".csv")
    print("openfile  : ",fileLoc+".csv")
    df2 = df[["Wait","Direction"]]
    AVGWait = 0

    for i in range(df2.shape[0]):

        AVGWait += df2.loc[i]["Wait"]

    AVGWait/= df2.shape[0]
    return AVGWait

def ListOfAVG(folder):
    avgList = []
    for i in range(1,8):
        avg = getCSV_AVG_Wait(folder+"/"+str(i))
        print( "%dth avg :  %d"%(i,avg))
        avgList.append(avg)
    return avgList

avgList = ListOfAVG("./CSVS")
cost = []
for i in range(1,8):
    cost.append(12*i)
result = pd.DataFrame(data={"ratio" : ["1:2","2:4","3:6","4:8","5:10","6:12","7:14"], "avg":avgList,"cost" :cost })
print(result)

ax = result.plot(kind='bar', title='Wait time', legend=True, fontsize=12)
ax.set_xlabel("ratio", fontsize=12)
ax.set_ylabel('avg', fontsize=12)
ax.legend(["average wait time","cost of lanes"], fontsize=12)
plt.show()


# calculating ratio of lanes.
"""
# counting car
tmpList = df2[["Car_Number","Direction"]]
countingDireciton={"E":0,"W":0,"N":0,"S":0}
print(type(df2))
#print(df2.loc[1]["Direction"])

for i in range(tmpList.shape[0]):
    if tmpList.loc[i]["Direction"] =="E":
        countingDireciton["E"]+=1

    elif tmpList.loc[i]["Direction"] == "W":
        countingDireciton["W"]+=1

    elif tmpList.loc[i]["Direction"] =="N":
        countingDireciton["N"]+=1

    elif tmpList.loc[i]["Direction"] =="S":
        countingDireciton["S"]+=1

print("Done")
print(countingDireciton)
"""
