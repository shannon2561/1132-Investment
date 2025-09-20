import numpy as np
import pandas as pd
import statsmodels.api as sm

#5
stock_data = pd.read_csv("stock returns.csv")
factors_data = pd.read_csv("data factors.csv")

data=pd.merge(stock_data, factors_data, on="Date")

data = data.replace([np.inf, -np.inf], np.nan)
data = data.dropna()

x=data[["MKT", "SMB", "HML"]]
x=sm.add_constant(x)
y=data["Stock_Return"]-data["Risk_Free_Rate"]

model=sm.OLS(y,x).fit()
print(model.summary())


#6
print("Residuals")
residuals = model.resid
print(residuals)


#7
print("IVOL")
IVOL=residuals.std()
print(IVOL)
