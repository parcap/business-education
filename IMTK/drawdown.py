import pandas as pd

def drawdown(return_series: pd.Series):
    '''
    Takes a time series of asset returns
    Computes and returns a data frame that contains:
        the wealth index
        the previous peaks
        the percent drawdowns
    '''
    wealth_index = 1000 * (1 + return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks) / previous_peaks
    
    return pd.DataFrame({
            'Wealth': wealth_index,
            'Peaks': previous_peaks,
            'Drawdown': drawdowns
            })

me_m = pd.read_csv('data/Portfolios_Formed_on_ME_monthly_EW.csv',
                   header = 0,
                   index_col = 0,
                   parse_dates = True,
                   na_values = -99.99)

rets = me_m[['Lo 10', 'Hi 10']]
rets.columns = ['SmallCap', 'LargeCap']
rets = rets / 100

rets.index = pd.to_datetime(rets.index, format = '%Y%m')
rets.index = rets.index.to_period('M')

# rets.index    # gives you the structure info about the rets object
# rets.info()   # gives you info about the rets object

# Neat filter you can do when data frame index is a date index
rets['1975']
rets['2015':]

wealth_index = 1000 * (1 + rets['LargeCap']).cumprod()
previous_peaks = wealth_index.cummax()
drawdowns = (wealth_index - previous_peaks) / previous_peaks

# Analytics on drawdown time series
drawdowns.min()
drawdowns['1975':].min()
drawdowns['1975':].idxmin()

# Let's leverage the defined function drawdown()
LargeCapDrawDown = drawdown(rets['LargeCap'])

drawdown(rets['LargeCap'])[['Wealth', 'Peaks']]
LargeCapDrawDown[['Wealth', 'Peaks']]   # same as the previous line

drawdown(rets[:'1950']['LargeCap'])[['Wealth', 'Peaks']]

drawdown(rets['LargeCap'])[['Drawdown']].min()
drawdown(rets['SmallCap'])[['Drawdown']].min()

drawdown(rets['LargeCap'])[['Drawdown']].idxmin()
drawdown(rets['SmallCap'])[['Drawdown']].idxmin()

drawdown(rets['1975':]['LargeCap'])[['Drawdown']].min()
drawdown(rets['1975':]['LargeCap'])[['Drawdown']].idxmin()