import pandas as pd
import matplotlib.pyplot as plt
def Break(file):
    list=[]
    for y in file:
        k = y.split(",")
        list.append(k)
    list.pop(0)
    list.pop()
    return list

def NA(file):
    total=0
    for y in file:
        if y[0] == "NA":
            total+=1
    return total
def main():
    with open('activity.csv', encoding='utf8') as csv_file:
        file = csv_file.read().replace('"', "").split('\n')
    text = Break(file)
    print("Number of missing table:",NA(text))
main()
activity_file = "activity.csv"
table = pd.read_csv(activity_file, delimiter = ',')
new_tableset = table.fillna(0)
new_tableset = new_tableset.iloc[:, [0, 1]].dropna() 
table_total = new_tableset.groupby(["date"]).sum()
plt.hist(table_total)
plt.ylabel("Frequency")
plt.xlabel("Total Steps")
plt.show()
print("The mean is:", new_tableset.mean())
print("The median is:", new_tableset.median())
