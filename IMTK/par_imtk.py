import pandas as pd
import db_scripts as dbs

pmdf = "select * from par_masterdata.fact."
pmdd = "select * from par_masterdata.dimension."
pmdp = "select * from par_masterdata.python."
pbid = "select * from par_bi.denormalized."

report_date = '09/30/2019'

dh_stmt = pbid + "holdings where Date = '" + report_date + "'"
dh = dbs.get_db_data(dh_stmt, 'pbi')

# long exposure by industry
long_exp_by_ind = dh[dh.Side=='Long'][['Symbol', 'Industry', 'Exposure']]
long_exp_by_ind = long_exp_by_ind.groupby(['Symbol', 'Industry']).sum().sort_values('Exposure', ascending=False)
long_exp_by_ind.to_excel('long_exposure_by_industry.xlsx')

# short exposure by industry
short_exp_by_ind = dh[dh.Side=='Short'][['Symbol', 'Industry', 'Exposure']]
short_exp_by_ind = short_exp_by_ind.groupby(['Symbol', 'Industry']).sum().sort_values('Exposure', ascending=True)
short_exp_by_ind.to_excel('short_exposure_by_industry.xlsx')





'''
# auditing P&L data
nh_stmt = pmdp + "holdings where date = '9/30/2019'"
nh = dbs.get_db_data(nh_stmt, 'pmd')

# constrain the fields to hone in on P&L data
nh = nh[['month_date', 'year_date', 'investment', 'manager', 'pnl_day']]
nh.columns = ['month', 'year', 'ticker', 'manager', 'pnl']

nh_group = nh.groupby(['month', 'year', 'manager'],
                      as_index = False)['pnl'].sum()

nh_group = nh_group[nh_group.month <= 9]

print(nh_group['pnl'].sum())

nh_pivot = nh_group.pivot(index = 'month',
                          columns = 'manager',
                          values = 'pnl')

nh_pivot.to_excel('testing3.xlsx')
'''