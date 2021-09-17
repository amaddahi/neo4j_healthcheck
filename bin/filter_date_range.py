from bin import globals
import pandas as pd

def run(start_date, end_date, df, interval, periods, options, check_point_duration):

    #
    # if no options are specified, gather stats for the last 24 hours with available data
    #

    start_date_min = df.date.min()
    end_date_max = df.date.max()

    #print(delta)
    #print(interval)
    #print(start_date)
    #print(end_date)

    
    if options is False:
        start_date = df.date.min()
        end_date = df.date.max()
        start_date = end_date - pd.to_timedelta("1day")

    elif (start_date == None):
        if (end_date == None):
            end_date = df.date.max()

        if interval == 'S':
            delta = str(periods)+"S"
        elif interval == 'Min':
            delta = str(periods)+"min"
        elif interval == 'H':
            delta = str(periods)+"hour"
        elif interval == 'D':
            delta = str(periods)+"D"
        elif interval == 'W':
            delta = str(periods)+"W"
        elif interval == 'Y':
            delta = str(periods)+"Y"

        #print(delta)
        #print(end_date)
        
        start_date = pd.Timestamp(end_date) - pd.to_timedelta(delta)

    elif (start_date != None and end_date == None):
        if interval == 'S':
            delta = str(periods)+"S"
        elif interval == 'Min':
            delta = str(periods)+"min"
        elif interval == 'H':
            delta = str(periods)+"hour"
        elif interval == 'D':
            delta = str(periods)+"D"
        elif interval == 'W':
            delta = str(periods)+"W"
        elif interval == 'Y':
            delta = str(periods)+"Y"
        end_date = pd.Timestamp(start_date) + pd.to_timedelta(delta)

    if not check_point_duration:
          print ('min_startdate:           ', pd.Timestamp(start_date_min))
          print ('max_enddate:             ', pd.Timestamp(end_date_max))
          print ('')
          print ('search_startdate:        ', pd.Timestamp(start_date))
          print ('search_enddate:          ', pd.Timestamp(end_date))
          print ('')
          print ('')

    if ( pd.Timestamp(start_date) > pd.Timestamp(end_date_max) ):
         print(" ")
         print(" ")
         print ("Exiting:  Invalid Start Search Date(" +  str(pd.Timestamp(start_date)) + ") is outside of the Max range of available metrics(" + str(pd.Timestamp(end_date_max)) + ")" )
         print(" ")
         print(" ")
         return 1

    if ( pd.Timestamp(end_date) < pd.Timestamp(start_date_min) ):
         print(" ")
         print(" ")
         print ("Exiting:  Invalid Start Search Date(" +  str(pd.Timestamp(start_date)) + ") is outside of the Max range of available metrics(" + str(pd.Timestamp(end_date_max)) + ")" )
         print(" ")
         print(" ")
         return 1

    if ( pd.Timestamp(end_date) > pd.Timestamp(end_date_max) ):
         df = df[df.date < end_date_max]
    else:
         df = df[df.date < end_date]

    if ( pd.Timestamp(start_date) < pd.Timestamp(start_date_min) ):
         df = df[df.date > start_date_min]
    else:
         df = df[df.date > start_date]

    return df
