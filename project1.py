# Cole Feely
# Due Oct. 7, 2020
# ECE 241 Project 1



import csv # For Task 2
#import time # for Task 7,8 and 9
#import random # for Task 7,8 and 9
#import matplotlib.pyplot as plt #for plotting in task 10
#import numpy as np # for plotting for task 10

#######################################################################################################################
class City: # Init the class to store all the operations needed for each city
    def __init__(self,cid,cname,cstate,pop,cities): # init all the data given
        self.cid = cid
        self.cname = cname
        self.cstate = cstate
        self.pop = pop
        self.cities = cities
        self.lastcase = cities[len(cities)-1]
    def __str__(self): # Print out the necessary information from LoadData
        return ("cid: "+ str(self.cid) + "; cname: " + str(self.cname) + "; cstate: " \
                + str(self.cstate) +"; cases:" + str(self.lastcase) )

#######################################################################################################################
# Use the class treenode given in class for the AVL tree. This way we can have the characteristics of a binary tree
# and the nodes, but store out Class City Objects in the tree

class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0 # Esp Useful for determining weight for our AVL tree

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
class AVLTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val): # This put method will be used for the buildBST method for the COV19LIB Class
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode): # Same as BST but add the balancing component
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self,node): # Basically, we only want out nodes to have a balance of 0,-1, or 1. If its not, rebal
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self,rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot):
        newRoot = rotRoot.leftChild

        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
            else:
                rotRoot.parent.leftChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(rotRoot.balanceFactor, 0)

    def rebalance(self,node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key): # This method will be use for the Search BST method in COV19Lib
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return str(res.payload) # Make sure to return the __str__ of our Class methof
           else:
                  return 'City not found' # Return if the city does not exist in db
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

########################################################################################################################

class COV19Library: # Init the class that will manage all the city objects
    def __init__(self):
        self.cityArray = [] # init the array that stores all the city objects
        self.isSorted = False # return if the cityArray si sorted, init as False
        self.size = len(self.cityArray) # init the size variable that will be given as the length of cityArray
        self.root = None # Create a root for our BST function

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

                    if names == "Nashville-Davidson--Murfreesboro--Frankl": # Our specific corner case to avoid!
                        cstate = "" # No state given
                        cname = names # That big long string is the name of the city
                    else:
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
        #self.LoadData('cov19_city.csv')
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
#-----------------------------------------------------------------------------------------------------------------------
# Methods used for Tasks 10 and 11
    def maxpopfinder(self):
        maxpop = 0 # init a var = 0
        for  i in range(len(self.cityArray)): # iterate through all our city objects
            pop = int(self.cityArray[i].pop) # record population
            if pop > maxpop: # if population is the max population thus far
                maxpop = pop # save that population
                returnpop = self.cityArray[i] # save that city
        return returnpop # Return city with max population

    def maxcasefinder(self):
        maxcases = 0 # init the max cases as zero
        for i in range(len(self.cityArray)):
            startofJune = self.cityArray[i].cities[30] # value at the start of June
            endofJune = self.cityArray[i].cities[60] # Last value in the cities array
            pop = int(self.cityArray[i].pop) # Return the population of city
            rate = (endofJune - startofJune) / pop # Find the rate in june
            if rate > maxcases:
                returnrate = self.cityArray[i]
        return returnrate

#----------------------------------------------------------------------------------------------------------------------
# Manipulate our quickSort given in class to sort out list of Cities
# We can use python's ability to alphabetise like numbers that are greater and less than
# Basicallay all we need to change is int he comparisons, compare self.cityArray[i].cname
    def quickSort(self): # Keep same
        self.quicksorthelper(0,self.size-1)
        self.isSorted = True


    def quicksorthelper(self, first, last): #Keep same
        if first < last:
            splitpoint = self.partition(first,last)

            self.quicksorthelper(first,splitpoint - 1)
            self.quicksorthelper(splitpoint + 1,last)

    def partition(self,first,last):
        pivot= self.cityArray[first].cname # Make the pivot the first city in our unsorted list

        left = first + 1 # increment position of first
        right = last

        done = False
        while not done:
            while left <= right and self.cityArray[left].cname <= pivot: # iterate until left is <= to piv or right=left
                left = left + 1 #
            while self.cityArray[right].cname >= pivot and right >= left:# iterate until right >= to piv or right=left
                right = right - 1
            if right < left: # If they cross, end the loop
                done = True
            else:
                temp = self.cityArray[left] # If while loops ended but never crossed
                self.cityArray[left] = self.cityArray[right] #Swap the Cities in those Arrays
                self.cityArray[right] = temp


        temp = self.cityArray[first]  #Swap cities again
        self.cityArray[first] = self.cityArray[right]
        self.cityArray[right] = temp


        return right # Return the poistion of right

#-----------------------------------------------------------------------------------------------------------------------

# Take advantage of the class given in class and use buildBST as the put method of the AVL tree
    def buildBST(self):
        self.temp = AVLTree() # Create a AVLTree to store our Cities in, make it an attribute so we can call elsewhere
        for i in range(len(self.cityArray)): # Iterate through our list of cities
            # Put our city in the tree with key as id and payload as the actual instance of the City class
            self.temp.put(self.cityArray[i].cid, self.cityArray[i])
        self.root = self.temp.root # update our root of COV19Lib as the root of the AVL tree created

# Use the get method of the AVL tree for the searchBST method
    def searchBST(self,key):
        self.buildBST() # Make sure we have an actual BST first
        return self.temp.get(key) # Call the AVL tree from buildBST and use the get function with the key we want


#-----------------------------------------------------------------------------------------------------------------------
# The following was code used of tasks 10 and 11, not used for the autograder

'''if __name__ == "__main__":
  c = COV19Library()
  c.LoadData('cov19_city.csv')
  prebuild = time.time()
  c.buildBST()
  buildtime = time.time() - prebuild



  cidlist = []
  with open('cov19_city.csv', 'r') as excel_file:  # open the file as excel_file
      sheet_1 = csv.reader(excel_file, delimiter=',')  # read and store the info in the var sheet_1
      count = 0  # init the count of number of iterations to avoid the first column that are labels
      for column in sheet_1:  # iterate through all the columns in sheet_1
          if count != 0:
              cid = column[0]  # first column will be the id
              cidlist.append(cid)
          count += 1 # Makes sure to skip the first row

  searchtimes = [] # init a lis to record all the times recorded
  for i in range(100): # Iterate 100 times
    randint = random.randrange(1, 942) # select a random number from cities 0 to 942
    randcid = cidlist[randint] # find the random id number corresponding to that random number
    presearch = time.time() # Record the time before the search
    c.linearSearch(randcid,'cid') # Perform the search
    aftersearch = time.time() - presearch #record the time difference between after and before the search
    searchtimes.append(aftersearch) # add that time to our list or average times
  averagetime = sum(searchtimes)/len(searchtimes) # Average is the sum of all divided by the amount of terms

  searchtimesBST = [] # again init a list to record all the times taken
  for i in range(100): #iterate 100 times
      randint = random.randrange(1, 942) # select random number
      randcid = cidlist[randint] # find the corresponding id number
      presearch = time.time()
      c.searchBST(randcid)
      aftersearch = time.time() - presearch
      searchtimesBST.append(aftersearch) #add the recorded time to the list

  averagetimeBST = sum(searchtimesBST)/len(searchtimesBST) # find the average time

  print('Search time for Binary Search Tree: ' + str(averagetimeBST) + ' sec')
  print('Linear Search time: ' + str(averagetime) + ' sec')
  print('Build BST time ' + str(buildtime) + ' sec')

  maxpopfinder = c.maxpopfinder()
  print('City with highest population: ' + str(maxpopfinder))
  print('City with highest rate in June: ' + str(c.maxcasefinder()))
  print('the length of maxpopfinder cities is: ' + str(len(maxpopfinder.cities)))
  maxforJune = []
  for i in range(0,61):
      maxforJune.append(c.maxpopfinder().cities[i])
  xaxis = np.arange(1,62)
  plt.plot(xaxis,c.maxpopfinder().cities)
  plt.show
'''