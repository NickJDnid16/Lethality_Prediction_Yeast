from datetime import datetime

startTime = datetime.now()

# Unicode Characters from text file
import codecs
import json
import sys
import time
import csv
counter = 1

from pygraph.classes.digraph import digraph

# Graph creation

gr = digraph()
count = 0

# Input
GraphInput = codecs.open('./Refined_GO_Nodes.txt', encoding='utf-8', mode='rb')

EdgesInput = codecs.open('./GO_Children&Parents.txt', encoding='utf-8', mode='rb')

with open('./GO_Children&Parents.txt') as json_file:
    json_data = json.load(json_file)
    # print(json_data, "\n")

    for key in json_data.keys():
        ##print ("key:", key, " parents:",json_data[key]['p'], " children:",json_data[key]['c'])#("key:",key,"\n")
        node = key.replace(":", "")
        gr.add_node(node)
        print ("Added ", node)

    for key in json_data.keys():
        print (count)
        ##print ("key:", key, " parents:",json_data[key]['p'], " children:",json_data[key]['c'])#("key:",key,"\n")
        node = key.replace(":", "")
        # gr.add_node(node)
        for parent in json_data[key]['p']:
            print("PARENT")
            pt = parent.replace(":", "")
            # print(node, " - ", pt)
            if gr.has_node(node) and gr.has_node(pt):
                if not gr.has_edge((pt, node)):
                    gr.add_edge((pt, node))
        for child in json_data[key]['c']:
            print("CHILD")
            cd = child.replace(":", "")
            if gr.has_node(node) and gr.has_node(cd):
                if not gr.has_edge((node, cd)):
                    gr.add_edge((node, cd))
        count += 1
# print(GraphInput)

counter = 0

count = 0

with open('./Refined_GO_Nodes.txt') as input:
    tempVec = []
    BinVec = []
    vec = []
    for line in input:
        tempVec.append(line.strip())
        BinVec.append(0)
    for item in tempVec:
        print("Item")
        print(item)
        tempItem = item.replace(":", "")
        vec.append(tempItem)
        print(tempItem)

Missing = []


def Incidents(Up):
    i = 0

    for key in Up:
        # print(i)
        # print(key)
        if key not in Seen:
            tempy = []
            try:
                tempy.extend(gr.incidents(key))
                Seen.append(key)
            except (KeyError, ValueError):
                OutMissing.write("Tempy Missing")
                # print(len(tempy))
            if len(tempy) > 0:
                i = i + 1
                if i > 0:
                    return False
                else:
                    return True


def Duplicates(Up):
    NewUp = []
    NodesSeen = []
    for node in Up:
        if node not in NodesSeen:  # not a duplicate
            NewUp.append(node)
            NodesSeen.append(node)
    return NewUp


debug = 0

data = open('./Gene&GO_F_With_Lethality.txt', mode="rb")


outputfile = open('./BinVec.txt', mode='wb')
OutMissing = open('./Missing.txt', mode='wb')
OutParents = open('./Parents.txt', mode='wb')

Testing = open('./Testings.txt', mode='wb')

Func = []
TempFunc  = []

for line in data:

    debug = debug + 1
    csv = line.split(",")
    Gene = csv[0]
    print(csv[0])


    Continue = True
    csvCount = 0
    Ancestors = []
    # Ancestors.append(temp)
    Seen = []
    Up = []
    for t in range(1, len(csv)):
        csvCount = csvCount +1
        if "GO" in csv[csvCount]:
            print(csv[csvCount])
            print "Here"

            temp = csv[csvCount]
            temp = temp.replace(":", "")
            Func.append(Gene+"\t"+temp+"\n")


            # print ("Ancestors")
            # print(gr.incidents(temp))

            Up.append(temp)



            # Ancestors.extend(Up)
            print("Up")
            Continue = True
            Nodes = []
            while Continue == True:
                l = 0
                if Incidents(Up) == False:
                    # print("GO in Incidents")

                    for node in Up:
                        if node not in Nodes:
                            Nodes.append(node)
                            try:
                                Up.extend(gr.incidents(node))
                                l = l + 1

                                if l == 1000000:
                                    Up = Duplicates(Up)
                                    # print("Parents Added")
                            except (KeyError, ValueError):
                                print("Error")

                                # print("Node Size")
                                # print(len(Nodes))


                else:
                    Continue = False
                    print("Root")

    Ancestors.extend(Up)
    print("Ancestors")
    # print(Ancestors)
    # print(vec)
    ModifiedAncestors = []
    NodesSeen = []
    for node in Ancestors:
        if node not in NodesSeen:  # not a duplicate
            ModifiedAncestors.append(node)
            NodesSeen.append(node)

    print ModifiedAncestors

    del Ancestors[:]
    for Node in ModifiedAncestors:


        # OutParents.write(Node)
        try:

            print(vec.index(Node))
            Testing.write(Node)
            BinVec[vec.index(Node)] = 1
        # Parents = gr.incidents(temp)

        except (KeyError, ValueError):
            print("Missing")
            try:
                Missing.index(Node)
                print("Already Missing")
            except (KeyError, ValueError):
                Missing.append(Node)

    outputfile.write(Gene)
    outputfile.write(',')

    for x in ModifiedAncestors:
        Func.append(Gene+"\t"+x+"\n")

    for key in BinVec:
        outputfile.write(str(key))

    outputfile.write('\n')
    Func.append('\n')

    print(Gene, BinVec)

    for t in range(0, len(BinVec)):
        BinVec[t] = 0
    print("Loop")
    try:
        del Seen[:]
        del Up[:]
        del Ancestors[:]
        del ModifiedAncestors[:]
        del Nodes[:]
    except NameError:
        print "NameError"

print("Missing")
print(len(Missing))
for key in Missing:
    OutMissing.write(str(Missing))
    OutMissing.write('\n')


###############################################
newFUNC = []
#Test

geneSeen = []

#outputfile.close()

tempy = open('./FUNCGenes.txt', mode='wb')
FuncMatch = open('./Gene&GO_F_With_Lethality.txt', mode='rb')
FUNCoutputfile = open('./Gene_With_GO_FUNC.txt', mode='wb')

tempySeen = []

Counter = 0





for line in FuncMatch:
    split_string = line.split(",")

    gene = split_string[0]

    lethality = split_string[-1]
    lethality = lethality.replace("\r\n","")


    if (lethality == "lethal"):
        for line in Func:
            if line == "\n":
                continue

            tempFUNC = []
            if gene in line and line not in geneSeen:
                geneSeen.append(line)
                line = line.strip()
                line = line.replace("GO","GO:")
                tempFUNC.append(str(line) + "\t1")
                #print tempFUNC
                newFUNC.append(tempFUNC)
            if gene in line and gene not in tempySeen:
                tempySeen.append(gene)
                tempy.write(gene+",lethal\n")
                Counter = Counter +1
                print Counter
    if (lethality == "viable"):
        for line in Func:
            if line == "\n":
                continue

            tempFUNC = []
            if gene in line and line not in geneSeen:
                geneSeen.append(line)
                line = line.strip()
                line = line.replace("GO","GO:")
                tempFUNC.append(str(line) + "\t0")

                #print tempFUNC
                newFUNC.append(tempFUNC)
            if gene in line and gene not in tempySeen:
                tempySeen.append(gene)
                tempy.write(gene+",viable\n")
                Counter = Counter +1
                print Counter

        #print "Something"
        #print tempFUNC
#FUNCoutputfile.write("\n".join(newFUNC))


for element in newFUNC:
    FUNCoutputfile.write(" ".join(element) + "\n")

########################################################


print(datetime.now() - startTime)
