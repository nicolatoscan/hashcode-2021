input = './input/e.txt'

streets = {}
count = 0

with open(input) as f:
    [duration, nItersections, nStreets, nCars, puntoni] = [int(x) for x in f.readline().strip('\n').split(' ')]

    for i in range(0, nStreets):
        [start, end, streenName, ll] = f.readline().strip('\n').split(' ')
        start = int(start)
        end = int(end)
        ll = int(ll)
        # start end lenght nonso usage
        if (start == 499 or end == 499):
            streets[streenName] = [start, end, ll, False, 0]

    for i in range(0, nCars):
        strada = f.readline().strip('\n').split(' ')[1:]
        arr = [x for x in strada if x in streets]
        if len(arr) > 2:
            count += 1

print(count)
