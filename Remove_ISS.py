'''
Created on 25 Oct 2015

@author: nid16
'''

import csv
import codecs


#inputfile = open('./Gene&GO_F_With_Lethality.txt', mode='r')
inputfile = open('./Gene&GO_F_No_IMP.txt', mode='r')#To remove IMP and ISS
outputfile = open('./Gene&GO_F_No_ISS.txt', mode='w')

inputfile = csv.reader(inputfile, delimiter=',')

previous = None


writer = csv.writer(outputfile)



for rows in inputfile:
        for index, words in enumerate(rows):
            previous = rows[index-1]
            current = rows[index]
            if index-1 != -1:
                if "viable" in rows[-1] or "lethal" in rows[-1]:# and "GO" in rows:
                    while "ISS" in rows[index] and "GO" in previous:
                            rows.pop(index-1)
                            if "GO" != rows:
                                break
                else:
                    Null = "Null"
        #if rows[-1] == "viable" or rows[-1] == "lethal":
        if "viable" in str(rows[-1]) or "lethal" in str(rows[-1]):

            if "GO" in str(rows):
                writer.writerow(rows)
                print rows
