import pandas as pd
import numpy as np

prices = pd.read_csv('data/sample_prices.csv')
returns = prices.pct_change()

returns = returns.dropna()

# simplest approach to computing stats
returns_std = returns.std()

deviations = returns - returns.mean()
squared_deviations = deviations ** 2

number_of_obs = returns.shape[0]

variance = squared_deviations.sum() / (number_of_obs - 1)

volatility = np.sqrt(variance)

annualized_volatility = volatility * np.sqrt(12)



returns = pd.read_csv('data/Portfolios_Formed_on_ME_monthly_EW.csv',
                      header = 0,
                      index_col = 0,
                      parse_dates = True,
                      na_values = -99.99)

columns = ['Lo 10', 'Hi 10']
returns = returns[columns]
returns = returns / 100
number_of_obs = returns.shape[0]

returns.columns = ['SmallCap', 'LargeCap']

# returns.plot.line()

returns_std = returns.std()
annualized_volatility = returns_std * np.sqrt(12)

return_per_month = (returns + 1).prod() ** (1 / number_of_obs) - 1

annualized_return = (return_per_month + 1) ** 12 - 1
print(annualized_return)

# simple way to annualize returns
annualized_return = (returns + 1).prod() ** (12 / number_of_obs) - 1

riskfree_rate = 0.03

excess_return = annualized_return - riskfree_rate

sharpe_ratio = excess_return / annualized_volatility

print(sharpe_ratio)