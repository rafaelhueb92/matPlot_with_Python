# Data from Datasus
import os
import matplotlib.pyplot as plt

cur_path = os.path.dirname(__file__)

data = open(cur_path + "\\bases\\original.csv").readlines()

x = []
y = []

for i in range(len(data)):
    if i != 0:
        linha = data[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.title("Growth of Brazilian Population from 1980-2016")
plt.xlabel("Year")
plt.ylabel("Population x100.000.000")
plt.plot(x, y, color="#e4e4e4")
plt.show()
