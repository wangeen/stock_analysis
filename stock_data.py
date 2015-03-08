# -*- coding: utf-8 -*-


class s_date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "{0}/{1}/{2}".format(self.year,self.month,self.day)

    def __ge__(self,other):
        if self.year<other.year:
            return False
        if self.year>other.year:
            return True
        if self.month<other.month:
            return False
        if self.month>other.month:
            return True
        if self.day<other.day:
            return False
        if self.day>other.day:
            return True
        return True

    def __le__(self,other):
        if self.year<other.year:
            return True
        if self.year>other.year:
            return False
        if self.month<other.month:
            return True
        if self.month>other.month:
            return False
        if self.day<other.day:
            return True
        if self.day>other.day:
            return False
        return True
    pass

# up fast property of day
class s_property_up:
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
class s_property_dw:
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
class s_stock_day:
    def __init__(self, day, open, high, low, close, volumn,total,  turnover):
        items = day.split('-')
        self.day = s_date(year=int(items[0]),month=int(items[1]),day=int(items[2]))

        self.open = open
        self.high = high
        self.low = low
        self.close = close

        self.average = total/volumn # average price should be more reasonable

        self.volumn = volumn
        self.total = total
        self.turnover = turnover
        pass

    def is_up(self):
        if self.close>self.open:
            return True
        return False

    def __str__(self):
        str  = '''        日期: {0}\n'''.format( self.day)
        str += '''      开盘价: {0:.2f}\n'''.format( self.open)
        str += '''      最高价: {0:.2f}\n'''.format( self.high)
        str += '''      最低价: {0:.2f}\n'''.format( self.low)
        str += '''      收盘价: {0:.2f}\n'''.format( self.close)
        str += '''        幅度: {0:.2f}\n'''.format((self.close-self.open)/self.open*100)
        str += '''        均价: {0:.2f}\n'''.format( self.average)
        str += '''   换手率(%): {0:.2f}\n'''.format( self.turnover)
        str += '''  成交量(手): {0:.2f}\n'''.format( self.volumn)
        str += '''成交金额(万): {0:.2f}\n'''.format( self.total/10000)
        str += '''资金流入(万): {0:.2f}\n'''.format( (self.total-self.volumn*self.open)/10000)
        return str
    pass

    def __repr__(self):
        return self.__str__()

stock_day_list = []

def get_sub_day_list(s_date_begin,s_date_end):
    sub_day_list = []
    for item in stock_day_list:
        if item.day>=s_date_begin and item.day<=s_date_end :
            sub_day_list.append(item)
        pass
    return sub_day_list

def print_up_fast():
    up_count = 0
    next_up = 0
    for i in range(0,len(stock_day_list)):
        try:
            item = stock_day_list[i]
            item.up_fast.log(item)
            up_count+=1
            if stock_day_list[i-1].is_up() is True:
                next_up+=1
        except:
            pass
        pass
    print "up fast count:",up_count," out of ",len(stock_day_list)
    print "next up day count:",next_up
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
        print stock_day_list[i]

