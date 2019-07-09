import random

numerals = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


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
    for loc in [-1, 0, 1]:
        if loc + row >= len(last) or loc + row < 0:
            parent.append(0)
        else: parent.append(numerals.find(last[row + loc]))
    out = rule_size - baseNtodec(parent, base)
    return rule[out] 


def nextgen(last, base):
    ans = ""
    for i in range(len(last)):
        ans += getstate(last, i, base)
    return ans


rule_10 = int(input("Enter rule(as decimal number):"))
base = int(input("Enter base(as decimal number):"))

rule_size = (base ** 3) - 1
if rule_10 < 0 :
    newRule = ''
    for _ in range(rule_size):
        newRule += str(random.randint(0, 9))
    rule_10 = int(newRule)

rule_list = baseN(rule_10, base)

rule = ''
for n in rule_list:
    rule += numerals[n]

if (len(rule) != rule_size):
    pad = ''
    for _ in range(0, rule_size - len(rule) + 1):
        pad += '0'
    rule = pad + rule

dem = (100, 50)
gens = []
ans = ""
for _ in range(int(dem[0] / 2)):
    ans += "0"
gens += [ans + numerals[base - 1] + ans]

for row in range(1, dem[1]):
    gens += [nextgen(gens[row - 1], base)]
for line in gens:
    print(line.replace("0", " "))

