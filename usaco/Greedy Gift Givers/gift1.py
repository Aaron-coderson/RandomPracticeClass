"""
ID: vijayaa1
LANG: PYTHON2
TASK: gift1
"""
fin = open("gift1.in", "r")
fout = open ('gift1.out', 'w')

#get data into var
x = fin.read().split('\n')
data = []
for line in x:
    data.append(line)
# checks how many participants and pops value
num_par = int(data[0])
data.pop(0)


participant = {}
for names in range(num_par):
    participant[data[0]] = 0
    data.pop(0)
print(data)

while data != []:
    giver = data.pop(0)
    amt_rec = data.pop(0).split(' ')
    amount = int(amt_rec[0])
    num_rec = int(amt_rec[1])
    participant[giver] -= amount
    if num_rec ==0:
        break
    if amount % num_rec != 0:
        v = amount % num_rec
        amount = amount - v
        participant[giver] += v
    for i in range(num_rec):
        receiver = data.pop(0)
        participant[receiver] += amount/num_rec


print(participant)


