import random
import argparse
from PIL import Image

numerals = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def inter(a:float,b:float,t:float):
    return int(t*b+(1-t)*a)

def colorToHex(c):
    return (c[2]<<8*2)+(c[1]<<8)+c[0]

def colorInter(a,b,t):
    return (inter(a[0],b[0],t),inter(a[1],b[1],t),inter(a[2],b[2],t))

def colorHist(a,b,c,t):
    if t < 1/2.0:
        return colorInter(a,b,t*2.0)
    return colorInter(b,c,(t-1/2.0)*2)

def colorHist2(lst,t):
    size = len(lst)
    for i in range(0,size-1):
        if t <= (i+1)/(size-1):
            return colorInter(lst[i],lst[i+1],(t-i/float(size-1))*(size-1))



def baseN(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def baseNtodec(n, b):
    number = 0
    for i, digit in enumerate(n):
        number += digit * (b ** (len(n) - i - 1))
    return number


def getstate(last, row, base):
    parent = []
    c = neighbors-int(neighbors/2)-1
    for loc in range(-c,c+1):
        if loc + row >= len(last) or loc + row < 0:
            parent.append(args.boundry_value)
        else: parent.append(last[row + loc])
    bn = baseNtodec(parent, base)
    out = rule_size - 1 - bn
    return rule[out] 


def nextgen(last, base):
    ans = []
    for i in range(len(last)):
        ans += [getstate(last, i, base)]
    return ans

def rotate(l, n):
    return l[n:] + l[:n]

class CustomAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not 'ordered_args' in namespace:
            setattr(namespace, 'ordered_args', [])
        previous = namespace.ordered_args
        previous.append((self.dest, values))
        setattr(namespace, 'ordered_args', previous)

parser = argparse.ArgumentParser()
parser.add_argument('rule',nargs='?', default=-1,type = int)
parser.add_argument('base', nargs='?', default=2, type = int)
parser.add_argument('-c','--colors', nargs='+', type = int, default= [0,0,0xb0,0xf0,0x89,0x13])
parser.add_argument('-n','--neighbors', type = int, default= 3)
parser.add_argument('-d','--dimensions', nargs='+', type = int, default= (700, 350))
parser.add_argument('-r','--random_start',action='store_true')
parser.add_argument('-b','--boundry_value', type = int, default= 0)
parser.add_argument('-m','--rule_mutations' , type = str, default= '')
args = parser.parse_args()

customPalette = [(args.colors[i],args.colors[i+1],args.colors[i+2]) for i in range(0,len(args.colors),3)]

rule_10 = args.rule
base = args.base
neighbors = args.neighbors

rule = []

rule_size = (base ** (neighbors))
if rule_10 < 0 :
    rule = [random.randint(0, base-1) for _ in range(rule_size)]
else:
    rule = baseN(rule_10, base)

if (len(rule) != rule_size):
    pad = [0 for _ in range(0, rule_size - len(rule))]
    rule = pad + rule

while len(rule) > rule_size:
    rule.pop(0)

if len(args.rule_mutations) > 0:
    for m in list(args.rule_mutations):
        if m == "i":
            for i in range(0,len(rule)):
                rule[i] = (base-1) - rule[i]
        elif m == "b":
            rule.reverse()
        elif m == "r":
            rule = rotate(rule,-1)
        elif m == "l":
            rule = rotate(rule,1)


dem = tuple(args.dimensions)
gens = []
ans = []

ans = [0 for _ in range(int(dem[0]/2))]
gens = ans + [base - 1] + ans

if args.random_start:
    gens = [random.randint(0, base-1) for i in range(0,dem[0])]

img = Image.new('RGB',dem)
pixels = img.load()
for row in range(0, dem[1]):
    for col in range(0,len(gens)-1):
        cellIndex = float(gens[col]/float(base-1))
        color = colorHist2(customPalette,cellIndex)
        pixels[col,row]= color
    gens = nextgen(gens, base)
img.save('test.png')

print(baseNtodec(rule,base))





# base 5 24203034231100402041314421044124123423211313212020442000121103242401143234213221044323220312234012114302422423421144442030244231440143121300313044133341102434001334343440042222210
