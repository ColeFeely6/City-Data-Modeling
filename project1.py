#import pandas as pd
import csv


class City:
    def __init__(self,cid,cname,cstate,pop,cities):
        self.cid = cid
        self.cname = cname
        self.cstate = cstate
        self.pop = pop
        self.cities = cities

class COV19Library:
    def __init__(self):
        self.datalist = []
        self.isSorted = False
        self.size = 0
    def __str__(self):
        return ("cid "+self.cid)
    def LoadData(self,filename):
        with open(filename,'r') as excel_file:
            sheet_1 = csv.reader(excel_file,delimiter = ',')
            count = 0
            for row in range(len(sheet_1)):
                if count != 0:
                    cid = row[0]
                    pop = row[2]
                    names = row[1]
                    cstate = []
                    cname = []
                    cities = []
                    for i in range(len(names)):
                        temp = names[i].split(' ')
                        newtemp = temp[len(temp) - 1]
                        cstate.append(newtemp)

                        newnewtemp = temp[0:len(temp) - 1]
                        newstring = ""
                        for i in range(len(newnewtemp)):
                            newstring = newstring + newnewtemp[i]
                            if i != len(newnewtemp):
                                newstring += " "
                            cname.append(newstring)

                    for i in range(4,65):
                        cities.append(int(row[i]))

                    data = City(cid,cname,cstate,pop,cities)
                    self.datalist.append(data)
                count += 1
                self.size = len(self.datalist)




