import sys
import time
import random
import math
from collections import Counter

mm = 0

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
            
            # numero macchine nomestrada
            #pesi = [[roadCounter[s], s] for s in stradeUsate]
            pesi = [[roadCounter[s] / streets[streenName][2], s] for s in stradeUsate]
            pesi.sort()
            pesi.reverse()

            tot = sum([p[0] for p in pesi])


            # if i == 499:
            #     #print('p', pesi)
            #     print('tp', len(pesi))
            #     pesi2 = [x for x in pesi if x[0] / tot > 0.002]
            #     #print('p2', pesi2)
            #     print('tp2', len(pesi2))
            #     if len(pesi2) > 0:
            #         pesi = pesi2


            f.write(f"{i}\n")
            f.write(f"{len(pesi)}\n")
            #print(len(pippo))
            ii = len(pesi)
            if ii < 0:
                print("OH HO")
        
            # #SPECIALE E
            # if len(pesi) == 1:
            #     f.write(f"{pesi[0][1]} {duration}\n")
            # elif len(pesi) == 2:
            #     # print(streets[pesi[1][1]][0])
            #     f.write(f"{pesi[0][1]} 2\n")
            #     f.write(f"{pesi[1][1]} 1\n")
            # else:
            #     for s in pesi:
            #         f.write(f"{s[1]} {s[0]}\n")

            for s in pesi:

                sec = roadCounter[s[1]] / random.choice([23, 22, 23, 24, 50, 22, 24, 23, 23,32, 12])
                print(sec)
                f.write(f"{s[1]} {max(1, math.floor(sec))}\n")
                #print(f"{s} 2")
                ii -= 1
