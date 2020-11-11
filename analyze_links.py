#!/usr/bin/python

from IlaData import IlaData
from os import listdir

data_dir = "/home/jomarian/ila_data"

for data_file in listdir(data_dir):
    data_file_path = data_dir+'/'+data_file
    print "Analyzing: "+ data_file_path
    analyzer = IlaData(data_file_path)
    analyzer.analysis_dir="/home/jomarian/analysis"
    analyzer.full_analyze()

