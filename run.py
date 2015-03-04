#!/usr/bin/env python
import subprocess
import argparse

from read_csv import read_csv
from theory import *


def script(cmd):
    print cmd
    subprocess.call(cmd, shell=True)


if __name__  == "__main__":
    read_csv("sample/600561.csv")
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

