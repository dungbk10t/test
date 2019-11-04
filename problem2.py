import re

database = {
    "H" : 1,
    "C" : 12,
    "O" : 16,
    "N" : 14,
    "K" : 39 
}

formula = input("Input: ")
# print(formula)

#Search data inside
s = re.findall('([A-Z][a-z]?)([0-9]*)', formula)
# print(s)
fomula_weight = 0

for elem, count in s:
        #For singular elements
        if count=='':
            count = 1

        fomula_weight += int(count)*database[elem]    
    
print("%s : %d"%(formula,fomula_weight))