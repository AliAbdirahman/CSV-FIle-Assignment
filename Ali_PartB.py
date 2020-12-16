import pandas as pd
import matplotlib.pyplot as plt
activity_file = "activity.csv"
file = pd.read_csv(activity_file, delimiter = ',')
file = file.groupby(["interval"]).mean()
plt.plot(file)
plt.ylabel("Average steps")
plt.xlabel("5-min interval")
plt.show()
print(file)
