#!/usr/bin/python3
import json
import os
import argparse
import sys
import distro
import json

with open("help-ms-dos.json", "r") as f:
    commands_help = json.load(f)

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
            a = parser(a)
            if a:
                break
                print('\n')
                sys.exit(1)
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
            return False
        elif string[0] == 'cls':
            os.system('clear')
            return False
        elif string[0] == 'help':
            print("cls help echo exit")
            return False
        elif string[0] == 'exit':
            return True
        else:
            print("'{}' is not recognized as an internal or externel command,\noperable program or batch file\n".format(str(string[0])))
            return False
    except:
        pass
        return False

def help(command):
    try:
        read = 
    except:
        pass
main()