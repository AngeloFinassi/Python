import matplotlib.pyplot as plt
anos = [2018, 2019, 2022, 2023]
ipca = [3.75, 4.31, 5.79, 3.94]  # Dados do IPCA
alimentacao = [4.04, 6.37, 11.64, 5.47]  # Dados da Alimentação
plt.figure(figsize=(10, 6))
plt.plot(anos, ipca, marker='o', label='IPCA (%)')
plt.plot(anos, alimentacao, marker='o', label='Alimentação (%)', linestyle='--')

plt.title('Correlação entre IPCA e Variação em Alimentação (2018-2023)')
plt.xlabel('Ano')
plt.ylabel('Variação (%)')
plt.grid(True)
plt.legend()
plt.xticks(anos)
plt.show()
