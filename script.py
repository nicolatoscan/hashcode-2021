import sys
import time
import random
import math

seed = random.randint()
print('seed', seed)
random.seed(seed)

inputs = ['a', 'b', 'c', 'd', 'e', 'f']
if len(sys.argv) <= 1:
    selected_inputs = inputs
else:
    selected_inputs = [sys.argv[1]]

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
            streets[streenName] = [start, end, ll, False]

        for i in range(0, nCars):
            strada = f.readline().strip('\n').split(' ')[1:]
            percorsi.append(strada)

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
            streets = intersezioniInput[i]
            f.write(f"{i}\n")
            f.write(f"{len(streets)}\n")
            #print(len(streets))
            
            for s in streets:
                f.write(f"{s} {random.randint(2, math.ceil(duration / 3))}\n")
                #print(f"{s} 2")

