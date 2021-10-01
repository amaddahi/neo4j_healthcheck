from bin import globals
from bin import delete_tmpfile
import pytz
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
#from matplotlib.backends.backend_pdf import PdfPages
#import matplotlib.pyplot as plt

def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


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
      pdf.cell(40,8, 'Neo4j Historical Performance Metrics Report',0,1)
      pdf.set_font('Arial', 'B', 16)
      pdf.cell(40,8,globals.customer,0,1)
      #pdf.cell(40,8,' ',0,1)
      pdf.set_font('Arial', '', 11)
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
       #pdf.alias_nb_pages()
    
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
           pdf.multi_cell(0, 2, r_line,0,'L',0)

    
       # save the pdf with name .pdf
       pdf.output(globals.results_file_pdf)
    
       #globals.pp.close()
    
       import glob

       m_pdf_file_path= globals.results_directory + "/m_*.pdf"
       m_pdf_files = []
       for file in glob.glob(m_pdf_file_path):
             m_pdf_files.append(file)

       merger = PdfFileMerger()
   
       merger.append("/tmp/title_page.pdf")
       merger.append(globals.results_file_pdf)

       for metric_category in ('query','store','count','object','transaction','cypher',"cypher","page_cache","check_point","jvm_gc",'bolt','operation' ):
           metric_category_plot_file=globals.results_directory + "/m_" + metric_category + ".pdf"
           if metric_category_plot_file in m_pdf_files:
                merger.append(metric_category_plot_file)

       #for pdf in m_pdf_files:
          #print(">>>>>>>>>>> " + pdf)
          #merger.append(pdf)
   
       merger.write(globals.combined_results_plot_pdf)
       merger.close()
    
       delete_tmpfile.run("allcharts.pdf")
       delete_tmpfile.run(globals.results_file_pdf)




class PDF(FPDF):
    def header(self):
        # Logo
        self.image('logo_pb.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

## Instantiation of inherited class
#pdf = PDF()
#pdf.alias_nb_pages()
#pdf.add_page()
#pdf.set_font('Times', '', 12)
#for i in range(1, 41):
    #pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
#pdf.output('tuto2.pdf', 'F')

