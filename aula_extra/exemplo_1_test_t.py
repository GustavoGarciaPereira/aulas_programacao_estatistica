"""
Perform t-test and create Q-Q plots

This code snippet reads data from a .sav file using the `pyreadstat` library, performs a t-test using the `ttest_ind` function from `scipy.stats`, and creates two Q-Q plots using `matplotlib.pyplot`.

Inputs:
- caminho: a string representing the path to the .sav file.

Outputs:
- t_stat: a float representing the t-statistic of the t-test.
- p_valor: a float representing the p-value of the t-test.

Example Usage:
```python
caminho = ''
df, meta = pyreadstat.read_sav(caminho)
grupo = df['grupo']
raclog = df['raclog']

# Realizar teste t
t_stat, p_valor = ttest_ind(raclog, grupo, equal_var=False)

# Gráficos Q-Q
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
stats.probplot(grupo, plot=plt)
plt.title('Gráfico Q-Q para o Grupo 1')

plt.subplot(1, 2, 2)
stats.probplot(raclog, plot=plt)
plt.title('Gráfico Q-Q para o Grupo 2')

plt.tight_layout()
plt.show()
```
"""

from scipy.stats import ttest_ind
import pyreadstat
import scipy.stats as stats
import matplotlib.pyplot as plt

caminho = ''
df, meta = pyreadstat.read_sav(caminho)
grupo = df['grupo']
raclog = df['raclog']
print(f'grupo {grupo}\n\n')
print(f'raclog {raclog}\n\n')

# Realizar teste t
t_stat, p_valor = ttest_ind(raclog, grupo, equal_var=False)

print(f"t-statistic: {t_stat}")
print(f"p-value: {p_valor}")

# Gráficos Q-Q
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
stats.probplot(grupo, plot=plt)
plt.title('Gráfico Q-Q para o Grupo 1')

plt.subplot(1, 2, 2)
stats.probplot(raclog, plot=plt)
plt.title('Gráfico Q-Q para o Grupo 2')

plt.tight_layout()
plt.show()
