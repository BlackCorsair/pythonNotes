#!/usr/bin/python
import getpass
from subprocess import call as cmd
"""
    Author: Jorge Hevia - jhevia@gfi.es
    What does this script?: this script checks the table space
    from a mysql database
"""
"""
    Name: colors
    Function: it colorize the sad black and white console"
"""


class colors:
    WARNING = "\033[93m"
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = "\033[91m"
    ENDC = "\033[0m"


# MAIN
sql = """SELECT SUM(round(((data_length + index_length) / 1024 / 1024), 2))\
 `Size in MB of the entire mysql server`
FROM information_schema.TABLES;
"""
c = colors()
print(c.OKGREEN + "Welcome to Tablespace size 101 traveler!!!")
print("Please enter the root password" + c.ENDC)
pwd = getpass.getpass()
print("\n")
log = cmd(["mysql", "-uroot", "-p" + str(pwd), "-e", sql])
print(c.OKGREEN + "\nBye!" + c.ENDC)
