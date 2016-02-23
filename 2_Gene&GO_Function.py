__author__ = 'nid16'

import codecs
import csv
import sys
data = {}
import pprint
outputfile = open('./Gene&GO_F.txt', mode='wb')
GOoutputfile = open('./Gene_With_Only_GO.txt', mode='wb')
FUNCoutputfile = open('./Gene_With_GO_FUNC.txt', mode='wb')
Seen =[]
FUNC = []
geneAssociation = open('./gene_association.sgd', mode= "rb")


for line in geneAssociation:
    split_string = line.split("\t")
    if(split_string[0] == "SGD"):#FlyBase = FB
        head, sep, tail = split_string[10].partition('|')
        genome = head
        print genome
        GO = split_string[4]
        dataMarker = split_string[6]
        data[genome] = data.get(genome,"")+GO+","+dataMarker+","
        if genome not in Seen:
            Seen.append(genome)
            GOoutputfile.write(genome + "\n")
        FUNC.append(genome + "\t" + GO  + "\n")
for line in open('./Single_Lethality_Genes.txt', mode='rb'):
    line = line.rstrip()
    split_line = line.split(",")
    gene = split_line[0]
    data[gene] = data.get(gene,"")+str(split_line[1])


################################################################

newFUNC = []

geneSeen = []
for line in open('./Single_Lethality_Genes.txt', mode='rb'):
    line = line.rstrip()
    split_line = line.split(",")
    gene = split_line[0]
    lethality = split_line[1]
    #print "Lethality is " + lethality
    if (lethality == "inviable"):
        for line in FUNC:
            tempFUNC = []
            if gene in line and line not in geneSeen:
                geneSeen.append(line)
                line = line.strip()
                tempFUNC.append(str(line) + "\t1")
                print tempFUNC
                newFUNC.append(tempFUNC)
    if (lethality == "viable"):
        for line in FUNC:
            tempFUNC = []
            if gene in line and line not in geneSeen:
                geneSeen.append(line)
                line = line.replace('\n','')
                tempFUNC.append(str(line) + "\t0")

                print tempFUNC
                newFUNC.append(tempFUNC)




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


inputfile = open('./Gene&GO_F.txt', mode='rb')
outputfile = open('./Gene&GO_F_With_Lethality.txt', mode='wb')
LethalOutput = open('./Lethal_Yeast.txt', mode='wb')
Viable_LethalOutput= open('./Lethal&Viable_Yeast.txt', mode='wb')
inputfile = csv.reader(inputfile, delimiter=',')

previous = None


writer = csv.writer(outputfile)
Lethalwriter = csv.writer(LethalOutput)
VLwriter = csv.writer(Viable_LethalOutput)


for rows in inputfile:

        if "viable" in str(rows[-1]) or "inviable" in str(rows[-1]):

            if "GO" in str(rows):
                writer.writerow(rows)
                VLwriter.writerow(rows[0:1])
                if "inviable" in str(rows[-1]):
                    Lethalwriter.writerow(rows[0:1])

                print rows