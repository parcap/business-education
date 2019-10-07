import numpy as np
import pandas as pd

prices_a = [8.70, 8.91, 8.71]       # python list

prices_a_num = prices_a[1:]
prices_a_den = prices_a[:-1]

# prices_a_num / prices_a_den - 1
# does not work; can not operate of lists



prices_b = np.array([8.70, 8.91, 8.71])

prices_b_num = prices_b[1:]
prices_b_den = prices_b[:-1]

prices_b_num / prices_b_den - 1



prices_c = pd.DataFrame({"BLUE": [8.70, 8.91, 8.71, 8.43, 8.73],
                         "ORANGE": [10.66, 11.08, 10.71, 11.59, 12.11]})

# prices.iloc[1:] / prices.iloc[:-1] - 1
# doe not work due to unwarranted index alignment

approach1a = prices_c.iloc[1:].values / prices_c.iloc[:-1] - 1
approach1b = prices_c.iloc[1:] / prices_c.iloc[:-1].values - 1

approach2 = prices_c / prices_c.shift(1)

approach3 = prices_c.pct_change()



prices = pd.read_csv('data/sample_prices.csv')

returns = prices.pct_change()

# prices.plot()
# returns.plot.bar()

returns_std = returns.std()
returns_mean = returns.mean()

returns_plus_one = returns + 1

# numpy approach
cum_return_approach1 = np.prod(returns_plus_one) - 1

# pandas approach
cum_return_approach2 = returns_plus_one.prod() - 1

# print((cum_return_approach2 * 100).round(2))