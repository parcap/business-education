import pandas as pd
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

# if mean > median, this is a sign of potential negative skewness
