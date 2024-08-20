import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv(r"C:\Users\finas\OneDrive\Documentos\teste1.csv", sep=";", index_col=0)
df = pd.DataFrame(data)
x = df.index
y = df.values

#range da linha de 0 a 2pi com 500 amostras
x = np.linspace(0, 2*np.pi, 500)
s = np.sin(x)
c = np.cos(x)

#quant linhas e colunas
plt.subplot(2, 1, 1)
plt.plot(x, c)

plt.subplot(2, 1, 2)
plt.plot(x, s)

plt.show()
