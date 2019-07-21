#!/usr/bin/python3
import os
import argparse
import sys
import distro

def main():
    os.system('clear')
    distroname = distro.name()
    distroversion = distro.version()
    if distroversion == "":
        distroversion = "1.2"
    print("{} [Version {}]\n(c) 2019 {}. All right reserved.\n".format(distroname, distroversion, distroname))
    while 1:
        try:
            a = input(os.getcwd() + ">")
            parser(a)
        except:
            break
            print('\n')
            sys.exit(1)
    

def parser(string):
    try:
        string = str(string).split(" ")
        if string[0] == 'echo':
            arg = str(' '.join(string))
            print(str(arg[len(string[0]) + 1:]))
        else:
            print("'{}' is not recognized as an internal or externel command,\noperable program or batch file\n".format(str(string[0])))
    except:
        pass
    
main()