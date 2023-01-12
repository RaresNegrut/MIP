#aparitie numere de 3 cifre
import re
s=str('The human skeleton of an adult consists of around 206 to 213 bones, 80 bones in the axial skeleton and 126 bones in the appendicular skeleton.')
cuv=re.compile("\d{3,}")
print(cuv.findall(s))

#eliminare spatii redundante
import re
s=str(input())
li=re.compile("\w+[.,?:;]*").findall(s)
string=" ".join(li)
print(string)