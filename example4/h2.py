import time

with open('list.txt', 'r') as L:
    contents = (L.read())
    l = [str(i) for i in contents.split('\n')]
    l.remove('')

#print(l)

look = True
index = 50000

if "222222" in l:
    print("Niceeeee")

while look:
    time.sleep(0.00005)
    if l[index] == "222222":
        look = False
        print(index)
    else:
        index += 1
    if l[index] == 100000:
        look = False

