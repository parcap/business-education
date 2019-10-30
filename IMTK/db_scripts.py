import pyodbc
import pandas as pd

def open_par_masterdata_connection(db):
    
    if db == 'pmd':
        cnx = pyodbc.connect('Driver={SQL Server};'
                             'Server=parcap-sql01;'
                             'Database=par_masterdata;'
                             'Trusted_Connection=yes;')
    
    if db == 'pbi':
        cnx = pyodbc.connect('Driver={SQL Server};'
                             'Server=parcap-sql01;'
                             'Database=par_bi;'
                             'Trusted_Connection=yes;')
    
    return cnx

def get_db_data(sql_stmt, db):
    
    cnx = open_par_masterdata_connection(db)
    data = pd.read_sql(sql_stmt, cnx)
    cnx.close()
    
    return data