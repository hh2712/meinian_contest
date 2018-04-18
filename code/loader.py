#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import OrderedDict
import pandas as pd
import numpy as np

class loader():
    def load_csv(self, filename):
        df = pd.read_csv(filename)
        fields =  df.columns.tolist()
        fields = [field.decode('gbk').encode('utf8') for field in fields]
        df.columns = fields
        return df
        
    
    def load_txt(self, txts, num_lines = 200):
        lines = []
        cnt = 0
        for txt in txts:
            with open(txt, 'r') as f:
                for line in f:
                    lines.append(line)
                    if cnt == num_lines:
                        break
                    cnt += 1
                    
        lines = [line.strip().split('$') for line in lines]
        return lines
    
    
    def sort_data(self, df, lines):
        self.data = {}
        row_idx = df.index['vid'== lines[0][0]]
        current_vid = None
        instance = None
        print 'num of lines', len(lines)
        for line in lines:
            if line[0] != 'vid':
                if line[0] not in self.data.keys():
                    # fill fields in the csv
                    row_idx = df.index['vid' == current_vid]
                    keys = df.columns.tolist()[1:]
                    values = df[row_idx:row_idx+1].values[0][1:]
                    instance = {}
                    for k, v in zip(keys, values):
                        instance[k] = v
                    
                    # fill the currernt line
                    instance[line[1]] = line[2]
                else:
                    instance = self.data[line[0]]
                    instance[line[1]] = line[2]
                self.data[line[0]] = instance
                
        for k, v in self.data.iteritems():
            print len(v)
    
    #def output_csv(self):
        

        