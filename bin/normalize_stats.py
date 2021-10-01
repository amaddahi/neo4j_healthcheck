from bin import globals

def run(df, metric_category):

    if (metric_category == 'bolt') :
                df["blt.accumulated_processing_time_Avg"] = (df["blt.accumulated_processing_time_Avg"]/(df["blt.messages_done-ps_Avg"])).fillna(0)
                df["blt.accumulated_processing_time_Max"] = (df["blt.accumulated_processing_time_Max"]/(df["blt.messages_done-ps_Avg"])).fillna(0)
                df["blt.accumulated_queue_time_Avg"] = (df["blt.accumulated_queue_time_Avg"]/(df["blt.messages_done-ps_Avg"])).fillna(0)
                df["blt.accumulated_queue_time_Max"] = (df["blt.accumulated_queue_time_Max"]/(df["blt.messages_done-ps_Avg"])).fillna(0)
    elif (metric_category == 'cypher') :
                # TODO
                df["cyp.replan_events-ps_Sum"] = (df["cyp.replan_events-ps_Sum"]*globals.metrics_csv_interval).fillna(0)
                df["cyp.replan_events-ps_Avg"] = (df["cyp.replan_events-ps_Avg"]*globals.metrics_csv_interval).fillna(0)
                df["cyp.replan_events-ps_Max"] = (df["cyp.replan_events-ps_Max"]*globals.metrics_csv_interval).fillna(0)
                #df["cyp.replan_wait_time_Avg"] = (df["cyp.replan_wait_time_Avg"]/(df["cyp.replan_events-ps_Avg"])).fillna(0)
                df["cyp.replan_wait_time_Avg"] = (df["cyp.replan_wait_time_Avg"]).fillna(0)
                #df["cyp.replan_wait_time_Max"] = (df["cyp.replan_wait_time_Max"]/(df["cyp.replan_events-ps_Avg"])).fillna(0)
                df["cyp.replan_wait_time_Max"] = (df["cyp.replan_wait_time_Max"]).fillna(0)

    return df
