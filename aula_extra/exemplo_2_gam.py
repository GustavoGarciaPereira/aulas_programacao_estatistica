import pandas as pd

# import statsmodels.api as sm
# import numpy as np
from statsmodels.gam.api import GLMGam, BSplines

df = pd.read_csv('esforco.csv', sep='\t')

print(df)
gam_bs = GLMGam.from_formula('VO2 ~ NYHA + Idade + Altura + Peso + FC', data=df)

# # import data
# from statsmodels.gam.tests.test_penalized import df_autos

# # create spline basis for weight and hp
# x_spline = df_autos[['weight', 'hp']]

# bs = BSplines(x_spline, df=[12, 10], degree=[3, 3])

# # penalization weight
# alpha = np.array([21833888.8, 6460.38479])
# gam_bs = GLMGam.from_formula('city_mpg ~ fuel + drive', data=df_autos)
res_bs = gam_bs.fit()

print(res_bs.summary())



'''
mod0 <- gam(VO2 ~ nyha + Idade + altura + Peso + FC, data=esforco) #modelo 1 básico
summary(mod0)

mod1 <- gam(VO2 ~ nyha + s(Idade) + s(altura) + s(Peso) + s(FC), data=esforco) 
summary(mod1)#modelo 2 smooth

plot(mod1,se=TRUE)#diagnóstico

mod2 <- gam(VO2 ~ nyha + Idade + s(altura) + Peso + s(FC),data=esforco)#modelo 3 ajustado
summary(mod2)

gam.check(mod2) #qualidade resíduo
'''
