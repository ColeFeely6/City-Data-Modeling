'''sheet_1 = pd.read_csv(filename)

        cid = (sheet_1['City_ID'])
        names = (sheet_1['City State'])
        pop = (sheet_1['POP10'])
        cities = sheet_1.iloc[:,'5/1/20':'6/30/20'] # lines 6 - 66
        cstate = []
        cname = []

        for i in range(len(names)):
            temp = names.at[i].split(' ')
            newtemp = temp[len(temp) - 1]
            cstate.append(newtemp)

            newnewtemp = temp[0:len(temp) - 1]
            newstring = ""
            for i in range(len(newnewtemp)):
                newstring = newstring + newnewtemp[i]
                if i != len(newnewtemp):
                    newstring += " "
            cname.append(newstring)



        for i in range(len(cid)):

            data = City(cid[i], cname[i], cstate[i], pop[i], cities[i])
            self.datalist.append(data)
        self.size = len(self.datalist)'''

'''sheet_1 = pd.read_excel(r'cov19_city.xlsx',sheet_name='cov19_city')

cid = (sheet_1['City_ID'])
names = (sheet_1['City State'])
cities = sheet_1.columns[5:65]
cstate = []
cname = []

for i in range(len(names)):
    temp = names.at[i].split(' ')
    newtemp = temp[len(temp) - 1]
    cstate.append(newtemp)

    newnewtemp = temp[0:len(temp) - 1]
    newstring = ""
    for i in range(len(newnewtemp)):
        newstring = newstring + newnewtemp[i]
        if i != len(newnewtemp):
            newstring += " "
    cname.append(newstring)

pop = (sheet_1['POP10'])

print(cid[0])
print(cname[0])
for i in range(len(cid)):
    datalist = []
    data = City(cid[i],cname[i],cstate[i],pop[i],cities[i])
    datalist.append(data)'''