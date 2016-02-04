__author__ = 'nid16'

import codecs
import csv
import sys
data = {}
import pprint
outputfile = open('./Gene&GO_F.txt', mode='w')
GOoutputfile = open('./Gene_With_Only_GO.txt', mode='w')
FUNCoutputfile = open('./Gene_With_GO_FUNC .txt', mode='w')
Seen =[]
FUNC = []
geneAssociation = open('./gene_association.sgd')
geneAssociation = csv.reader(geneAssociation, delimiter='\t')

for rows in geneAssociation:

    if(rows[0] == "SGD"):#FlyBase = FB
        head, sep, tail = rows[10].partition('|')
        genome = head
        print genome
        GO = rows[4]
        dataMarker = rows[6]
        data[genome] = data.get(genome,"")+GO+","+dataMarker+","
        if genome not in Seen:
            Seen.append(genome)
            GOoutputfile.write(genome + "\n")
        FUNC.append(genome + "\t" + GO  + "\n")
for line in open('./Single_Lethality_Genes.txt', mode='r'):
    line = line.rstrip()
    split_line = line.split(",")
    gene = split_line[0]
    data[gene] = data.get(gene,"")+str(split_line[1])


################################################################

newFUNC = []

geneSeen = []
for line in open('./Single_Lethality_Genes.txt', mode='r'):
    line = line.rstrip()
    split_line = line.split(",")
    gene = split_line[0]
    lethality = split_line[1]
    #print "Lethality is " + lethality
    if "inviable" in lethality:
        for line in FUNC:
            tempFUNC = []
            if gene in line and line not in geneSeen:
                geneSeen.append(line)
                line = line.strip()
                tempFUNC.append(str(line) + "\t1")
                #print tempFUNC
                newFUNC.append(tempFUNC)
    if "viable" in lethality:
        for line in FUNC:
            tempFUNC = []
            if gene in line and line not in geneSeen:
                geneSeen.append(line)
                line = line.replace('\n','')
                tempFUNC.append(str(line) + "\t0")

                #print tempFUNC
                newFUNC.append(tempFUNC)

        #print "Something"
        #print tempFUNC
#FUNCoutputfile.write("\n".join(newFUNC))


for element in newFUNC:
    #FUNCoutputfile.writelines(str(element)+"\n")
    FUNCoutputfile.write(" ".join(element) + "\n")


###############################################################



########################################################

for x in data:
    print (x,data[x])
    outputfile.write(x+","+data[x]+"\n")
  #  FUNCoutputfile.write()
outputfile.close()


########################################################


inputfile = open('./Gene&GO_F.txt', mode='r')
outputfile = open('./Gene&GO_F_With_Lethality.txt', mode='w')

inputfile = csv.reader(inputfile, delimiter=',')

previous = None


writer = csv.writer(outputfile)



for rows in inputfile:

        if "viable" in str(rows[-1]) or "inviable" in str(rows[-1]):

            if "GO" in str(rows):
                writer.writerow(rows)
                print rows