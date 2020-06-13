import pandas as pd
import numpy as np


def in_year(dateTime, year):
    """
    input: dateTime object
           year (int)
    output: True if dateTime is in year
            False if otherwise
    """
    if dateTime.year == year:
        return True
    else:
        return False
    


def filter_data_by_year(rp_sale_df, year):
    """
    Input: rp_sale_df - DataFrame created from the EXTR_RPSale.csv, 
           year - A specified year to filter with (must be int)
    Output: DataFrame containing only entries from the specified year
    """
    #convert DocumentDate column to datetime
    rp_sale_df['DocumentDate'] = pd.to_datetime(rp_sale_df['DocumentDate'])
    
    #create a mask
    mask = rp_sale_df['DocumentDate'].apply(lambda date: in_year(date, year))
    
    return rp_sale_df[mask]

def create_2019_sale_csv(rp_sale_df):
    new_df = filter_data_by_year(rp_sale_df, 2019)
    new_df.to_csv('../../data/EXTR_RPSale_2019.csv')
    