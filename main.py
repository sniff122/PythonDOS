import os
import argparse
import sys

command_dir = os.getcwd() + "\MS-DOS"

def main():
    a = input(os.getcwd() + ">")
    parser(a)
    

def parser(string):
    try:
        string = str(string).split(" ")
        if string[0] == 'echo':
            arg = str(''.join(string))
            print(str(arg[len(string[0]):]))
    except:
        pass
    
main()