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

r = '{:0>8s}'.format(int2base(102,2))
inRule = {'base':2,'neighbors':3,'rule':r,'range':''}
outRule = {'base':5,'neighbors':3,'rule':'','range':''}

inRule['range']=getRange(inRule['base'],inRule['neighbors'])
outRule['range']=getRange(outRule['base'],outRule['neighbors'])

pattern = r'{}{}{}'
outRule['rule'] = outRule['range']

for i,parent in enumerate(inRule['range'].split()):
    intParent = tuple(map(int,list(parent.replace('1','2').replace('0','1'))))
    regex = re.compile(pattern.format(*intParent), re.S)
    if inRule['rule'][i] == '1':
        outRule['rule'] = regex.sub(lambda m: m.group().replace(m.group(),'2',1), outRule['rule'])
    if inRule['rule'][i] == '0':
        outRule['rule'] = regex.sub(lambda m: m.group().replace(m.group(),'1',1), outRule['rule'])

r = '{:0>8s}'.format(int2base(60,2))
inRule['rule'] = r
pattern = r'{}{}{}'

for i,parent in enumerate(inRule['range'].split()):
    intParent = tuple(map(int,list(parent.replace('0','3').replace('1','4'))))
    regex = re.compile(pattern.format(*intParent), re.S)
    if inRule['rule'][i] == '1':
        outRule['rule'] = regex.sub(lambda m: m.group().replace(m.group(),'4',1), outRule['rule'])
    if inRule['rule'][i] == '0':
        outRule['rule'] = regex.sub(lambda m: m.group().replace(m.group(),'3',1), outRule['rule'])

regex = re.compile(r'\d{'+str(outRule['neighbors'])+r'}', re.S)
outRule['rule'] = regex.sub(lambda m: m.group().replace(m.group(),'0',1), outRule['rule'])

outRule['rule'] = (outRule['rule'].replace(' ',''))

#print(outRule['range'])
#print(inRule['range'])
#print(outRule['rule'])
print(baseNtodec(list(map(int,list(outRule['rule']))),outRule['base']))
