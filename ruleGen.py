import string
import re


digs = string.digits + string.ascii_letters

def baseNtodec(n, b):
    number = 0
    for i, digit in enumerate(n):
        number += digit * (b ** (len(n) - i - 1))
    return number

def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)

def getRange(base,numDigits):
    out = ''
    for i in range((base**numDigits)-1,-1,-1):
        out += (('{:0>'+'{}'.format(numDigits)+'s} ').format(int2base(i,base)))
    return out

r = '{:0>8s}'.format(int2base(90,2))
inRule = {'base':2,'neighbors':3,'rule':r,'range':''}
outRule = {'base':3,'neighbors':5,'rule':'','range':''}

inRule['range']=getRange(inRule['base'],inRule['neighbors'])
outRule['range']=getRange(outRule['base'],outRule['neighbors'])

pattern = r'{}\d{}\d{}'
outRule['rule'] = outRule['range']

for i,parent in enumerate(inRule['range'].split()):
    intParent = tuple(map(int,list(parent)))
    regex = re.compile(pattern.format(*intParent), re.S)
    outRule['rule'] = regex.sub(lambda m: m.group().replace(m.group(),inRule['rule'][i],1), outRule['rule'])


regex = re.compile(r'\d{'+str(outRule['neighbors'])+r'}', re.S)
outRule['rule'] = regex.sub(lambda m: m.group().replace(m.group(),'0',1), outRule['rule'])

outRule['rule'] = (outRule['rule'].replace(' ',''))

#print(outRule['range'])
#print(inRule['range'])
#print(outRule['rule'])
print(baseNtodec(list(map(int,list(outRule['rule']))),outRule['base']))
