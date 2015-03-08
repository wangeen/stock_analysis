import matplotlib.pyplot as plt
from stock_data import *

def plot_main():
    average_list =[]
    for day in stock_day_list:
        average_list.append(day.average)
        pass
    plt.plot(average_list)
    plt.ylabel('Price')
    plt.show()
