#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

#df = pd.DataFrame([[5.1, 3.5, 0], [4.9, 3.0, 0], [7.0, 3.2, 1], [6.4, 3.2, 1], [5.9, 3.0, 2]], columns=['length', 'width', 'species'])

df = pd.read_csv("oo.log")

print(df)

with PdfPages('multipage_pdf.pdf') as pdf:

    #df.plot.scatter(x='t', y='duration', c='DarkBlue') 
    df.plot.scatter(x='t', y='duration', c='DarkBlue') 

    #df.plot.scatter()
    #df.plot()
    pdf.savefig()
    plt.close()

    #df.plot(kind='bar')
    #df.plot(style='.-')
    #pdf.savefig()
    #plt.close()

