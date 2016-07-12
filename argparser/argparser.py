#!/usr/bin/env python

from argparse import ArgumentParser
import sys


def interpret_a(address):
    print(address)

def interpret_file(file):
    with open(file) as file:
        for line in file:
            line = line.strip()
            if line:
                yield(line)

parser = ArgumentParser()

parser.add_argument("-a" , help="directly input IPs seperated by spaces")
parser.add_argument("-f", help="input a file with IPs, one IP per line")

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
print(args.echo)
