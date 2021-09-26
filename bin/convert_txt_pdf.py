from bin import globals
from bin import delete_tmpfile
import pytz
import matplotlib.pyplot as plt
import warnings

import pandas as pd
import numpy as np
import sys
import getopt
import time
import os
import dateutil
import re
import datetime
import fnmatch
import subprocess
import string
from os import listdir
from configobj import ConfigObj
from fpdf import FPDF
from PyPDF2 import PdfFileMerger
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

def run():

   warnings.simplefilter(action='ignore', category=FutureWarning)
   # save FPDF() class into
   # a variable pdf
   pdf = FPDF()

   # Add a page
   pdf.add_page()


   # set style and size of font
   # that you want in the pdf
   pdf.set_font("Courier", size = 5)

   # open the text file in read mode
   f = open(results_file_txt, "r")

   # insert the texts in pdf
   for x in f:
       pdf.cell(300, 2, txt = x, ln = .3, align = 'L')

   # save the pdf with name .pdf
   pdf.output(results_file_pdf)


def add_title_page():
     
      pdf = FPDF()
      pdf.add_page()

      pdf.image('resources/neo4j.png', 10, 40, 191)

      pdf.set_font('Arial', 'B', 25)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,10, ' ',0,1)
      pdf.cell(40,5, ' ',0,1)
      pdf.cell(40,8, 'Neo4j Performance Summary Report',0,1)
      pdf.set_font('Arial', 'B', 18)
      pdf.cell(40,8,globals.customer,0,1)
      #pdf.cell(40,8,' ',0,1)
      pdf.set_font('Arial', 'B', 12)
      pdf.cell(40,8,time.strftime('%Y-%m-%d',time.localtime()),0,1)
      pdf.output('/tmp/title_page.pdf', 'F')
      pdf.close()

def run2():

       add_title_page()

       warnings.simplefilter(action='ignore', category=FutureWarning)
       # save FPDF() class into a variable pdf
       pdf = FPDF()
   
       # Add a page
       pdf.add_page()
    
       # set style and size of font that you want in the pdf
       #pdf.set_fill_color(r=220, g=220, b=220)
       pdf.set_font("Courier", size = 5)
    
       #print(">>>>>In convert_txt_pdf - result_file_txt:" + globals.results_file_txt )
       #print(">>>>>In convert_txt_pdf - results_file_pdf:" + globals.results_file_pdf )
       #print(">>>>>In convert_txt_pdf - combined_results_plot_pdf:" + globals.combined_results_plot_pdf)

       # open empty text file in read mode
       f_result_file_text = open(globals.results_file_txt, "r")

       # insert the texts in pdf
       for r_line in f_result_file_text:
           pdf.cell(300, 2, txt = r_line, ln = .3, align = 'L')
           #pdf.multi_cell(350, 2, x, align = 'L', fill=True)
           #200, 40, $reportSubtitle, 1

    
       # save the pdf with name .pdf
       pdf.output(globals.results_file_pdf)
    
       #globals.pp.close()
    
       import glob

       m_pdf_file_path= globals.results_directory + "/m_*.pdf"
       m_pdf_files = []
       for file in glob.glob(m_pdf_file_path):
             m_pdf_files.append(file)
       #print (m_pdf_files)

       merger = PdfFileMerger()
   
       merger.append("/tmp/title_page.pdf")
       merger.append(globals.results_file_pdf)

       for pdf in m_pdf_files:
          #print(">>>>>>>>>>> " + pdf)
          merger.append(pdf)
   
       merger.write(globals.combined_results_plot_pdf)
       merger.close()
    
       delete_tmpfile.run("allcharts.pdf")
       delete_tmpfile.run(globals.results_file_pdf)
