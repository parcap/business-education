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
erk.kurtosis(normal_rets)

# scipy method for calculating kurtosis - note that this is excess kurtosis
sp.kurtosis(hfi)

# scipy's Jarque Bera test of significance
sp.jarque_bera(normal_rets)
sp.jarque_bera(hfi)

erk.is_normal(normal_rets)

hfi.aggregate(erk.is_normal)



# Semi-Deviation
hfi = erk.get_hfi_returns()

hfi.std(ddof = 0)   # standard deviation

hfi[hfi < 0].std(ddof = 0)   # semideviation
erk.semideviation(hfi)



# Historical VaR
np.percentile(hfi, 5, axis = 0)
        
erk.var_historic(hfi)

erk.var_gaussian(hfi)  
erk.var_gaussian(hfi, modified = True)  

var_list = [erk.var_gaussian(hfi), erk.var_gaussian(hfi, modified = True),
            erk.var_historic(hfi)]

comparison = pd.concat(var_list, axis = 1)
comparison.columns = ['Gaussian', 'Cornish-Fisher', 'Historic']

comparison.plot.bar(title = 'EDHEC Hedge Fund Indices VaR')

erk.cvar_historic(hfi)