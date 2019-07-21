import os
import argparse
import sys

command_dir = os.getcwd() + "\MS-DOS"

def main():
    

def parser(string):
    try:
        string = str(string).split(" ")
        if string[0] == 'cd':
            string = str(''.join(string))
            print(str(string[1:]))
    except:
        pass
    