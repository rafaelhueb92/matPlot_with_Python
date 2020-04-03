# Boxplot - diagram's box

import matplotlib.pyplot as plt
import random

vector = []

for i in range(100):
    random_nbr = random.randint(0,50);
    vector.append(random_nbr);

plt.bloxplot(vector);
plt.title("My first boxplot");
plt.show();