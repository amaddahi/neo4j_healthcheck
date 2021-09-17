from bin import globals
from bin import get_filenames
from bin import merge_csv_files
from bin import convert_epoch_to_timestamp
import os
import pandas as pd
#import numpy as np



def run(start_date, end_date, metric_category):

    df2=False
    filenames = get_filenames.run(metric_category)

    if globals.debug:
        print(">>>>IN pre-process files:  Names of files retrieved by get_filenames")
        print(filenames)
        print("-------------------------------")
    #
    # Paste multiple csv files into a single file for the same metric category
    #
    (filetmp,check_point_duration_metric_filetmp) = merge_csv_files.run(filenames, metric_category)

    if globals.debug:
         print("********************")
         print("check_point_duration_metric_filetmp: ", check_point_duration_metric_filetmp)
         print("filetmp: ", filetmp)
         print("********************")
    #
    # Read the merged file with epoch timestamp into a dataframe
    #
    df = pd.read_csv(filetmp)
    if check_point_duration_metric_filetmp:
        df2 = pd.read_csv(check_point_duration_metric_filetmp)

    #df = pd.read_csv(filetmp, parse_dates=['date'], date_parser=lambda epoch: pd.to_datetime(epoch, unit='s'))

    os.system("rm " + filetmp)

    if globals.debug:
        df.to_csv(metric_category + "_0.csv")

    #
    # Change epoch to UTC timestamp
    #
    df = convert_epoch_to_timestamp.run(df, 'UTC')
    if check_point_duration_metric_filetmp:
        df2 = convert_epoch_to_timestamp.run(df2, 'UTC')

    if globals.debug:
        df.to_csv(metric_category + "_1.csv")


    #
    # drop any rows with null values - indicating mismatched enddates
    #
    df = df.dropna()
    if check_point_duration_metric_filetmp:
        df2 = df2.dropna()

    if globals.debug:
        df.to_csv(metric_category + "_2.csv")

    if check_point_duration_metric_filetmp:
       #return df,df2
       os.system("rm " + check_point_duration_metric_filetmp)
    #else:
       #return df


    return df,df2

