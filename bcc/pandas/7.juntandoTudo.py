import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv(r"C:\Users\finas\OneDrive\Documentos\int.csv", sep=";", index_col=0)
df1 = pd.DataFrame(data1)

x1 = df1.index
y1 = df1.iloc[:,0]

data2 = pd.read_csv(r"C:\Users\finas\OneDrive\Documentos\freq_estudos_dps_em.csv", sep=";", index_col=0)
df2 = pd.DataFrame(data2)

x2 = df2.index
y2 = df2.iloc[:,0]

plt.subplot(2, 1, 1)
plt.plot(x1, y1)

plt.title('Percentual de pessoas que utilizaram a a internet no período de referência na população de 10 anos ou mais de idade (%)')
plt.xlabel('Período')
plt.ylabel('População(%)')


plt.subplot(2, 1, 2)
plt.plot(x2, y2)

plt.title('Pessoas de 15 a 29 anos com o ensino médio completo ou superior incompleto que não frequentam escola, curso técnico, normal (magistério), pré-vestibular ou curso de qualificação profissional')
plt.xlabel('Período')
plt.ylabel('Mil Pessoas')

plt.tight_layout()
plt.show()
