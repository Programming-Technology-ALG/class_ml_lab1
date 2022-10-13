import pandas as pd

def add_early_wakeup(df)-> pd.DataFrame:
    if df['wakeup_time'] < 6: df['early_wakeup'] = True
    return df