from bin import globals
from bin import get_filenames
from bin import get_plot_group
from bin import check_min_max
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

def run(df, metric_category):

    SMALL_SIZE = 5
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 12
    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=SMALL_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    #matplotlib.rc('font', size=SMALL_SIZE)
    #matplotlib.rc('axes', titlesize=SMALL_SIZE)

    # check if we have enough data points for a plot  ( need >= 2)
    #

    if check_min_max.run(df):

        #filenames = get_filenames.run(metric_category)
        column_names = list(df)
        plot_group = get_plot_group.run(metric_category)

        #print(column_names)
        #print(plot_group)
        #print("----------------")

        if globals.debug:
            print("---------------------------------------")
            print(plot_group)
            print("---------------------------------------")

        pdf_filename = globals.results_directory + "/m_" + metric_category + ".pdf"

        #with PdfPages(metric_category + ".pdf") as pdf:

        with PdfPages(pdf_filename) as pdf:


            for plot_x in plot_group:
                # print ("GRAPH: " + str(i))
                # i=1
                plot_keep_list = []
                for item in plot_x:
                    for col in column_names:
                        if item in col:
                            plot_keep_list.append(col)

                # Skip the plotting for this metric - means no input file was found earlier
                #
                if not plot_keep_list:
                   print(df)
                   print ("No input file out???")
                   print(df)
                   continue

                plot_delete_list = list(set(column_names) - set(plot_keep_list))


                if metric_category=='query':
                    df_plot=df
                    df_plot.plot.scatter(x='t', y='Duration', c='DarkBlue')
                else:
                    df_plot = df.drop(plot_delete_list, 1, errors='ignore')
                    df_plot.plot()
                plt.title(metric_category)
                pdf.savefig()
                plt.close()


def run2(df,metric_category):

    import matplotlib
    import matplotlib.pyplot as plt

    SMALL_SIZE = 5
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 12
    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=SMALL_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    #matplotlib.rc('font', size=SMALL_SIZE)
    #matplotlib.rc('axes', titlesize=SMALL_SIZE)

    df = pd.read_csv("/tmp/qqq.all")

    df['t'] = pd.to_datetime(df['t'], format="%Y-%m-%d %H:%M")
    #print(df.head(5))

    pdf_filename = globals.results_directory + "/m_" + metric_category + ".pdf"

    #with PdfPages('multipage_pdf.pdf') as pdf:
    with PdfPages(pdf_filename) as pdf:

        df.plot.scatter(x='t', y='duration',s=2)
        plt.title(metric_category)
        pdf.savefig()
        plt.close()