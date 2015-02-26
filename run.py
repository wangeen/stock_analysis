#!/usr/bin/env python
import subprocess
import argparse

from read_csv import read_csv


def script(cmd):
    print cmd
    subprocess.call(cmd, shell=True)


if __name__  == "__main__":
    read_csv("sample/600561.csv")

    parser = argparse.ArgumentParser()
    parser.add_argument("-m",  "--message",  help="this is sample python script", action='store_true')
    args = parser.parse_args()
    if args.message:
        print "start script"
        ## TODO,  to be added here
        print "end script"
    else:
        parser.print_help()
