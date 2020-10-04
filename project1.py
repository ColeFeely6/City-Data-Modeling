#import pandas as pd
import csv


class City: # Init the class to store all the operations needed for each city
    def __init__(self,cid,cname,cstate,pop,cities): # init all the data given
        self.cid = cid
        self.cname = cname
        self.cstate = cstate
        self.pop = pop
        self.cities = cities
    def __str__(self): # Print out the necessary information from LoadData
        return ("cid: "+ str(self.cid) + "; cname: " + str(self.cname) + "; cstate: " \
                + str(self.cstate) +"; cases:" + str(self.cities[len(self.cities)-1]) )



#######################################################################################################################

class COV19Library: # Init the class that will manage all the city objects
    def __init__(self):
        self.cityArray = [] # init the array that stores all the city objects
        self.isSorted = False # return if the cityArray si sorted, init as False
        self.size = len(self.cityArray) # init the size variable that will be given as the length of cityArray


#----------------------------------------------------------------------------------------------------------------------
    def LoadData(self,filename): # Open any csv file given
        with open(filename,'r') as excel_file: # open the file as excel_file
            sheet_1 = csv.reader(excel_file,delimiter = ',') # read and store the info in the var sheet_1
            count = 0 # init the count of number of iterations to avoid the first column that are labels
            for column in sheet_1: # iterate through all the columns in sheet_1
                if count != 0:
                    cid = column[0] # first column will be the id
                    pop = column[2] # third column will be the population size
                    names = column[1] # third column will have the names of the city and state that we will seperate
                    cities = [] # init the var cities that will record an array of the cases


                    temp = names.split() # set a temp var to split by sp the names array as ex: ['Forest','City','AR']
                    cstate = temp[len(temp) - 1] #That last item will always our state(s)
                    newnewtemp = temp[0:len(temp) - 1] # Init a new var that is everything not the state
                    cname = " ".join(newnewtemp) # use the join function but throw a space in between, found using W3S

                    for i in range(4,65): # iterate through the cases data, aka 5th column to the max 66th
                        cities.append(int(column[i])) # add that case to the list
                    # Now for all the data collected for this iteration add it to an instance of city
                    # Add that City Object to the list of all the city objects
                    data = City(cid,cname,cstate,pop,cities)
                    self.cityArray += [data]
                # increment count so we can avoid the first row of labels
                count += 1
                # Update the size of the Library
                self.size = len(self.cityArray)
#----------------------------------------------------------------------------------------------------------------------

    def linearSearch(self,city,attribute):
        self.LoadData('cov19_city.csv')
        if attribute == 'cid':
            for i in range(len(self.cityArray)):
                if str(city) == self.cityArray[i].cid:
                    return self.cityArray[i]
                elif i == len(self.cityArray)-1:
                    return 'City not found'
        elif attribute == 'name':
            for i in range(len(self.cityArray)):
                if city == self.cityArray[i].cname:
                    return self.cityArray[i]
                elif i == len(self.cityArray) - 1:
                    return 'City not found'
        else:
            return 'City not found'

#c = COV19Library()
#print(c.linearSearch(23700,'cid'))