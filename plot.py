import matplotlib.pyplot as plt
from stock_data import *
#/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/matplotlib/finance.py
from matplotlib.finance import candlestick2

def plot_main(day_list):
    average_list =[]
    for day in reversed(day_list):
        average_list.append(day.average)
        pass
    plt.plot(average_list)
    plt.ylabel('Price')
    plt.show()

def plot_candlestick(day_list):
    opens = []
    highs = []
    lows = []
    closes = []
    average_list =[]
    for day in reversed(day_list):
        opens.append(day.open)
        highs.append(day.high)
        lows.append(day.low)
        closes.append(day.close)
        average_list.append(day.average)
        pass
    fig, ax = plt.subplots()
    plt.plot(average_list)
    candlestick2(ax,opens,closes,highs,lows,0.6)
    plt.show()
    pass
