import matplotlib as mpl
import matplotlib.pyplot as plt
import csv

anno = []
val=[]

data_file = open("./CO2_emissions.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
next(data_reader)
next(data_reader)
next(data_reader)
next(data_reader)
for row in data_reader:
    anno.append(int(row[0]))
    val.append(float(row[1]))
    

fig, (ax1) = plt.subplots(1, 1)
fig.suptitle("dati")
ax1.plot(anno, val, '-g')
ax1.set_xlabel('anno')
ax1.set_ylabel('valore')


plt.show()