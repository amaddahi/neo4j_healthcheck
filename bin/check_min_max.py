from bin import globals

def run(df):
    ok_to_print=None
    if len(df.index) == 1:
        print(' ')
        print ('WARNING: Not enough Data to plot (date.min=date.max), please wait for more data to be captured! ')
        print(' ')
        ok_to_print=False
    else:
        ok_to_print=True
    return ok_to_print

