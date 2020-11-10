#!/usr/bin/python

import matplotlib.pyplot as plt
from numpy import add as vectoradd
from numpy import add as vectoradd
from numpy import mean,std
import os

class IlaData:
    def __init__(self,datafile_path):
        self.headerline_num=0
        self.radixline_num=1
        self.placeholder_word='f7fb'
        self.frameword='bc'
        self.framelength=24
        self.rxdata_signals = [
            "hb0_gtwiz_userdata_rx_int_1[15:0]" , 
            "hb1_gtwiz_userdata_rx_int_1[15:0]" , 
            "hb2_gtwiz_userdata_rx_int_1[15:0]" , 
            "hb3_gtwiz_userdata_rx_int_1[15:0]" , 
        ]
        #   "datatype"   : (lowest_bit,highest_bit+1)
        self.framedict = {
            "Comma"      : (0,8)   ,
            "isAnyTDC63" : (8,9)   ,
            "isAnyTDC62" : (9,10)  ,
            "isAnyTDC59" : (10,11) ,
            "isAnyTDC58" : (11,12) ,
            "CapID"      : (12,14) ,
            "CapErr"     : (14,15) ,
            "TDCbad"     : (15,16) ,
            "QIE_ADC0"   : (16,24) ,
            "QIE_ADC1"   : (24,32) ,
            "QIE_ADC2"   : (32,40) ,
            "QIE_ADC3"   : (40,48) ,
            "QIE_ADC4"   : (48,56) ,
            "QIE_ADC5"   : (56,64) ,
            "QIE_ADC6"   : (64,72) ,
            "QIE_ADC7"   : (72,80) ,
            "TDC3"       : (80,82) ,
            "TDC2"       : (82,84) ,
            "TDC1"       : (84,86) ,
            "TDC0"       : (86,88) ,
            "TDC7"       : (88,90) ,
            "TDC6"       : (90,92) ,
            "TDC5"       : (92,94) ,
            "TDC4"       : (94,96) ,
        }
        #   "datatype" : (bin_min,bin_max,nbins)
        self.bin_limits = {
            "Comma"      : (0,255,256) ,
            "isAnyTDC63" : (0,1,2)     ,
            "isAnyTDC62" : (0,1,2)     ,
            "isAnyTDC59" : (0,1,2)     ,
            "isAnyTDC58" : (0,1,2)     ,
            "CapID"      : (0,3,4)     ,
            "CapErr"     : (0,1,2)     ,
            "TDCbad"     : (0,1,2)     ,
            "QIE_ADC0"   : (0,255,32)  ,
            "QIE_ADC1"   : (0,255,32)  ,
            "QIE_ADC2"   : (0,255,32)  ,
            "QIE_ADC3"   : (0,255,32)  ,
            "QIE_ADC4"   : (0,255,32)  ,
            "QIE_ADC5"   : (0,255,32)  ,
            "QIE_ADC6"   : (0,255,32)  ,
            "QIE_ADC7"   : (0,255,32)  ,
            "TDC3"       : (0,3,4)     ,
            "TDC2"       : (0,3,4)     ,
            "TDC1"       : (0,3,4)     ,
            "TDC0"       : (0,3,4)     ,
            "TDC7"       : (0,3,4)     ,
            "TDC6"       : (0,3,4)     ,
            "TDC5"       : (0,3,4)     ,
            "TDC4"       : (0,3,4)     ,
        }
        #   "datatype" : (mean_min,mean_max)
        self.mean_limits = {
            "Comma"      : (188.0,188.0) ,
            "isAnyTDC63" : (0.0,0.0) ,
            "isAnyTDC62" : (0.0,0.0) ,
            "isAnyTDC59" : (0.0,0.0) ,
            "isAnyTDC58" : (0.0,0.0) ,
            "CapID"      : (1.4,1.6) ,
            "CapErr"     : (0.0,0.0) ,
            "TDCbad"     : (0.0,0.0) ,
            "QIE_ADC0"   : (3.0,6.0) ,
            "QIE_ADC1"   : (3.0,6.0) ,
            "QIE_ADC2"   : (3.0,6.0) ,
            "QIE_ADC3"   : (3.0,6.0) ,
            "QIE_ADC4"   : (3.0,6.0) ,
            "QIE_ADC5"   : (3.0,6.0) ,
            "QIE_ADC6"   : (3.0,6.0) ,
            "QIE_ADC7"   : (3.0,6.0) ,
            "TDC3"       : (3.0,3.0) ,
            "TDC2"       : (3.0,3.0) ,
            "TDC1"       : (3.0,3.0) ,
            "TDC0"       : (3.0,3.0) ,
            "TDC7"       : (3.0,3.0) ,
            "TDC6"       : (3.0,3.0) ,
            "TDC5"       : (3.0,3.0) ,
            "TDC4"       : (3.0,3.0) ,
        }
        #   "datatype" : (std_min,std_max)
        self.std_limits = {
            "Comma"      : (0.0,0.0) ,
            "isAnyTDC63" : (0.0,0.0) ,
            "isAnyTDC62" : (0.0,0.0) ,
            "isAnyTDC59" : (0.0,0.0) ,
            "isAnyTDC58" : (0.0,0.0) ,
            "CapID"      : (1.0,1.2) ,
            "CapErr"     : (0.0,0.0) ,
            "TDCbad"     : (0.0,0.0) ,
            "QIE_ADC0"   : (0.0,1.5) ,
            "QIE_ADC1"   : (0.0,1.5) ,
            "QIE_ADC2"   : (0.0,1.5) ,
            "QIE_ADC3"   : (0.0,1.5) ,
            "QIE_ADC4"   : (0.0,1.5) ,
            "QIE_ADC5"   : (0.0,1.5) ,
            "QIE_ADC6"   : (0.0,1.5) ,
            "QIE_ADC7"   : (0.0,1.5) ,
            "TDC3"       : (0.0,0.0) ,
            "TDC2"       : (0.0,0.0) ,
            "TDC1"       : (0.0,0.0) ,
            "TDC0"       : (0.0,0.0) ,
            "TDC7"       : (0.0,0.0) ,
            "TDC6"       : (0.0,0.0) ,
            "TDC5"       : (0.0,0.0) ,
            "TDC4"       : (0.0,0.0) ,
        }
        self.analysis_dir="./analysis"
        self.datafile_path=datafile_path
        self.get_datafile_name()
        self.get_raw_data()
        self.get_headers()
        self.get_radices()
        self.get_decode_dict()
        self.get_data()
        self.get_rxdata()

    def get_datafile_name(self):
        self.datafile_name = self.datafile_path.split('/')[-1].split('.')[0]
        
    def get_raw_data(self):
        data_file=open(self.datafile_path,'r')
        self.raw_data=data_file.readlines()
        data_file.close()
    
    def get_headers(self):
        headerline = self.raw_data[self.headerline_num].strip()
        self.headers=headerline.split(',')

    def get_radices(self):
        radixline = self.raw_data[self.radixline_num].strip()
        self.radices=radixline.split('- ')[1].split(',')

    def get_decode_dict(self):
        self.decode_dict = {}
        for headernum,header in enumerate(self.headers):
            self.decode_dict[header] = self.radices[headernum]

    def get_data(self):
        self.data={}
        for header in self.headers:
            self.data[header] = []
        for line_num,dataline in enumerate(self.raw_data):
            if (line_num != self.headerline_num) and (line_num != self.radixline_num):
                for colnum,header in enumerate(self.headers):
                    self.data[header].append(dataline.split(',')[colnum])

    def invert_word(self,wordin):
        return wordin[2:4]+wordin[0:2]

    def invert_words(self,signal_name):
        inverted_data=""
        for wordnum in range(0,len(self.data[signal_name])):
            inverted_data=inverted_data + self.invert_word(self.data[signal_name][wordnum])
        return inverted_data

    def trim_placeholders(self,data):
        placeholder_pos=data.find(self.placeholder_word)
        if (placeholder_pos > 0):
            data=data[0:placeholder_pos] + data[placeholder_pos+len(self.placeholder_word):]
            data=self.trim_placeholders(data)
        return data

    def get_frames(self,data):
        frames = []
        frame_index=data.find(self.frameword)
        while (frame_index+self.framelength < len(data)):
            checkframe = data[frame_index:frame_index+len(self.frameword)]
            if (checkframe == self.frameword):
                next_frame = data[frame_index:frame_index+self.framelength]
                frames.append(next_frame)
                frame_index=frame_index+self.framelength
            else:
                print "ERROR: badframe!"
                exit()
        return frames

    def hex2bin(self,hexstring):
        binout = ""
        for char in hexstring:
            binout = binout + format(int(char,16),'b').zfill(4)
        return binout

    def process_frame(self,frame):
        frame_data = {}
        binframe=self.hex2bin(frame)
        for datatype in self.framedict:
            bindata = binframe[self.framedict[datatype][0]:self.framedict[datatype][1]]
            frame_data[datatype] = int(bindata,2)
        return frame_data

    def process_rxdata(self,signal_name):
        inverted_data = self.invert_words(signal_name)
        trimmed_data = self.trim_placeholders(inverted_data)
        frames = self.get_frames(trimmed_data)
        processed_data = []
        for frame in frames:
            processed_data.append(self.process_frame(frame))
        return processed_data
        
    def get_rxdata(self):
        self.rx_data={}
        for signal in self.rxdata_signals:
            self.rx_data[signal] = self.process_rxdata(signal)

    def test_capids(self,signal):
        self.logfile.write("---------------------------------------------------\n")
        self.logfile.write(signal + " capID rotation")
        self.logfile.write("\n")
        self.logfile.write("---------------------------------------------------\n")
        passall = True
        x = []
        y = []
        prev_vals = [-1]*4
        for frame_num,frame in enumerate(self.rx_data[signal]):
            modframe=frame_num%4
            capnum=frame["CapID"]
            x.append(modframe)
            y.append(capnum)
            if not prev_vals[modframe] < 0:
                if not capnum == prev_vals[modframe]:
                    passall = False
            prev_vals[modframe]=capnum
        if passall:
            self.logfile.write(signal + " capIDrotation: TESTS PASSED\n")
            #print signal +  " capIDrotation: TESTS PASSED"
        else:
            self.logfile.write("TEST FAILED: " + signal + " capIDrotation\n")
            self.logfile.write("     capseq: " + str(y) + "\n")
            print "TEST FAILED: " + signal + " capIDrotation"
            print "     capseq: " + str(y)
        plt.plot(x, y, 'o', color='black')
        plt.xlim(-0.5, 3.5)
        plt.ylim(-0.5, 3.5)
        plt.title(signal + " CapID rotation")
        plt.xlabel("frame # %4")
        plt.ylabel("CapID")
        plt.savefig(self.analysis_dir+'/'+self.datafile_name+'/'+signal+'/'+self.datafile_name+'_'+signal+'_capIDrotation.png')
        plt.clf()

    def analyze_datatype(self,signal,datatype):
        self.logfile.write("---------------------------------------------------\n")
        self.logfile.write(signal + " " +  datatype)
        self.logfile.write("\n")
        self.logfile.write("---------------------------------------------------\n")
        bin_min = self.bin_limits[datatype][0]-0.5
        bin_max = self.bin_limits[datatype][1]+0.5
        nbins = self.bin_limits[datatype][2]
        stepsize = (bin_max - bin_min)/nbins
        bins = []
        for i in range(0,nbins+1):
            bins.append(bin_min+i*stepsize)
        x = []
        for frame in self.rx_data[signal]:
            x.append(frame[datatype])        
        av=mean(x)
        stdev=std(x)
        mn=min(x)
        mx=max(x)
        self.logfile.write(signal + " " +  datatype + " mean  = " + str(av) + "\n")
        self.logfile.write(signal + " " +  datatype + " stdev = " + str(stdev) + "\n")
        self.logfile.write(signal + " " +  datatype + " min   = " + str(mn) + "\n")
        self.logfile.write(signal + " " +  datatype + " max   = " + str(mx) + "\n")
        passall = True
        if ((av < self.mean_limits[datatype][0]) or (av > self.mean_limits[datatype][1])):
            passall = False
            self.logfile.write("TEST FAILED: " + signal + " " +  datatype + " mean  = " + str(av) + "\n")
            print "TEST FAILED: " + signal + " " +  datatype + " mean  = " + str(av)
        if ((stdev < self.std_limits[datatype][0]) or (stdev > self.std_limits[datatype][1])):
            passall = False
            self.logfile.write("TEST FAILED: " + signal + " " +  datatype + " stdev  = " + str(stdev) + "\n")
            print "TEST FAILED: " + signal + " " +  datatype + " stdev  = " + str(stdev)
        if passall:
            self.logfile.write(signal + " " +  datatype + ": TESTS PASSED\n")
            #print signal + " " +  datatype + ": TESTS PASSED"
        plt.hist(x, bins,histtype=u'step')
        plt.title(signal + " " + datatype + " histogram")
        plt.xlabel(datatype)
        plt.ylabel("count")
        annotation_string =  'dataset: ' + self.datafile_name + '\n'
        annotation_string += 'signal: ' + signal + '\n'
        annotation_string += 'datatype: ' + datatype + '\n'
        annotation_string += 'mean = ' + "{:.2f}".format(av) + '\n'
        annotation_string += 'stdev = ' + "{:.2f}".format(stdev) + '\n'
        annotation_string += 'min = ' + "{:.2f}".format(mn) + '\n'
        annotation_string += 'max = ' + "{:.2f}".format(mx)
        plt.annotate(annotation_string, xy=(0.4, 0.7), xycoords='axes fraction')
        plt.savefig(self.analysis_dir+'/'+self.datafile_name+'/'+signal+'/'+self.datafile_name+'_'+signal+'_'+datatype+'.png')
        #plt.show()

    def analyze_signal(self,signal):
        if not os.path.isdir(self.analysis_dir+'/'+self.datafile_name+'/'+signal):
            os.mkdir(self.analysis_dir+'/'+self.datafile_name+'/'+signal)
        self.logfile.write("===================================================\n")
        self.logfile.write(signal)
        self.logfile.write("\n")
        self.logfile.write("===================================================\n")
        self.test_capids(signal)
        for datatype in self.framedict:
            self.analyze_datatype(signal,datatype)
            plt.clf()

    def full_analyze(self):
        if not os.path.isdir(self.analysis_dir):
            os.mkdir(self.analysis_dir)
        if not os.path.isdir(self.analysis_dir+'/'+self.datafile_name):
            os.mkdir(self.analysis_dir+'/'+self.datafile_name)
        self.logfile_name=self.analysis_dir+'/'+self.datafile_name+'/'+self.datafile_name+'.log'
        self.logfile=open(self.logfile_name,'w')
        for signal in self.rxdata_signals:
            self.analyze_signal(signal)
        self.logfile.close()

x=IlaData("iladata.csv")
x.full_analyze()

# check mean + stdev for each hist
# add expect mean expect stdev dicts for each
# accept also BC0 comma
# add merge data function
