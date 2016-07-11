#!/usr/bin/env python

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("echo", help="echo the string")


args = parser.parse_args()
print(args.echo)
