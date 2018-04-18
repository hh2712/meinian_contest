#!/usr/bin/env python
# -*- coding: utf-8 -*-
import loader as l 

if __name__ == "__main__":
    # data files
    train_csv = '../data/train.csv'
    test_csv = '../data/test.csv'
    txt1 = '../data/rawdata1.txt'
    txt2 = '../data/rawdata2.txt'
    text_files = [txt1, txt2]
    
    # import csv data
    td = l.loader()
    train_df = td.load_csv(train_csv)
    lines = td.load_txt(text_files)
    full_train_df = td.sort_data(train_df, lines)
    