import pandas as pd
import matplotlib.pyplot as plt

#Carrega os arquivos e o transforma em um data frame
data = pd.read_csv(r"C:\Users\finas\OneDrive\Documentos\teste1.csv", sep=";", index_col=0)
df = pd.DataFrame(data)

#Plota os dados
for c in df.columns:
    #x-index, y-values para cada coluna
    plt.bar(df.index, df[c], color='blue')

#Títulos e nomes para detalhar o gráfico gerado
plt.title('Quantidades')
plt.xlabel('Produtos')
plt.ylabel('Valores')
plt.legend()

plt.show()