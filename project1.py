#import pandas as pd
import csv


class City:
    def __init__(self,cid,cname,cstate,pop,cities):
        self.cid = cid
        self.cname = cname
        self.cstate = cstate
        self.pop = pop
        self.cities = cities
    def __str__(self):
        return ("cid: "+ str(self.cid) + "; cname: " + str(self.cname) + "; cstate: " \
                + str(self.cstate) +"; cases:" + str(self.cities) )



#######################################################################################################################

class COV19Library:
    def __init__(self):
        self.cityArray = []
        self.isSorted = False
        self.size = 0
#----------------------------------------------------------------------------------------------------------------------
    def LoadData(self,filename):
        with open(filename,'r') as excel_file:
            sheet_1 = csv.reader(excel_file,delimiter = ',')
            count = 0
            for row in sheet_1:
                if count != 0:
                    cid = row[0]
                    pop = row[2]
                    names = row[1]
                    cities = []


                    temp = names.split()
                    cstate = temp[len(temp) - 1]
                    newnewtemp = temp[0:len(temp) - 1]
                    cname = " ".join(newnewtemp)

                    for i in range(4,65):
                        cities += [int(row[i])]

                    data = City(cid,cname,cstate,pop,sum(cities))
                    self.cityArray += [data]
                count += 1
                self.size = len(self.cityArray)
#----------------------------------------------------------------------------------------------------------------------