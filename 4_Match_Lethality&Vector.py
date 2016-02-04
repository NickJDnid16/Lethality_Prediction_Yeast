'''
Created on 25 Oct 2015

@author: nid16
'''

import codecs
import time
import linecache
from datetime import datetime

startTime = datetime.now()

OutPut = codecs.open('./Lethality&Vector.txt', encoding='utf-8', mode='w')

lines = 0
for BinLine in codecs.open('./BinVec.txt',encoding='utf-8', mode='r'):
    csv = BinLine.split(",")

    Gene = csv[0]
    Gene.strip("'")
    
    lines = lines +1
    
    line = linecache.getline('./Gene&GO_F_With_Lethality.txt', lines)
    #line = linecache.getline('./Gene&GO_F_No_ISS.txt', lines)
    #line = linecache.getline('./Gene&GO_F_No_IMP.txt', lines)
    count = 0
    
    if "GO" in line:
        print count
        count += 1
        csv[1] = csv[1].replace('\n', '')   
        Ge = line.split(",")
        length = len(Ge) -1
        if Ge[0] == Gene:
      
            if "lethal" in Ge[length]:
                print "lethal"
                
            
                Out = ','.join(csv)
                OutPut.write(Out.strip('\'"'))
                OutPut.write(",lethal")
                OutPut.write("\n")
            
            elif "viable" in Ge[length]:
          
                print "viable"
                Out = ','.join(csv)
                Out = Out.replace('\'','')
                OutPut.write(Out.strip('"\''))
                OutPut.write(",viable") 
                OutPut.write("\n")
     
    else:
        print "NO GO"
    
OutPut.close()
                
print(datetime.now()-startTime)   
