#!/usr/bin/python
import sys, getopt

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hn:m:",["nValue=","mValue="])
   except getopt.GetoptError:
      print 'add.py -n <nValue> -m <mValue>'
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print 'add.py -n <nValue> -m <mValue>'
         sys.exit()
      elif opt in ("-n", "--nValue"):
         nValue1 = int(arg)
      elif opt in ("-m", "--mValue"):
         mValue1 = int(arg)
		 
   mn=nValue1+mValue1
   print  mn
if __name__ == "__main__":
   main(sys.argv[1:])