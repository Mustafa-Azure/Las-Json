from email import header
import json
from typing import final
from unicodedata import name
import lasio
import pandas as pd

las = lasio.read('Sample1.las')
#ls = las.to_json()
#print(ls)
lasdf = las.df()
#print(las.curves['DEPT'])
curveList = las.curves
#print(las.well.WELL.value)
#print(las.curves.GR.mnemonic)
dict1={}
i=0
tempdict = {}
for c in curveList:
    
    items = {}
    #print(c)
    items = {"name":"","description":"","quantity":"","unit":"","valueType":"","dimensions":""} 
    items['name'] = c.mnemonic
    tempdict[i] = items
    #print(c.mnemonic)
    #print("name" ":" + str(c.mnemonic) + "," + "description" + ":" + str(c.descr)+ "," + "quantity" + ":" + str(c.descr)+ "," + "unit" + ":" + str(c.descr)+ "," + "valueType" + ":" + str(c.descr)+ "," + "dimensions" + ":" + str(c.descr))
    #temp="name" ":" + str(c.mnemonic) + "," + "description" + ":" + str(c.descr)+ "," + "quantity" + ":" + str(c.descr)+ "," + "unit" + ":" + str(c.descr)+ "," + "valueType" + ":" + str(c.descr)+ "," + "dimensions" + ":" + str(c.descr)
    #dict1=temp
    #print("##################")
    i=i+1

print(tempdict)
#print(json.dumps(dict1))
json_string = json.dumps(las.curves['DEPT'])
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
workingdf1 = workingdf["GR"]
#print(workingdf1)
df2 = workingdf1.to_json(orient = 'table')
#print(df2)
########################################################################################################
FinalDict = {}
headerItems = {"header":{"well":"","country":"","date":"","startIndex":"","endIndex":"","step":""},"curves":[],"data":[]}

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


finalc[0] = c1
finalc[1] = c2
headerItems['curves'] = finalc

FinalDict.update(headerItems)
#print(json.dumps(FinalDict))