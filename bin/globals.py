
def initialize():

    global version
    global verbose
    global database


    global host_ip
    global db_user
    global db_pwd
    global neo4j_home
    global working_directory
    global metrics_directory
    global logs_directory
    global bin_directory
    global conf_directory
    global data_directory
    global results_directory
    global results_file_txt
    global results_file_pdf
    global docker
    global metrics_csv_interval
    global all_csv_filename
    global process_metrics
    global dbms_mode
    global bolt_port
    global checkdb
    global display_precision
    global debug
    global customer
    global interval_string
    global admin_report_directory
    global pp
    global fo
    global combined_results_plot_pdf
    global plot_file_pdf
    global long_running_query_file 
    global long_running_query_sorted_file 

    version = '2.0'
    verbose = False
    database = "system"
   
    #host_ip = "72.211.24.138"
    #host_ip = "192.168.65.2"
    host_ip = "localhost"
    pp = None
    db_user = None
    db_pwd = None
    neo4j_home = None
    working_directory = None
    combined_results_plot_pdf = None
    plot_file_pdf = "allcharts.pdf"
    metrics_directory=None
    logs_directory = None
    bin_directory = None
    conf_directory = None
    data_directory = None
    admin_report_directory= None 
    results_directory = None
    results_file_txt = None
    results_file_pdf = None
    docker = None
    metrics_csv_interval = 3  # seconds
    all_csv_filename = "nj_perf.csv"
    process_metrics = None
    dbms_mode = None
    bolt_port = 7687
    checkdb = None
    display_precision=None
    debug = None
    customer = None
    interval_string = None
    
