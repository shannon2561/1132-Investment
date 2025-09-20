import numpy as np
import pandas as pd
import statsmodels.api as sm

#5
stock_0050=pd.read_csv("0050.csv")
stock_2317=pd.read_csv("2317.csv")
stock_2883=pd.read_csv("2883.csv")
factors=pd.read_csv("Data Factor.csv")

data_0050=pd.merge(stock_0050, factors, on="Date")
data_2317=pd.merge(stock_2317, factors, on="Date")
data_2883=pd.merge(stock_2883, factors, on="Date")


data_0050=data_0050.replace([np.inf, -np.inf], np.nan).dropna()
data_2317=data_2317.replace([np.inf, -np.inf], np.nan).dropna()
data_2883=data_2883.replace([np.inf, -np.inf], np.nan).dropna()


#0050
print("0050")
a=data_0050[["MKT", "SMB", "HML"]]
a=sm.add_constant(a)
b=data_0050["Ri_0050"]-data_0050["Rf"]
model_0050=sm.OLS(b,a).fit()
print(model_0050.summary())

print("Residuals")
residuals_0050=model_0050.resid
print(residuals_0050)

print("IVOL")
IVOL_0050=residuals_0050.std()
print(IVOL_0050)

print()

#2317
print("2317")
c=data_2317[["MKT", "SMB", "HML"]]
c=sm.add_constant(c)
d=data_2317["Ri_2317"]-data_2317["Rf"]
model_2317=sm.OLS(d,c).fit()
print(model_2317.summary())

print("Residuals")
residuals_2317=model_2317.resid
print(residuals_2317)

print("IVOL")
IVOL_2317=residuals_2317.std()
print(IVOL_2317)

print()

#2883
print("2883")
e=data_2883[["MKT", "SMB", "HML"]]
e=sm.add_constant(e)
f=data_2883["Ri_2883"]-data_2883["Rf"]
model_2883=sm.OLS(f,e).fit()
print(model_2883.summary())

print("Residuals")
residuals_2883=model_2883.resid
print(residuals_2883)

print("IVOL")
IVOL_2883=residuals_2883.std()
print(IVOL_2883)

print()