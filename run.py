#!/usr/bin/env python
import subprocess,os
import argparse
import config

from read_csv import read_csv
from theory import *
from plot import *


def script(cmd):
    print cmd
    subprocess.call(cmd, shell=True)

if __name__  == "__main__":
    read_csv("sample/601318.csv")

    sub_day_list = get_sub_day_list(s_date(year=2014,month=12,day=1),s_date(year=2015,month=4,day=1))
    print sub_day_list
    #plot_main(sub_day_list)
    plot_candlestick(sub_day_list)

    if os.path.exists(config.output_path):
        script("rm -rf {0}".format(config.output_path))
    os.makedirs(config.output_path)
    print "Please refer '{0}' for result.".format(config.output_path)
    #theory_up_down_days_count()
    #theory_pre_next_count()

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--Tup", help="theory: price up fast with setting percent")
    parser.add_argument("-d", "--Tdown", help="theory: price down fast with setting percent")
    parser.add_argument("-a", "--day", help="print the recent given N days detail")
    #parser.add_argument("-d", "--Tdown", help="theory: price down fast", action='store_true')
    args = parser.parse_args()
    if args.Tup:
        try:
            theory_price_change_fast(float(args.Tup))
            print_up_fast()
        except:
            print parser.print_help()
    if args.Tdown:
        try:
            theory_price_change_fast(float(args.Tdown))
            print_dw_fast()
        except:
            print parser.print_help()
    if args.day:
        try:
            print_latest_days(int(args.day))
        except:
            print parser.print_help()
        pass
    pass

