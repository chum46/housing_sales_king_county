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
    
    
def add_PIN_column(df):
    """
    input: dataframe with Major and Minor columns
    output: dataframe with PIN column added
    """
    # turn the major and minor columns into strings
    df['Major'] = df['Major'].apply(str)
    df['Minor'] = df['Minor'].apply(str)
    
    # pad each column with zeros
    df['Major'] = df['Major'].apply(lambda elem: elem.rjust(6, '0'))
    df['Minor'] = df['Minor'].apply(lambda elem: elem.rjust(4, '0'))
    
    #create pin column
    PIN = df['Major'] + df['Minor']
    df['PIN'] = PIN
    return df

def filter_data_by_PIN(original_df):
    """
    input: the name of a csv file that is in your /data/ folder
    outup: a dataframe containing only the entries connected to sales of single building parcels in 2019
    """
    #import PINS dataframe
    PINS = pd.read_csv('../../data/PINS.csv',dtype={'PIN':'string'}, index_col=0)
    #check if the file has a PIN column, this is needed for filtering. If not, creates one
    if 'PIN' in original_df.columns:
        return original_df.join(PINS, how='inner', on='PIN')
    else:
        df = add_PIN_column(original_df)
        return df.join(PINS, how='inner', on='PIN')