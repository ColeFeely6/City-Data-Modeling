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
class TreeNode:
    class TreeNode:
        def __init__(self, key, val, left=None, right=None, parent=None):
            self.key = key
            self.payload = val
            self.leftChild = left
            self.rightChild = right
            self.parent = parent
            self.balanceFactor = 0

        def hasLeftChild(self):
            return self.leftChild

        def hasRightChild(self):
            return self.rightChild

        def isLeftChild(self):
            return self.parent and self.parent.leftChild == self

        def isRightChild(self):
            return self.parent and self.parent.rightChild == self

        def isRoot(self):
            return not self.parent

        def isLeaf(self):
            return not (self.rightChild or self.leftChild)

        def hasAnyChildren(self):
            return self.rightChild or self.leftChild

        def hasBothChildren(self):
            return self.rightChild and self.leftChild

#######################################################################################################################

class COV19Library: # Init the class that will manage all the city objects
    def __init__(self):
        self.cityArray = [] # init the array that stores all the city objects
        self.isSorted = False # return if the cityArray si sorted, init as False
        self.size = len(self.cityArray) # init the size variable that will be given as the length of cityArray
        self.root = None

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
        if attribute == 'id': # If the attribute passed in is a id
            for i in range(len(self.cityArray)): # iterate through out list
                if str(city) == self.cityArray[i].cid: # If found return that city object
                    return self.cityArray[i]
                elif i == len(self.cityArray)-1: # Else if we are at the end of the list and not found, say so
                    return 'City not found'
        elif attribute == 'name': # If the attribute passed in is a name
            for i in range(len(self.cityArray)): # iterate through out list
                if city == self.cityArray[i].cname:# If found return that city object
                    return self.cityArray[i]
                elif i == len(self.cityArray) - 1: # Else if we are at the end of the list and not found, say so
                    return 'City not found'
        else:
            return 'City not found'
#----------------------------------------------------------------------------------------------------------------------

## TODO I think that this function is creating new names because there should be 942 terms but there are 1884
    ## TODO check and see if proper swapping

    def quickSort(self):
        self.quicksorthelper(0,self.size-1)
        self.isSorted = True


    def quicksorthelper(self, first, last):
        if first < last:
            splitpoint = self.partition(first,last)

            self.quicksorthelper(first,splitpoint - 1)
            self.quicksorthelper(splitpoint + 1,last)

    def partition(self,first,last):
        pivot= self.cityArray[first].cname

        left = first + 1
        right = last

        done = False
        while not done:
            while left <= right and self.cityArray[left].cname <= pivot:
                left = left + 1
            while self.cityArray[right].cname >= pivot and right >= left:
                right = right - 1
            if right < left:
                done = True
            else:
                temp = self.cityArray[left]
                self.cityArray[left] = self.cityArray[right]
                self.cityArray[right] = temp
                #swap

        temp = self.cityArray[first]
        self.cityArray[first] = self.cityArray[right]
        self.cityArray[right] = temp
        #swap

        return right

#-----------------------------------------------------------------------------------------------------------------------

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)


c = COV19Library()
c.quickSort()
for i in

#print(c.linearSearch('23700','id'))