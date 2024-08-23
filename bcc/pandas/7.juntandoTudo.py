import pandas as pd
import matplotlib.pyplot as plt

#Carrega os dados das planilhas.csv, como um dataframe
data1 = pd.read_csv(r"C:\Users\finas\OneDrive\Documentos\int.csv", sep=";", index_col=0)
df1 = pd.DataFrame(data1)

data2 = pd.read_csv(r"C:\Users\finas\OneDrive\Documentos\freq_estudos_dps_em.csv", sep=";", index_col=0)
df2 = pd.DataFrame(data2)

#x recebe o index, y recebe primeira coluna como arr unidimensional
x1 = df1.index
y1 = df1.iloc[:,0]

x2 = df2.index
y2 = df2.iloc[:,0]

#subplot utilizado para especificar como serão destribuídos os gráficos linha coluna
plt.subplot(2, 1, 1)

#primeiro gráfico
plt.plot(x1, y1)
plt.title('Percentual de pessoas que utilizaram a a internet no período de referência na população de 10 anos ou mais de idade (%)')
plt.xlabel('Período')
plt.ylabel('População(%)')

#linha, coluna, terceiro argumento diz respeito a destribuição do gráfico na "matriz"
plt.subplot(2, 1, 2)

#segundo gráfico
plt.plot(x2, y2)
plt.title('Pessoas de 15 a 29 anos com o ensino médio completo ou superior incompleto que não frequentam escola, curso técnico, normal (magistério), pré-vestibular ou curso de qualificação profissional')
plt.xlabel('Período')
plt.ylabel('Mil Pessoas')

#tight_layout() serve para deixar os gráficos espaçados
plt.tight_layout()
plt.show()
