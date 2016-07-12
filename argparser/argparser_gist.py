#!/usr/bin/python

import argparse

__author__ = 'Dorian Lenzner'

def get_args():
    parser = argparse.ArgumentParser(description='Retrieves arguments')

    parser.add_argument('-a', '--adress', type=str, help='Ip Adresses seperated by space', required=False, nargs='*')
    parser.add_argument('-f', '--file', type=str, help='File with IPs, line by line', required=False)

    args = parser.parse_args()

    adress = args.adress[0].split(",")
    file = args.file

    return adress, file


adress, file = get_args()

print(adress)
print(file)
