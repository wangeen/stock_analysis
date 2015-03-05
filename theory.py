# -*- coding: utf-8 -*-
import csv, sys
from stock_data import *

# my database for all data
# 资金回流
# 价格的大波动和资金流向的关系
# 少量的投入就会引起价格的大波动
# 利用T＋1分析问题

def theory_up_down_days_count():
    print '''检测上涨下降天数'''
    previous_close = stock_day_list[0].average
    up_days = 0.0
    down_days = 0.0
    equal_days = 0.0
    for item in stock_day_list[1:]:
        close = item.average
        diff = close-previous_close
        if diff>0:
            up_days += 1
        elif diff<0:
            down_days += 1
        else:
            equal_days += 1
        previous_close = close
        pass
    total_days = up_days+down_days+equal_days
    print "   up days {0}, percent {1:.2f}%".format(up_days,up_days/total_days*100)
    print " down days {0}, percent {1:.2f}%".format(down_days,down_days/total_days*100)
    print "equal days {0}, percent {1:.2f}%".format(equal_days,equal_days/total_days*100)
    pass

def theory_pre_next_count(previous_up=True):
    '''pre up, next count'''
    previous_previous_close = stock_day_list[0].average
    previous_close = stock_day_list[1].average
    up_days = 0.0
    down_days = 0.0
    equal_days = 0.0
    for item in stock_day_list[2:]:
        close = item.average
        diff_previous = previous_close-previous_previous_close
        if previous_up==True and diff_previous>0:
            diff = close-previous_close
            if diff>0:
                up_days += 1
            elif diff<0:
                down_days += 1
            else:
                equal_days += 1
        previous_previous_close = previous_close
        previous_close = close
        pass
    total_days = up_days+down_days+equal_days
    if previous_up:
        print "previous up"
    else:
        print "previous down"
    print "up days", up_days," percent ",up_days/total_days*100
    print "down days", down_days," percent ",down_days/total_days*100
    print "equal days", equal_days," percent ",equal_days/total_days*100
    pass

def theory_period():
    #TODO period is decided by wave,  by now we assum it should be 5
    return 5

def theory_maker_stuck():
    ''' 判定大量投资被套 '''
    pass


def theory_price_change_fast(percent=8):
    print '''检测价格波动过快'''
    percent /= 100.0
    period = theory_period()
    total_days = len(stock_day_list)
    if total_days<period:
        print "the total days is less than period"
        return
    i = 0
    last_day = stock_day_list[i]
    last_price = last_day.average
    i+=1
    period_current = 0
    while i<(total_days-period):
        for j in range(0,period):
            current_price = stock_day_list[i+j].average
            if (current_price-last_price)/last_price>percent:
                last_day.up_fast = property_up(stock_day_list[i+j])
                break
            elif (current_price-last_price)/last_price<-percent:
                last_day.dw_fast = property_dw(stock_day_list[i+j])
                break
        last_day =  stock_day_list[i]
        last_price = last_day.average
        i+=1
        pass
    pass

def theory_stock_keep_time():
    '''每股平均保留时间'''

    pass

def theory_small_():
    '''小区间震动，大成交量'''
    pass

