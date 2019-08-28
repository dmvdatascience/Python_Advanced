# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:09:36 2019

@author: GrantDW
"""

def run_EDA(dataset):
    ''' 
    run_EDA takes a PANDAS dataframe and performs exploratory data analysis on it,
    in order to determine strengths, weaknesses, and simple relationships between
    the various columns.
    '''
    
    import pandas as pd
    
    df1 = pd.DataFrame({
        'Columns': dataset.columns.tolist(),
        'DataTypes': dataset.dtypes.tolist(),
        'Missing_count': dataset.apply(lambda x: (len(dataset)-x.count()), axis = 0),
        'Missing_percent': dataset.apply(lambda x: round((len(dataset)-x.count())/len(dataset),2), axis = 0),
        'Unique_count': dataset.apply(lambda x: x.nunique(), axis = 0),
        'Unique_percent': dataset.apply(lambda x: round(x.nunique()/len(dataset),2), axis = 0),
        })


    df2 = dataset.describe().set_index(pd.Series(['Count', 'Mean', 'StdDev', 'Min', 'Quart25', 'Med', 'Quart75', 'Max'])).transpose()

    df3 = df1.join(df2, how = 'left')
    
    return(df3)