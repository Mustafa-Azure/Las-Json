from array import array
from email import header
from email.headerregistry import Address
import json
import telnetlib
from typing import final
from unicodedata import name
import lasio
import pandas as pd

las = lasio.read('Sample1.las')
#ls = las.to_json()
#print(ls)
#print(las.keys())
lasdf = las.df()
#print(las.curves['DEPT'])
curveList = las.curves
#print(las.well.WELL.value)
#print(las.curves.GR.mnemonic)
dict1={}
i=0
tempdict = []
for c in curveList:
    
    items = {}
    #print(c)
    items = {"name":"","description":"","quantity":"","unit":"","valueType":"","dimensions":""} 
    if i==0:
          # Filling in values for DEPTH
          items['name'] = "MD"
          items['description'] = "Measured depth"
          items['quantity'] = "length"
          items['unit'] = "m"
          items['valueType'] = "float"
          items['dimensions'] = 1
    else:
          #Filling in values of other curves based on available data in curve section
          items['name'] = c.mnemonic
            
          items['description'] = c.descr
          items['quantity'] = ""
          items['unit'] = c.unit
          items['valueType'] = ""
          items['dimensions'] = ""
    tempdict.append(items)
    #print(tempdict[i])
    #print(c.mnemonic)
    #print("name" ":" + str(c.mnemonic) + "," + "description" + ":" + str(c.descr)+ "," + "quantity" + ":" + str(c.descr)+ "," + "unit" + ":" + str(c.descr)+ "," + "valueType" + ":" + str(c.descr)+ "," + "dimensions" + ":" + str(c.descr))
    #temp="name" ":" + str(c.mnemonic) + "," + "description" + ":" + str(c.descr)+ "," + "quantity" + ":" + str(c.descr)+ "," + "unit" + ":" + str(c.descr)+ "," + "valueType" + ":" + str(c.descr)+ "," + "dimensions" + ":" + str(c.descr)
    #dict1=temp
    #print("##################")
    i=i+1

#print(tempdict)
#print(json.dumps(tempdict))
#print(json.dumps(dict1))
#json_string = json.dumps(las.curves['DEPT'])
#print(json_string)
#print(curveList)
#print(lasdf)
#print(lasdf)
df_list = []
#lasdf['WELL'] = las.well.WELL.value
#lasdf['DEPTH'] = lasdf.index
df_list.append(lasdf)
workingdf = pd.concat(df_list, sort=False)
#print(workingdf)
#workingdf1 = workingdf['RHOB']

#Adding DEPTH as column - Gets added at the end by default
address = las['DEPT']
lasdf['DEPT'] = address
#print(lasdf)
#lasdf.columns = las.keys()
#Changing the order of columns (DEPTH in the begginning)
cols = lasdf.columns.tolist()
print(cols)
cols = cols[-1:] + cols[:-1]
print(cols)
lasdf = lasdf[cols]

#changing Nan to -999.25
df1 = lasdf.astype(object).where(pd.notnull(lasdf),-999.25)
print(df1)
tempdata = []
tempdata = lasdf
#print(tempdata)
#tempdatalist = tempdata.tolist()
#print(tempdatalist)

# define a list
l=[]
i=0
a=[]
a = lasdf.values
#print(a)
b=json.dumps(a.tolist())

########################################################################################################
FinalDict = {}
headerItems = {"header":{"well":"","country":"","date":"","startIndex":"","endIndex":"","step":""},"curves":[{}],"data":[]}

#print(las.well)

headerItems['header']['well'] = las.well.WELL.value
headerItems['header']['country'] = las.well.PROV.value
headerItems['header']['date'] = las.well.DATE.value
headerItems['header']['startIndex'] = las.well.STRT.value
headerItems['header']['endIndex'] = las.well.STOP.value
headerItems['header']['step'] = las.well.STEP.value

#print(json.dumps(headerItems))


finalc = {}
c1 =  {
        "name": "MD",
        "description": "Measured depth",
        "quantity": "length",
        "unit": "m",
        "valueType": "float",
        "dimensions": 1
      }
c2 =  {
        "name": "GR",
        "description": "Measured depth",
        "quantity": "length",
        "unit": "m",
        "valueType": "float",
        "dimensions": 1
      }


#Filling Curves Data
headerItems['curves'] = tempdict

#Filling Log Data - ASCII values
headerItems['data'] = a.tolist()
FinalDict.update(headerItems)
#print(json.dumps(FinalDict))

#################################### Data Section#############################################
