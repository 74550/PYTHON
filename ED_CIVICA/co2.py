import matplotlib as mpl
import matplotlib.pyplot as plt
import csv

anno = []
tot=[]
gas = []
liq = []
sol=[]
cem=[]
comb=[]
pro=[]
data_file = open("./CO2_emissions.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
for row in data_reader:
    anno.append(int(row[0]))
    tot.append(int(row[1]))
    gas.append(int(row[2]))
    liq.append(int(row[3]))
    sol.append(int(row[4]))
    cem.append(int(row[5]))
    comb.append(int(row[6]))
    pro.append(row[7])

fig, (ax1, ax2, ax3, ax4,ax5,ax6,ax7) = plt.subplots(7, 1)
fig.suptitle("dati")

ax1.plot(anno, tot, '-g')
ax1.set_xlabel('anno')
ax1.set_ylabel('Tot')

ax2.plot(anno, gas, '-r')
ax2.set_xlabel('anno')
ax2.set_ylabel('emissione di combustibile sottoforma di gas')

ax3.plot(anno, liq, '-y')
ax3.set_xlabel('anno')
ax3.set_ylabel('emissione di combustibile sottoforma di liquido')

ax4.plot(anno, sol, '-b')
ax4.set_xlabel('anno')
ax4.set_ylabel('emissione di combustibile sottoforma di solido')

ax5.plot(anno, cem, '-b')
ax5.set_xlabel('anno')
ax5.set_ylabel('cemento')

ax6.plot(anno, comb, '-b')
ax6.set_xlabel('anno')
ax6.set_ylabel('combustione del gas')

ax7.plot(anno, pro, '-b')
ax7.set_xlabel('anno')
ax7.set_ylabel('pro capite')

plt.show()