import os
import argparse
import sys

def main():
    distro = "Furry Linux"
    print(distro + " [Version 1.0]\n(c) 2019 " + distro + ". All right reserved.\n")
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