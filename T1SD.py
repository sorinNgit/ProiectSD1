import random
import time

#Radix Sort

def radixSort(v):
    if len(v) == 0:
        return "Vector nul"
    RADIX = 10
    placement = 1
    cifmax = max(v)
    while placement < cifmax:
      buckets = [list() for _ in range( RADIX )]
      for i in v:
        d = int((i / placement) % RADIX)
        buckets[d].append(i)
      a = 0
      for b in range( RADIX ):
        buck = buckets[b]
        for i in buck:
          v[a] = i
          a =a + 1
      placement = placement * RADIX
    return v

# Merge Sort

def interclasare(lst, ldr):
    i = j = 0
    rez = []
    while i < len(lst) and j < len(ldr):
        if lst[i] <= ldr[j]:
            rez.append(lst[i])
            i += 1
        else:
            rez.append(ldr[j])
            j += 1
    rez.extend(lst[i:])
    rez.extend(ldr[j:])
    return rez


def mergeSort(ls):
    if len(ls) == 0:
        return "Vector nul"
    if len(ls) == 1:
        return ls
    mij = len(ls) // 2
    lst = mergeSort(ls[:mij])
    ldr = mergeSort(ls[mij:])
    return interclasare(lst, ldr)


# Quick Sort

def alegere_pivot(v):
    if (len(v)<=5):
        return v[len(v)//2]
    else:
        med=[]
        A=[v[i:i+5] for i in range (0,len(v),5)]
        for i in A:
            med.append(i[len(i)//2])
    return alegere_pivot(med)

def quickSort(v):
    L = [] #less
    E = [] #equal
    G = [] #grater
    if len(v) > 1:
        pivot = alegere_pivot(v)
        for i in v:
            if i < pivot:
                L.append(i)
            elif i == pivot:
                E.append(i)
            elif i > pivot:
                G.append(i)
        return quickSort(L)+E+quickSort(G)
    else:
        return v

# Bubble Sort

def bubbleSort(v):
    if len(v) == 0:
        return "Vector nul"
    n = len(v)
    aux = v.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if aux[j] > aux[j + 1]:
                aux[j], aux[j + 1] = aux[j + 1], aux[j]
    return aux


# Shell Sort

def gapInsertionSort(starting_index,list,gap): # luat de pe net
    for item_index in range(starting_index,len(list),gap):
        current_position = item_index
        next_position = current_position+gap

        while next_position <len(list):
            if list[current_position] > list[next_position]:
                list[current_position],list[current_position+gap] = list[current_position+gap],list[current_position]
            current_position = next_position
            next_position = next_position+gap

    return list

def shellSort(v):
    gap = len(v)//2

    while gap >0:
        for i in range(gap):
            v=gapInsertionSort(i,v,gap)

        gap = gap // 2

    return v

# Functia testSort

def testSort(q, p):
    if q == sorted(p):
        return "Vectorul este corect sortat"
    else:
        return "Vectorul NU este corect sortat"


# Generator numere random

def vector_random(n, max):
    random1 = []
    for i in range(n):
        random1.append(random.randint(1, max))

    return random1

#Citire vector din fisier
with  open("input.txt", "r") as f:
    intrare = f.read()
intrare = intrare.split()
for i in range(len(intrare)):
    intrare[i] = int(intrare[i])
v = intrare

# In caz ca vrem ca vectorul sa fie random (vector_random(nr_elem, elem_max))

v = vector_random(20, 100)

g=open("output.out","w")

g.write("Vectorul este: " +str(v)+"\n")

sortari=[bubbleSort,radixSort,mergeSort,shellSort,quickSort]

for sortare in sortari:
    g.write(str(sortare) + ': ')
    v0=v
    timp_initial = time.time()
    q=sortare(v0)
    timp_final = time.time()
    if sortare==quickSort:
        if len(v)==0:
            q="Vector nul"
    g.write(str(q) + '\n')
    if q != "Vector nul":
        g.write(str(testSort(q,v0))+'\n')
        g.write(str(timp_final - timp_initial)+'\n')

