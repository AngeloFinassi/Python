import pandas as pd
import numpy as np

#2dimensões
df = pd.DataFrame(
    {
        "dates":pd.date_range("20060110", periods=5),
        #Por padrão adiciona uma data
        "times":pd.date_range("10:55", periods=5, freq="5min").time

        # "dates": (1.0, 2.0, 3.0),
        # "times": ['10:55', '11:00', '12:05']
    }
)

df2 = pd.DataFrame(
    {
        #raise ValueError("All arrays must be of the same length")
        "Matérias": ["Bases Matemáticas", "Estrutura da Matéria", "EDVT"],
        "NOTAS": [7, 5.75, 8.75],
        "Situação": ["B", "C", "B"]
    }
)

#To see a part of the arr use tail or head function
long_series = pd.Series(np.random.randn(1000))

print(df2)