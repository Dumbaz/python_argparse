#!/usr/bin/env python

from argparse import ArgumentParser
import sys

parser = ArgumentParser()

parser.add_argument("-a" , help="directly input IPs seperated by spaces")
parser.add_argument("-f", help="input a file with IPs, one IP per line")

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
print(args.echo)
