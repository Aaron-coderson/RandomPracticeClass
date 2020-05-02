"""
ID: vijayaa1
LANG: PYTHON3
TASK: ride
PROG: ride
"""

#import sys

fin = open("ride.in", "r")
fout = open ('ride.out', 'w')

x = fin.readline()
y = fin.readline()

numbersa = []

for each in x:
  number = ord(each.lower())-96
  numbersa.append(number)

numbersb = []

for each in y:
  number = ord(each.lower())-96
  numbersb.append(number)

numa = 1
for number in numbersa[0:len(x)-1]:
    if number >0 and number<27:
        numa = numa*number

numb = 1
for number in numbersb:
    if number >0 and number<27:
        numb = numb*number

numa = numa%47
numb = numb%47

if numa==numb:
    fout.write('GO')
    fout.write('\n')
    fout.close()
else:
    fout.write('STAY')
    fout.write('\n')
    fout.close()