import os
import argparse
import sys
import distro

def main():
    try:
        distroname = distro.name()
        distroversion = distro.version()
        if distroversion == "":
            distroversion = "1.2"
        print("{} [Version {}]\n(c) 2019 {}. All right reserved.\n".format(distroname, distroversion, distroname))
        a = input(os.getcwd() + ">")
        parser(a)
    except:
        sys.exit(1)
    

def parser(string):
    try:
        string = str(string).split(" ")
        if string[0] == 'echo':
            arg = str(''.join(string))
            print(str(arg[len(string[0]):]))
    except:
        pass
    
main()