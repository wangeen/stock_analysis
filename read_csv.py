# -*- coding: utf-8 -*-
import csv, sys
from stock_class import stock_day_info, stock_day_info_list

def day_string_to_int(day):
    pass

def read_csv(fname):
    del stock_day_info_list[:]
    with open(fname,  'rb') as csvfile:
        spamreader = csv.reader(csvfile,  delimiter=',',  quotechar='|')
        for row in spamreader:
            if len(row)!=15:
                sys.exit("{0} : cvs format error,  each row should has 15 items".format(fname))
            #0: 日期,
            #1: 股票代码,
            #2: 名称,
            #3: 收盘价,
            #4: 最高价,
            #5: 最低价,
            #6: 开盘价,
            #7: 前收盘,
            #8: 涨跌额,
            #9: 涨跌幅,
            #10: 换手率,
            #11: 成交量,
            #12: 成交金额,
            #13: 总市值,
            #14: 流通市值
            str_day = row[0]
            str_close = row[3]
            str_high = row[4]
            str_low = row[5]
            str_open = row[6]
            str_turnover = row[10]
            str_volumn = row[11]
            str_total = row[12]
            #print ',  '.join(row)
            one_day_info = stock_day_info(day=str_day, open=str_open, high=str_high, low=str_low, close=str_close, volumn=str_volumn, total=str_total, turnover=str_turnover)
            one_day_info.print_day_info()
            stock_day_info_list.append(one_day_info)
            #print row
    pass
