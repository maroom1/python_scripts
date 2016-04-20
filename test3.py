#!/usr/bin/python

import sys, getopt

def main(argv):
   value = ''
   #lastname = ''
   try:
      opts, args = getopt.getopt(argv,"hv:",["value="])
   except getopt.GetoptError:
      print 'test3.py -v value'
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print 'Display Usage \n test3.py -v value '
         sys.exit()
      elif opt in ("-v", "--value"):
         value = arg
		 
      # elif opt in ("-l", "--last"):
        #  lastname = arg 

   print 'Value is "', value
   #print 'Last Name is "', lastname

if __name__ == "__main__":
   main(sys.argv[1:])