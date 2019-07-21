import os
import argparse
import sys
import distro

def main():
    distroname = distro.name()
    distroversion = distro.version()
    print(distroname + " [Version {}]\n(c) 2019 ".format(distroversion) + distroname + ". All right reserved.\n")
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