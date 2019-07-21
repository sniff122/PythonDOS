import os
import argparse
import sys
import distro

command_dir = os.getcwd() + "\MS-DOS"

def main():
    distroname = distro.name()
    distroversion = distro.version()
    print(distroname + " [Version {}]\n(c) 2019 " + distroname + ". All right reserved.\n".format(distroversion))
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