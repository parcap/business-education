import pandas as pd
import numpy as np
import edhec_risk_kit as erk

ind = erk.get_ind_returns()

'''
erk.drawdown(ind['Food'])['Drawdown'].plot.line(figsize = (12, 6))

ind5_var = erk.var_gaussian(ind[['Food', 'Smoke', 'Coal', 'Beer', 'Fin']],
                            modified = True)

ind_var = erk.var_gaussian(ind, modified = True)

ind_var = ind_var.sort_values(ascending = False)

erk.var_gaussian(ind, modified = True).sort_values().plot.bar()

erk.sharpe_ratio(ind, 0.03, 12).sort_values().plot. \
    bar(title = 'Industry Sharpe Ratios 1926 - 2018', color = 'green')
    
er.sort_values().plot.bar()
''' 
er = erk.annualize_rets(ind['1996':'2000'], 12)
cov = ind['1996':'2000'].cov()

l = ['Food', 'Beer', 'Smoke', 'Coal']
# print(er[l])
# print(cov.loc[l, l])

weights = np.repeat(0.25, 4)

port_ew_return = erk.portfolio_return(weights, er[l])
port_ew_vol = erk.portfolio_vol(weights, cov.loc[l, l])


l = ['Smoke', 'Fin', 'Games', 'Coal']
# erk.plot_ef(20, er[l], cov.loc[l, l], '.-')

# erk.plot_ef(20, er, cov, '.-', show_cml = True, rfr = 0.1)

'''
l = ['Games', 'Fin']
w15 = erk.minimize_vol(0.15, er[l], cov.loc[l, l])
vol15 = erk.portfolio_vol(w15, cov.loc[l, l])
'''
l = ['Food', 'Steel']
print(erk.msr(0.1, er[l], cov.loc[l,l]))
print(erk.msr(0.1, np.array([0.11, .12]), cov.loc[l, l]))
print(erk.msr(0.1, np.array([0.10, .13]), cov.loc[l, l]))
print(erk.msr(0.1, np.array([0.13, .10]), cov.loc[l, l]))

# demonstrates the error maximizing nature of Markowitz

erk.plot_ef(20, er, cov, show_cml = True, rfr = 0.1,
            show_ew = True, show_gmv = True)
