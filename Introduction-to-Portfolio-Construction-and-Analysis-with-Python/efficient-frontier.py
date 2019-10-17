import pandas as pd
import edhec_risk_kit as erk

ind = erk.get_ind_returns()

erk.drawdown(ind['Food'])['Drawdown'].plot.line(figsize = (12, 6))

ind5_var = erk.var_gaussian(ind[['Food', 'Smoke', 'Coal', 'Beer', 'Fin']],
                            modified = True)

ind_var = erk.var_gaussian(ind, modified = True)

ind_var = ind_var.sort_values(ascending = False)

erk.var_gaussian(ind, modified = True).sort_values().plot.bar()

erk.sharpe_ratio(ind, 0.03, 12).sort_values().plot. \
    bar(title = 'Industry Sharpe Ratios 1926 - 2018', color = 'green')

er = erk.annualize_rets(ind['1995':'2000'], 12)

er.sort_values().plot_bar()

cov = ind['1995':'2000'].cov()