import pandas as pd
import matplotlib.pyplot as plt

def convert_to_float(df):
    #Substituir vírgulas por pontos apenas em colunas de strings e depois converter para float
    for col in df.columns:
        #Verifica se a coluna é do tipo string
        if df[col].dtype == 'object':
            df[col] = df[col].str.replace(',', '.').astype(float)
    return df

df1 = pd.read_csv(r"C:\Users\finas\OneDrive\Documentos\int.csv", sep=";", index_col=0)
df2 = pd.read_csv(r"C:\Users\finas\OneDrive\Documentos\freq_estudos_dps_em.csv", sep=";", index_col=0)

df1 = convert_to_float(df1)
df2 = convert_to_float(df2)

# Alinhar os DataFrames pelos índices
merged_df = pd.merge(df1, df2, left_index=True, right_index=True, how='inner')

# Calcular a correlação entre as colunas
correlation = merged_df.corr().iloc[0, 1]  # Correlação entre a primeira coluna de df1 e df2
print(f'Correlação entre os dois gráficos: {correlation}')
