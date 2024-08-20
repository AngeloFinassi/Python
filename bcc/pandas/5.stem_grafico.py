import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\finas\OneDrive\Documentos\teste1.csv", sep=";", index_col=0)
df = pd.DataFrame(data)
x = df.index
y = df.values

plt.figure(figsize=(15, 6))

plt.stem(x, y)
plt.show()