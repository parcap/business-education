import pandas as pd
import db_scripts as dbs

pmdf = "select * from par_masterdata.fact."
pmdd = "select * from par_masterdata.dimension."
pmdp = "select * from par_masterdata.python."
pbid = "select * from par_bi.denormalized."

# auditing P&L data
nh_stmt = pmdp + "holdings where date >= '1/1/2019'"
nh = dbs.get_db_data(nh_stmt, 'pmd')

# constrain the fields to hone in on P&L data
nh = nh[['date', 'month_date', 'year_date', 'investment', 'manager', 'pnl_day']]
nh_test = nh['2019':]

nh_group = nh.groupby(['date', 'manager'], as_index = False).sum()

print(nh_group.head())

nh_group_pivot = nh_group.pivot(index = 'date',
                                columns = 'manager',
                                values = 'pnl_day')

nh_group_pivot.to_excel("testing3.xlsx")