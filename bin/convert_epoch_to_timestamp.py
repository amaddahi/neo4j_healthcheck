from bin import globals
import pandas as pd

def run(df, timezone):
    if timezone == "UTC":
        df['date'] = pd.to_datetime(df['date'], unit='s')
    return df
