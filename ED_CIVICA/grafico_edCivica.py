import matplotlib as mpl
import matplotlib.pyplot as plt
import csv

mesi_n = []
temp=[]
giacca = []
scuola = []
videogiochi=[]
data_file = open("./a.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
for row in data_reader:
    mesi_n.append(row[0])
    temp.append(int(row[1]))
    giacca.append(int(row[2]))
    scuola.append(int(row[3]))
    videogiochi.append(int(row[4]))

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle("Media temperature, giorni in cui metto una giacca, giorni di scuola e giorni in cui gioco ai videogiochi nel periodo Gennaio-Giugno")
ax1.plot(mesi_n, temp, '-g')
ax1.set_xlabel('Mese')
ax1.set_ylabel('Temp medie')

ax2.plot(mesi_n, giacca, '-r')
ax2.set_xlabel('Mese')
ax2.set_ylabel('Giorni di giacca')

ax3.plot(mesi_n, scuola, '-y')
ax3.set_xlabel('Mese')
ax3.set_ylabel('Giorni di scuola')

ax4.plot(mesi_n, videogiochi, '-b')
ax4.set_xlabel('Mese')
ax4.set_ylabel('Giorni di videogiochi')

plt.show()