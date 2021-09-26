
from bin import globals
from bin import normalize_stats
from bin import get_filenames
from bin import apply_output_projection
from bin import print_dataframe
from bin import plot_metric
from bin import convert_txt_pdf
from bin import pre_process_files
from bin import get_admin_report_env
import warnings

import os
from bin import usage
from bin import filter_date_range
import pandas as pd
from bin import process_cumulative_counters
from bin import process_cumulative_timings
import numpy as np

def run(start_date, end_date, metric_category, interval, periods, options):

    warnings.simplefilter(action='ignore', category=FutureWarning)
    msgx="################################################" + "\n"
    msg= "Summarizing Stats:  " + metric_category

    globals.category_file_exists=1
    # TODO
    if metric_category == 'network':
       #for file in os.listdir(metrics_directory):
           #if fnmatch.fnmatch(file, "*causal_clustering*"):
               msg = msg + "  --> Collected for HA clusters only"
               print_dataframe.run2(0, "\n" + msgx + " \n" + msg + " \n ")
               return
    elif metric_category == 'check_point':
               msg = msg + "(ms)"  
               print_dataframe.run2(0, "\n" + msgx + " \n" + msg + " \n ")
               #return
    elif metric_category == 'store':
               msg = msg + "(MB)"  
               print_dataframe.run2(0, "\n" + msgx + " \n" + msg + " \n ")
    elif metric_category == 'query':
               msg="Long Running Queries"
               print_dataframe.run2(0, "\n" + msgx + " \n" + msg + " \n ")
               if (globals.admin_report_directory != None ):
                   get_admin_report_env.run()
                   get_admin_report_env.admin_report_check()
               else:
                   msg = "\n" + "Note:  Will not run list of long running queries as Admin Report Directory Not Provided" + "\n"
                   print_dataframe.run2(0, "\n" + msgx + " \n" + msg + " \n ")
                   #usage.run("query")
               return

    elif metric_category == 'causal_clustering':
       if not os.path.exists(globals.metrics_directory + '*causal_clustering*'):
               dbms_mode='CORE'
               return
    else:
       print_dataframe.run2(0, "\n" + msgx + " \n" + msg + " \n ")

    # skip category processing if no matching files found (i.e metric category not turned ON)
    globals.category_file_exists=len(get_filenames.run(metric_category))
    if globals.category_file_exists == 0:
        return

    print (" ")
    print (" ")
    (df,df2) = pre_process_files.run(start_date, end_date, metric_category)

    if globals.debug:
        df.to_csv(metric_category + "11.csv")
        #df2.to_csv(metric_category + "12.csv")

    # can this be moved to main?
    #
    if start_date == None and end_date == None:
        aggr_interval = "H"

    df = filter_date_range.run(start_date, end_date, df, interval, periods, options,False)
    if isinstance(df2 , pd.DataFrame):
        check_point_duration=True
        df2 = filter_date_range.run(start_date, end_date, df2, interval, periods, options,check_point_duration)

    if not isinstance(df, pd.DataFrame):
        if df==1:
            return

    df_org=df

    if globals.debug:
        df.to_csv(metric_category + "_df_filtered_date_2.csv")
        # print_dataframe.run(df.tail(5))

    df = process_cumulative_counters.run(interval, df, metric_category)

    if globals.debug:
        df.to_csv(metric_category + "_df_cumu_cntr_3.csv")

    df = process_cumulative_timings.run(interval, df, df_org, metric_category)

    if globals.debug:
        df.to_csv(metric_category + "_df_cumu_time_4.csv")

    if options is False:
        interval = "H"

    df = df.replace([np.inf, -np.inf], np.nan)

    #print_dataframe(df.head(5))
    #print(df.index.tolist())

    #df = np.ceil(df.groupby(pd.Grouper(key='date', freq=interval)).agg( [('Sum', 'sum') , ('Count', 'count'), ('Avg', 'mean'), ('Max', 'max')] )).fillna(0).astype(int)
    df = (df.groupby(pd.Grouper(key='date', freq=interval)).agg( [('Sum', 'sum') , ('Count', 'count'), ('Avg', 'mean'), ('Max', 'max')] )).fillna(0)

    #print_dataframe(df.tail(15).T)
    if isinstance(df2 , pd.DataFrame):
          df2 = (df2.groupby(pd.Grouper(key='date', freq=interval)).agg( [('Sum', 'sum') , ('Count', 'count'), ('Avg', 'mean'), ('Max', 'max')] )).fillna(0)


    #df.to_csv(metric_category + "avg-max-5.csv")

    # Reformat dataframe column labels
    #
    df.columns = ["_".join(x) for x in df.columns.ravel()]
    if isinstance(df2 , pd.DataFrame):
         df2.columns = ["_".join(x) for x in df2.columns.ravel()]

    #print(list(df))

    df = normalize_stats.run(df,metric_category)

    # When aggregating by the seconds, remove dataframe columns where all different metrics are zero
    #
    if interval in ('S','Min'):
       df=df[(df.sum(axis=1) != 0)]

    if globals.debug:
        print (" ")
        print (df.T)
        print (" ")

    # only applies to check_point duration
    if isinstance(df2 , pd.DataFrame):
        df = df.merge(df2,how='left', left_on='date', right_on='date')

    #if globals.debug:
        #print_dataframe(df.tail(15).T)

    df = apply_output_projection.run(df,metric_category)

    #print_dataframe.run(df.tail(15).T)
    print_dataframe.run2(df.tail(15).T,"xxxxxxxxxxxx")

    # TODO - check this
    #
    if globals.process_metrics == 'all':
        csv_filename = globals.results_directory + "/" + globals.all_csv_filename
        df.to_csv(csv_filename,mode='a')
    else:
        csv_filename = globals.results_directory + "/" + metric_category + ".csv"
        df.to_csv(csv_filename)

    plot_metric.run(df, metric_category)

    convert_txt_pdf.run2()
