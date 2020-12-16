
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
def total(file):
    total={}
    for x in range(1,9):
        for y in file:
            if y[1] == "2012-10-0"+str(x):
                if y[0] != "NA":
                    total[y[1]] = total.get(y[1], 0) + int(y[0])
    for x in range(10,30):
        for y in file:
            if y[1] == "2012-10-"+str(x):
                if y[0] != "NA":
                    total[y[1]] = total.get(y[1], 0) + int(y[0])
    return sorted(total.values())
def median(file):
    m = total(file)
    if len(m) % 2 == 0:
        median = ( m[len(m)//2] + m[(len(m)//2-1)] ) / 2
    else:
        median = m[len(m) // 2]
    return median
def mean(file):
    m = total(file)
    sum=0
    for i in m:
        sum+=i
    return sum//len(m)
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
    print("The total number of steps taken per day is",sum(total(text)))
    print("The meadian is:",median(text))
    print("The mean is:",mean(text))
    print("Number of missing data:",NA(text))
    plt.hist(total(text))
    plt.ylabel("Frequency")
    plt.xlabel("Number of steps in a day")
    plt.show()


main()
