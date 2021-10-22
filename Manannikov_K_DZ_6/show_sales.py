from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as f:
    zaq = []
    for line in f.read().splitlines():
        zaq.append(line)

if len(argv) == 1:
    print(zaq)
elif len(argv) == 2:
    print(zaq[1])
else:
    q = int(argv[1]) - 1
    s = int(argv[2])
    print(zaq[q:s])
