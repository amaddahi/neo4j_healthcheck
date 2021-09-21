from bin import globals
import warnings

import pandas as pd

def run(df, timezone):
    warnings.simplefilter(action='ignore', category=FutureWarning)
    if timezone == "UTC":
        df['date'] = pd.to_datetime(df['date'], unit='s')
    return df
