def problem(dic):
    print(dic['1'][0] + dic['2'][0])
    print(dic['1'][0] + dic['2'][1])
    print(dic['1'][1] + dic['2'][0])
    print(dic['1'][1] + dic['2'][1])
    gh = len(dic['1'])
    counter = 0
    g = 0
    k = []
    while g == 0:
        for x in range(len(dic)):
            for y in range(gh):
                for z in range(gh):
                    if x == 0:
                        k.append(str(dic[str(x + 1)][y]) + ',' + str(dic[str(x + 1 + 1)][z])
                    if x == 1:
                        k.append(str(dic[str(x + 1)][y]) + ',' + str(dic[str(x + 1 - 1)][z])

data: {'1': ["a", "b"], "2": ["c", "d"]}
problem(data)