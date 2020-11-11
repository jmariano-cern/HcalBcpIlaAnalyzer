#!/usr/bin/python

# import the IlaData object
from IlaData import IlaData
# import python os interface to list directories
from os import listdir

# analyze each file in this directory
data_dir = "/home/jomarian/ila_data"
# save analysis results here
analysis_dir = "/home/jomarian/analysis"
# check for these signals in each file
# it is fine if not all signals are present in a given file
rxdata_signals = [
    "hb0_gtwiz_userdata_rx_int_1[15:0]" ,
    "hb1_gtwiz_userdata_rx_int_1[15:0]" ,
    "hb2_gtwiz_userdata_rx_int_1[15:0]" ,
    "hb3_gtwiz_userdata_rx_int_1[15:0]" ,
]

# loop over files in the data directory
for data_file in listdir(data_dir):
    # get full path for each file
    data_file_path = data_dir+'/'+data_file
    # print update to terminal
    print "Analyzing: "+ data_file_path
    # create an IlaData object for the file
    analyzer = IlaData(data_file_path)
    # set the oputput directory for the new analyzer
    analyzer.analysis_dir = analysis_dir
    # set the rxdata signals for the new analyzer
    analyzer.rxdata_signals = rxdata_signals
    # run the analysis
    analyzer.full_analyze()
