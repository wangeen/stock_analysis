# -*- coding: utf-8 -*-
import csv, sys
from stock_class import stock_day, stock_day_list

def day_string_to_int(day):
    pass

def read_csv(fname):
    del stock_day_list[:]
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
            try:
                str_day = row[0].strip()
                str_close = float(row[3].strip())
                str_high = float(row[4].strip())
                str_low = float(row[5].strip())
                str_open = float(row[6].strip())
                str_turnover = float(row[10].strip())
                str_volumn = float(row[11].strip())
                str_total = float(row[12].strip())
                if str_close>0 and str_high>0 and str_low>0 and str_open>0:
                    one_day_info = stock_day(day=str_day, open=str_open, high=str_high, low=str_low, close=str_close, volumn=str_volumn, total=str_total, turnover=str_turnover)
                    #one_day_info.log()
                    stock_day_list.append(one_day_info)
            except:
                pass
    pass
