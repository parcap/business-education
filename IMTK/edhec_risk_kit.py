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
    
def skewness(returns):    
    '''
    Alternative to scipy.stats.skew()
    Computes the skewness of the supplied series or data frame
    Returns a float or a series
    '''
    returns_demeaned = returns - returns.mean()
    sigma_returns = returns.std(ddof = 0)
    skewness = (returns_demeaned ** 3).mean() / (sigma_returns ** 3)
    
    return skewness

def get_ffme_returns():    
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
    
    return rets

def get_hfi_returns():    
    '''
    Load and format the EDHEC Hedge Fund Index Returns
    '''
    hfi = pd.read_csv('data/edhec-hedgefundindices.csv',
                   header = 0,
                   index_col = 0,
                   parse_dates = True)

    hfi = hfi / 100
    hfi.index = hfi.index.to_period('M')
    
    return hfi