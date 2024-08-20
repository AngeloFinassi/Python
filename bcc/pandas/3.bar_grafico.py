import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\finas\OneDrive\Documentos\teste1.csv", sep=";", index_col=0)
df = pd.DataFrame(data)

#Plota os dados
plt.figure(figsize=(10, 6))

for c in df.columns:
    #x-index, y-values for each index
    plt.bar(df.index, df[c], color='blue')

plt.title('Quantidades')
plt.xlabel('Produtos')
plt.ylabel('Valores')
plt.legend()

plt.show()