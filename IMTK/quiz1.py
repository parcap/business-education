import pandas as pd
import numpy as np
import edhec_risk_kit as erk

me_m = pd.read_csv('data/Portfolios_Formed_on_ME_monthly_EW.csv',
                   header = 0,
                   index_col = 0,
                   parse_dates = True,
                   na_values = -99.99)

rets = me_m[['Lo 20', 'Hi 20']]
rets.columns = ['SmallCap', 'LargeCap']
rets = rets / 100
    
rets.index = pd.to_datetime(rets.index, format = '%Y%m')
rets.index = rets.index.to_period('M')


obs_rets = rets.shape[0]

print((rets + 1).prod() ** (12 / obs_rets) - 1)
print(rets.std() * np.sqrt(12))


rets_1999_to_2015 = rets['1999':'2015']

obs_rets_1999_to_2015 = rets_1999_to_2015.shape[0]

print((rets_1999_to_2015 + 1).prod() ** (12 / obs_rets_1999_to_2015) - 1)
print(rets_1999_to_2015.std() * np.sqrt(12))



wealth_index = 1000 * (1 + rets_1999_to_2015['LargeCap']).cumprod()
peaks = wealth_index.cummax()
drawdown = (wealth_index - peaks) / peaks

# wealth_index.plot.line()
# peaks.plot.line()
# drawdown.plot.line()

# print (-drawdown.min() * 100)
# print (drawdown.idxmin())


hfi = erk.get_hfi_returns()
hfi = hfi['2009':'2018']

hfi_negative_returns = pd.concat([hfi < 0])

semideviation = hfi[hfi_negative_returns].std()
skew = hfi.skew()
kurtosisness = hfi.kurtosis()

print(semideviation.idxmax())
print(semideviation.idxmin())
print(skew.idxmin())
print(kurtosisness.idxmax())