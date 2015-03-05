# -*- coding: utf-8 -*-

class day_pair:
    def __init__(self, today, yesterday):
        self.today = today
        self.yesterday = yesterday
        pass
    def print_up_too_fast(self):
        print "[up fast]:[{0},{1}]:price {2} {3:.2f}%".format(self.today.day,
                                                self.yesterday.day,
                                                self.today.close,
                                                (-self.today.close+self.yesterday.close)/self.yesterday.close*100
                                                )
        pass
    pass

# up fast property of day
class property_up:
    def __init__(self, day):
        self.day = day
        pass
    def log(self,day):
        print "[up]:[{0},{1}]:price {2} {3:.2f}%".format(day.day,
                                                self.day.day,
                                                day.close,
                                                (-day.close+self.day.close)/self.day.close*100)
        pass
    pass

# down fast property of day
class property_dw:
    def __init__(self, day):
        self.day = day
        pass
    def log(self,day):
        print "[dw]:[{0},{1}]:price {2} {3:.2f}%".format(day.day,
                                                self.day.day,
                                                day.close,
                                                (-day.close+self.day.close)/self.day.close*100)
        pass
    pass

# the stock price and volumn information of one day
class stock_day:
    def __init__(self, day, open, high, low, close, volumn,total,  turnover):
        self.day = day

        self.open = open
        self.high = high
        self.low = low
        self.close = close

        self.average = total/volumn # average price should be more reasonable

        self.volumn = volumn
        self.total = total
        self.turnover = turnover
        pass

    def log(self):
        print '''  日期:''', self.day
        print '''开盘价:{0:.2f}'''.format( self.open)
        print '''最高价:{0:.2f}'''.format( self.high)
        print '''最低价:{0:.2f}'''.format( self.low)
        print '''收盘价:{0:.2f}'''.format( self.close)
        print '''  幅度:{0:.2f}'''.format((self.close-self.open)/self.open*100)
        print '''  均价:{0:.2f}'''.format( self.average)

        print '''   换手率(%):{0:.2f}'''.format( self.turnover)
        print '''  成交量(手):{0:.2f}'''.format( self.volumn)
        print '''成交金额(万):{0:.2f}'''.format( self.total/10000)
        print '''资金流入(万):{0:.2f}'''.format( (self.total-self.volumn*self.open)/10000)

        print
        pass
    pass

stock_day_list = []

def print_up_fast():
    up_count = 0
    for item in stock_day_list:
        try:
            item.up_fast.log(item)
            up_count+=1
        except:
            pass
        pass
    print "up fast count:",up_count," out of ",len(stock_day_list)
    pass

def print_dw_fast():
    dw_count = 0
    for item in stock_day_list:
        try:
            item.dw_fast.log(item)
            dw_count+=1
        except:
            pass
    print "dw fast count:",dw_count," out of ",len(stock_day_list)
    pass

def print_latest_days(count):
    for i in range(0,count):
        stock_day_list[i].log()

