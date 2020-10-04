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
        self.cityArray = []
        self.isSorted = False
        self.size = 0
    def __str__(self,n):
        return ("cid: "+ str(self.cityArray[n].cid) + " name: " + str(self.cityArray[n].cname) + " state: " \
                + str(self.cityArray[n].cstate) + " population: " + str(self.cityArray[n].pop) + \
                " cases: " + str(self.cityArray[n].cities) )
    def LoadData(self,filename):
        with open(filename,'r') as excel_file:
            sheet_1 = csv.reader(excel_file,delimiter = ',')
            count = 0
            for row in sheet_1:
                if count != 0:
                    cid = row[0]
                    pop = row[2]
                    names = row[1]
                    cname = ""
                    cities = []
                    temp = names.split(' ')
                    cstate = temp[len(temp) - 1]
                    newnewtemp = temp[0:len(temp) - 1]
                    newstring = ""
                    for i in range(len(newnewtemp)):
                        newstring = newstring + newnewtemp[i]
                        if i != len(newnewtemp):
                            newstring += " "
                        cname = cname + newstring

                    for i in range(4,65):
                        cities.append(int(row[i]))

                    data = City(cid,cname,cstate,pop,cities)
                    self.cityArray.append(data)
                count += 1
                self.size = len(self.cityArray)



