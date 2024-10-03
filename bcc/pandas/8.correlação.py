import pandas as pd

#Criação dos dados
data = {
    #         2018, 2019, 2020, 2021, 2022, 2023
    'ipca' : [3.75, 4.31, 4.52, 10.06, 5.79, 3.94],
    'alimentacao' : [4.04, 6.37, 14.09, 7.94, 11.64, 5.47]
    }

#Conversão para um Data Frame
df = pd.DataFrame(data)

correlation = df["ipca"].corr(df["alimentacao"])
print(correlation)

#import os; print(os.popen("dir").read())