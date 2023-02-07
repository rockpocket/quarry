#run, dear god run for you life

import pandas as pd
import re

sr = pd.Series(['New_Yokr', 'Libson', 'Tokyo', 'Paris', 'Munich'])

idx = ['City 1', 'City 2', 'City 3', 'City 4', 'City 5']

sr.index = idx

print(sr)


variable = 'integer'
string = True
boolean = 1.0
float = False
integer = '123'

#print("The variable's data type is",type(variable),"it's object value is",variable)
#print("The string's data type is",type(string),"it's object value is",string)
#print("The boolean's data type is",type(boolean),"it's object value is",boolean)
#print("The float's data type is",type(float),"it's object value is",float)
#print("The integer's data type is",type(integer),"it's object value is",integer)