# -*- coding: utf-8 -*-
import csv, sys
from stock_class import stock_day_info, stock_day_info_list

def theory_test():
    previous_close = stock_day_info_list[0].close
    up_days = 0
    down_days = 0
    equal_days = 0
    for item in stock_day_info_list[1:]:
        close = item.close
        diff = previous_close-close
        if diff<0:
            up_days += 1
        elif diff>0:
            down_days += 1
        else:
            equal_days += 1
            pass
        previous_close = close
        pass
    print "up days", up_days
    print "down days", down_days
    print "equal days", equal_days
    pass

def theory_period():
    #TODO period is decided by wave,  by now we assum it should be 5
    return 5

def theory_maker_stuck():
    ''' 判定大量投资被套 '''
    pass

def theory_price_down_too_fast(percent):
    '''价格下降过快'''
    pass

def theory_price_up_too_fast(percent):
    '''价格上升过快'''
    pass

def theory_stock_keep_time():
    '''每股平均保留时间'''

    pass

def theory_small_():
    '''小区间震动，大成交量'''
    pass

