import pandas as pd
import numpy as np
import scipy.stats as sp
import edhec_risk_kit as erk

'''
returns = erk.get_ffme_returns()

erk.drawdown(returns['SmallCap'])['Drawdown'].min()

erk.drawdown(returns['1975':]['SmallCap'])['Drawdown'].min()
'''

hfi = erk.get_hfi_returns()

hfi_skewness_stats = pd.concat([hfi.mean(),
                                hfi.median(),
                                hfi.mean() > hfi.median()],
                               axis = 'columns')

# if mean < median, this is a sign of potential negative skewness

erk.skewness(hfi).sort_values()

# scipy method for calculating skewness
sp.skew(hfi)

normal_rets = np.random.normal(0, 0.15, size = (263, 1))

erk.skewness(normal_rets)