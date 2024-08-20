import pandas as pd
import random

numbers = []
for c in range(0, 1000):
    numbers.append(random.randint(0, 100))

df = pd.DataFrame(numbers)



#print(numbers)

#Mostra uma análise sobre o arr, max, min
#print(df.describe())

#os dados são 'deitados'
#print(df.T)

print(df.sort_index)