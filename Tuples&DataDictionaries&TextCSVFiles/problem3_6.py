# -problem3_6.py *- coding: utf-8 -*-

import sys

infile = sys.argv[1]
outfile = sys.argv[2]

fread = open(infile)
fwrite = open(outfile,'w')

for line in fread:
    line = line.strip("\n")
    fwrite.write(str(len(line)) + "\n")
   
fread.close()
fwrite.close()