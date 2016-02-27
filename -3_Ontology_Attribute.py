'''
Created on 26 Oct 2015

@author: nid16
'''

import codecs 

output = open('./Ontology_Attributes.txt', mode='wb')

line = 0 

for Line in open('./Refined_GO_Nodes.txt', mode='rb'):
    line = line+1
    print(line)
    output.write("@attribute ")
    Line = Line.replace("\n", "")
    output.write(Line)
    output.write(" {1,0}")
    output.write("\n")
    
output.close()