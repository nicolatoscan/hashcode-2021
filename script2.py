import sys
import time
import random
import math
from collections import Counter


seed = random.random()
print('seed', seed)
random.seed(seed)

inputs = ['a', 'b', 'c', 'd', 'e', 'f']
if len(sys.argv) <= 1:
    selected_inputs = inputs
else:
    selected_inputs = [sys.argv[1]]

roadCounter = Counter()
for file in selected_inputs:
    print(file, time.time() * 1000)
    inp = f"input/{file}.txt"
    out = f"output/{file}.txt"
    streets = {}
    percorsi = []
    with open(inp) as f:
        [duration, nItersections, nStreets, nCars, puntoni] = [int(x) for x in f.readline().strip('\n').split(' ')]

        for i in range(0, nStreets):
            [start, end, streenName, ll] = f.readline().strip('\n').split(' ')
            start = int(start)
            end = int(end)
            ll = int(ll)
            # start end lenght nonso usage
            streets[streenName] = [start, end, ll, False, 0]

        for i in range(0, nCars):
            strada = f.readline().strip('\n').split(' ')[1:]
            percorsi.append(strada)
            roadCounter.update(strada)

    intersezioniInput = []
    intersezioniOutput = []
    for i in range(0, nItersections):
        intersezioniInput.append([])
        intersezioniOutput.append([])

    for stradaName in streets:
        streetData = streets[stradaName]
        intersezioniInput[streetData[1]].append(stradaName)
        intersezioniOutput[streetData[0]].append(stradaName)


    with open(out, 'w') as f:
        f.write(f"{nItersections}\n")
        #print(nItersections)

        for i in range(0, nItersections):
            #print('a', intersezioniInput[i])
            stradeUsate = [x for x in intersezioniInput[i] if roadCounter[x] != 0]
            # print('b', pippo)
            # print('----')

            if len(stradeUsate) == 0:
                f.write(f"{i}\n")
                f.write(f"1\n")
                f.write(f"{intersezioniInput[i][0]} 1\n")
                continue

            
            pesi = [[roadCounter[s], s] for s in stradeUsate]
            pesi.sort()
            #pesi.reverse()

            
            #pesi = [x for x in pesi if ]
            
            f.write(f"{i}\n")
            f.write(f"{len(stradeUsate)}\n")
            #print(len(pippo))
            ii = len(pesi)
            for s in pesi:
                f.write(f"{s[1]} {ii}\n")
                #print(f"{s} 2")
                ii -= 1