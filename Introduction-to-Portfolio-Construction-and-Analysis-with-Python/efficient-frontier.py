import pandas as pd
import edhec_risk_kit as erk

ind = erk.get_ind_returns()

erk.drawdown(ind['Food'])['Drawdown'].plot.line(figsize = (12, 6))

ind5_var = erk.var_gaussian(ind[['Food', 'Smoke', 'Coal', 'Beer', 'Fin']],
                            modified = True)

ind_var = erk.var_gaussian(ind, modified = True)

ind_var = ind_var.sort_values()

print(ind_var)
