#!/usr/bin/python

import sys, getopt

def main(argv):
   firstname = ''
   lastname = ''
   try:
      opts, args = getopt.getopt(argv,"hf:l:",["first=","last="])
   except getopt.GetoptError:
      print 'test2.py -f <first name> -l <last name>'
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print 'Welcome'
         sys.exit()
      elif opt in ("-f", "--first"):
         firstname = arg
      elif opt in ("-l", "--last"):
         lastname = arg

   print 'First Name is "', firstname
   print 'Last Name is "', lastname

if __name__ == "__main__":
   main(sys.argv[1:])