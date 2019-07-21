#!/usr/bin/python3
import os
import argparse
import sys
import distro
import json

def main():
    os.system('clear')
    distroname = distro.name()
    distroversion = distro.version()
    if distroversion == "":
        distroversion = "1.0"
    print("{} [Version {}]\n(c) 2019 {}. All right reserved.\n".format(distroname, distroversion, distroname))
    while 1:
        try:
            a = input(os.getcwd() + ">")
            a = parser(a)
            if a:
                print('\n')
                sys.exit(1)
                break
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
            if checkcommand(string, 1):
                help(string[1])
            else:
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

def checkcommand(string, num):
    try:
        string[int(num)]
        return True
    except:
        return False

def help(command):
    try:
        read = open('MS-DOS/help-ms-dos.json', 'r')
        data = json.load(read)
        data[command]
        print(data[command]['description'])
        print(data[command]['usage'])
    except:
        pass
main()