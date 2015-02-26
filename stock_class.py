# -*- coding: utf-8 -*-

class stock_day_info:
    def __init__(self, day, open, high, low, close, volumn,total,  turnover):
        self.day = day

        self.open = open
        self.high = high
        self.low = low
        self.close = close

        self.volumn = volumn
        self.total = total
        self.turnover = turnover
        pass

    def print_day_info(self):
        print '''日期:''', self.day
        print '''开盘价:''', self.open
        print '''最高价:''', self.high
        print '''最低价:''', self.low
        print '''收盘价:''', self.close

        print '''换手率(%):''', self.turnover
        print '''成交量(手):''', self.volumn
        print '''成交金额:''', self.total
        pass

stock_day_info_list = []
