# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
myList=[{'dec':a,'bin':str(bin(a)),'oct':str(oct(a)),'hex':str(hex(a))} for a in range(0,16)]
pprint(myList)