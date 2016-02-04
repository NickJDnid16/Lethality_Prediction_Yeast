'''
Created on 23 Oct 2015

@author: nid16
'''

import codecs
from itertools import repeat
import csv
import sys
inputfile = open('./phenotype_data.tab', mode='r')
outputfile = open('./Lethal&Viable_Genes.txt', mode='w')

for line in inputfile:
    if "inviable" in line or "viable" in line:
        outputfile.write(line)

inputfile.close()
outputfile.close()


inputfile = open('./Lethal&Viable_Genes.txt', mode='r')
outputfile = open('./Genes&Lethality_Rows.txt', mode='w')

inputfile = csv.reader(inputfile, delimiter='\t')
outputfile = csv.writer(outputfile)

for row in inputfile:

    count = int (1)
    del row[1]

    if count > 0:
        #outputfile.writerows(row[0])
        outputfile.writerows(repeat(row[0:1] + row[8:9], count))




data = {}


#inputfile = open('./Gene_With_Lethal&Viable_Only.txt', mode='r')
inputfile = open('./Genes&Lethality_Rows.txt', mode='r')
outputfile = open('./Genes_With_All_Lethality.txt', mode='w')

for line in inputfile:
    split_string = line.split(",")
    genome = split_string [0]
    lethalNotation = split_string [1]
    data [genome] = data.get(genome,"")+lethalNotation.rstrip('\r\n')+","


for x in data:
        #print (x+","+data[x]+"\n")
    outputfile.write(x+","+data[x]+"\n")

outputfile.close()



########################################

#sys.exit("STOPPED")



outputfile = open('./Single_Lethality_Genes.txt', mode='w')
inputfile = open('./Genes_With_All_Lethality.txt', mode='r')

for line in inputfile:
    v = ",viable" in line
    l = ",inviable" in line

    if (l and v):
        print ("Ignoring Line")
    elif "decreased" in line or "arrested" in line:
        print ("Ignoring Line")
    else:
        line = line.rstrip()
        bits = line.split(',')
        if(v):
            bit = bits[0]+",viable\n"
            print (bit)
            outputfile.write(bit)
        if(l):
            bit = bits[0]+",inviable\n"
            print (bit)
            outputfile.write(bit)
        if ((not l) and (not v)):
            print("Not Viable OR Lethal")


outputfile.close()


############################################################################################


