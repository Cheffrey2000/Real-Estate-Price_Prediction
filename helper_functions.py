import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as scs
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols



# Building an OLS model with a summary output or just results
def make_ols_model(df, target='price', columns_to_use=None, add_constant=False, summary=False):
    X = df[columns_to_use]
    y = df[target]

    if add_constant:
        X = sm.add_constant(X)
    
    model = sm.OLS(y, X)
    results = model.fit()
    if summary:
        print(results.summary())
    return model, results

# Linear regression plot
def lin_reg_plt(x=None, y=None, data=None):
    sns.lmplot(x=x, y=y, data=data, aspect=1, height=4)
    
def make_pairplot(columns=None, df=None):
    if columns is None:
        columns=['price', 'bedrooms', 'bathrooms', 'ren_period', 'sqft_living', 'floors', 'condition']
    if df is None:
        df = df
    sns.pairplot(df, kind='scatter', vars=columns, height=2)
    plt.show()