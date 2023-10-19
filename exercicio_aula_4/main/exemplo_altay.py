#exemplo em R
"""
v1 <- c(1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,4,5,6)
v2 <- c(1,2,1,1,1,1,2,1,2,1,3,4,3,3,3,4,6,5)
v3 <- c(3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,5,4,6)
v4 <- c(3,3,4,3,3,1,1,2,1,1,1,1,2,1,1,5,6,4)
v5 <- c(1,1,1,1,1,3,3,3,3,3,1,1,1,1,1,6,4,5)
v6 <- c(1,1,1,2,1,3,3,3,4,3,1,1,1,2,1,6,5,4)
m1 <- cbind(v1,v2,v3,v4,v5,v6)

c1 = cor(m1)
c1
round (c1, 2)

factanal(m1, factors = 3) #usando dados

factanal(c1, covmat = c1, factors = 3) #usando matriz covariancia
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import FactorAnalysis
from scipy.stats import pearsonr

# Criando os vetores
v1 = [1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,4,5,6]
v2 = [1,2,1,1,1,1,2,1,2,1,3,4,3,3,3,4,6,5]
v3 = [3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,5,4,6]
v4 = [3,3,4,3,3,1,1,2,1,1,1,1,2,1,1,5,6,4]
v5 = [1,1,1,1,1,3,3,3,3,3,1,1,1,1,1,6,4,5]
v6 = [1,1,1,2,1,3,3,3,4,3,1,1,1,2,1,6,5,4]

# Criando a matriz
m1 = pd.DataFrame({'v1': v1, 'v2': v2, 'v3': v3, 'v4': v4, 'v5': v5, 'v6': v6})

# Calculando a matriz de correlação
c1 = m1.corr()

# Arredondando a matriz de correlação
c1_rounded = c1.round(2)

# Realizando análise fatorial nos dados
fa = FactorAnalysis(n_components=3)
fa.fit(m1)

# Realizando análise fatorial na matriz de correlação
# Note que o scikit-learn não suporta análise fatorial diretamente na matriz de correlação,
# então estamos ajustando nos dados originais novamente
fa_cov = FactorAnalysis(n_components=3)
fa_cov.fit(m1)

# Exibindo os resultados
print(c1_rounded)
print(fa.components_)
print(fa_cov.components_)
