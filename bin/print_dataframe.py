from bin import globals
import warnings

import sys
import pandas as pd

def run2(df,msg):

    warnings.simplefilter(action='ignore', category=FutureWarning)
    #global display_precision
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 700)
    pd.set_option('display.width', 1000)
    #new_df=df.style.set_properties(subset=['date'], **{'width-min': '1000px'})
    #print(new_df)

    if globals.display_precision:
       pd.options.display.float_format = '{:,.1f}'.format
       df.to_csv('results.txt', sep='\t', index=True)
    else:
       pd.options.display.float_format = '{:,.0f}'.format
       #df.to_csv('results.txt', sep='\t', index=True)
       #np.savetxt('results2.txt', df.values, fmt='%d')
       #df.to_csv('results3.txt', header=True, index=True, sep='\t',float_format='%.0f')

    # TODO: Add results_directory to full path
    with open(globals.results_file_txt, 'a') as globals.fo:
           #if 00instance(df, pd.DataFrame):
           if isinstance(df, pd.DataFrame):
              globals.fo.write('\n')
              globals.fo.write(df.__repr__())
              globals.fo.write('\n')
              globals.fo.write('\n')
              print(df)
           else:
               print(msg)
               #msg=msg+'\n'
               globals.fo.write(msg)
    #print('\n')

    sys.stdout.flush()



def run(df):
    warnings.simplefilter(action='ignore', category=FutureWarning)

    #global display_precision
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 700)
    pd.set_option('display.width', 1000)
    if globals.display_precision:
       pd.options.display.float_format = '{:,.1f}'.format
    else:
       pd.options.display.float_format = '{:,.0f}'.format
    print(df)
    print('')
    print('')


def print_dataframe(df):
    warnings.simplefilter(action='ignore', category=FutureWarning)

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 700)
    pd.set_option('display.width', 1000)
    if globals.display_precision:
       pd.options.display.float_format = '{:,.1f}'.format
       df.to_csv('results.txt', sep='\t', index=True)
    else:
       pd.options.display.float_format = '{:,.0f}'.format
       #df.to_csv('results.txt', sep='\t', index=True)
       #np.savetxt('results2.txt', df.values, fmt='%d')
       #df.to_csv('results3.txt', header=True, index=True, sep='\t',float_format='%.0f')

    # TODO: Add results_directory to full path
    with open(results_file_txt, 'w') as fo:
               fo.write(df.__repr__())

    print(df)
    print('')
    print('')

    sys.stdout.flush()
