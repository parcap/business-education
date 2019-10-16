import pandas as pd
import numpy as np
import scipy.stats as sp

# data import functions
def get_ind_returns():
    '''
    Load Ken French 30 Industry Portfolio Values Weighted Month Returns
    '''
    ind = pd.read_csv('data/ind30_m_vw_rets.csv',
                      header = 0, index_col = 0, parse_dates = True)
    ind /= 100
    ind.index = pd.to_datetime(ind.index, format = '%Y%m').to_period('M')
    ind.columns = ind.columns.str.strip()
    
    return ind


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

def kurtosis(returns):    
    '''
    Alternative to scipy.stats.kurtosis()
    Computes the skewness of the supplied series or data frame
    Returns a float or a series
    '''
    returns_demeaned = returns - returns.mean()
    sigma_returns = returns.std(ddof = 0)
    kurtosisness = (returns_demeaned ** 4).mean() / (sigma_returns ** 4)
    
    return kurtosisness

def is_normal(returns, level = 0.01):
    '''
    Applies the Jarque-Bera test to determine if a series is normal or not
    Test is applied at the 1% level by default
    Returns True if the hypothesis of normality is accepted, False otherwies
    '''
    statistic, p_value = sp.jarque_bera(returns)
    
    return p_value > level

def semideviation(returns):
    '''
    Returns the semideviation (aka standard deviation of negative returns only)
    returns must be a series of a data frame
    '''
    is_negative = returns < 0
    
    return returns[is_negative].std(ddof = 0)

def var_historic(returns, level = 5):
    '''
    Returns the historic VaR at a specified level
    i.e. returns the number such that "level" percent of the returns
    fall below that number, and the (100 - level) percent are above
    '''
    if isinstance(returns, pd.DataFrame):
        return returns.aggregate(var_historic, level = level)
    elif isinstance(returns, pd.Series):
        return -np.percentile(returns, level)
    else:
        raise TypeError('Expected returns to be a series or data frame')
        
def var_gaussian(returns, level = 5, modified = False):
    '''
    Returns the parameteric Gaussian VaR of a series of data frame
    '''
    z = sp.norm.ppf(level / 100)
    
    if modified:
        s = skewness(returns)
        k = kurtosis(returns)
        z = (z + (s / 6 * (z ** 2 -1)) +
                (1 / 24 * (z ** 3 - 3 * z) * (k - 3)) -
                (1 / 36 * (2 * z ** 3 - (s ** 2))))
    
    return -(returns.mean() + z * returns.std(ddof = 0))

def cvar_historic(returns, level = 5):
    '''
    Computes the Conditional VaR of a series or data frame
    '''
    if isinstance(returns, pd.DataFrame):
        return returns.aggregate(cvar_historic, level = level)
    elif isinstance(returns, pd.Series):
        is_beyond = returns <= -var_historic(returns, level = level)
        return -returns[is_beyond].mean()
    else:
        raise TypeError('Expected returns to be a series or data frame')

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