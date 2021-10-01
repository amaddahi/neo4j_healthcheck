from bin import globals
from bin import get_metric_category_abbr
from bin import get_filenames
import re
import numpy as np
import warnings


def run(interval, df, df_org, metric_category):

    warnings.simplefilter(action='ignore', category=FutureWarning)
    #print(list(df))

    filenames = get_filenames.run(metric_category)

    (metric_category_abbr, db_category_abbr) = get_metric_category_abbr.run(metric_category)

    if globals.debug:
        print("Inside cumulative timing....")
        print(" ")

    for file in filenames:
        #if metric_category in ('cypher'):
        if metric_category in ('cypher','jvm_gc','check_point'):
            file_token_name = file[3]
        else:
            file_token_name = file[0]

        x1 = re.sub(db_category_abbr + metric_category +
                    '.', metric_category_abbr, file_token_name)
        # x2 = re.sub('.csv','', x1)
        val_label = re.sub('.csv', '', x1)
        # val_label = re.sub('metrics/','', x2)
        val_label = val_label + file[2]

        if file[1] == 2:   # Example: ["neo4j." + globals.database + ".check_point.total_time.csv", 2, "", "neo4j.check_point.total_time.csv"]

            df[val_label] = np.ceil(df[val_label].diff()).fillna(0)

            #if metric_category == 'bolt':
            #df[val_label] = np.ceil(df[val_label].diff()/(df_org["blt.messages_done-ps"].diff())).fillna(0)

            if metric_category == 'jvm_gc':
                df["Total_GC_pause_time-ms"]= np.ceil(df['vm.gc.time.g1_young_generation'] +  df['vm.gc.time.g1_old_generation']).fillna(0).astype(int)

            # Set negative diffs (due to restarts) to zero
            df[val_label][df[val_label] < 0] = 0

    df = df.dropna()

    if globals.debug:
        print("Exiting cumulative timing....")
        print(" ")

    return df
