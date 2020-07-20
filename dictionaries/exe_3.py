from dictionaries.exe_1 import *
dicSum=create_dic()
dicNew={}
keys=list(dicSum.keys())
value=list(dicSum.values())
for i in range (len(keys)):
    dicNew.update({keys[len(keys)-1-i]:value[len(value)-1-i]})
print(dicNew)