import pandas as pd
import matplotlib.pyplot as plt

#carrega os dados, transforma em data frame
data = pd.read_csv(r"C:\Users\finas\OneDrive\Documentos\teste1.csv", sep=";", index_col=0)
df = pd.DataFrame(data)

#carega index e valores(arr) para variavel x e y
x = df.index
y = df.values

#plota o gráfico
plt.stem(x, y)
plt.show()