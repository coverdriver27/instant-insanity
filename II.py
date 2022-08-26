import math

list1 = []
list2 = []
list3 = []
list4 = []


def counter(the_list, n):   #function that ensures only 3 occurences of the same number are used from the generators
    count = the_list.count(n)
    return int(count)


def generator1():   #generator for puzzle 1
    length = int(len(list1))
    n = 1
    while length < 90:
        result = 1 + (math.floor(n * pow(math.pi, 2)) % 30)
        n += 1
        quantity = counter(list1, result)
        if quantity < 3:
            list1.append(result)
            length = int(len(list1))
    return


def generator2():   #generator for puzzle 2
    length = int(len(list2))
    n = 1
    while length < 90:
        result = 1 + (math.floor(n * pow(math.e, 2)) % 30)
        n += 1
        quantity = counter(list2, result)
        if quantity < 3:
            list2.append(result)
            length = int(len(list2))
    return


def generator3():   #generator for puzzle 3
    length = int(len(list3))
    n = 1
    while length < 90:
        result = 1 + ((n*7) % 30)
        n += 1
        quantity = counter(list3, result)
        if quantity < 3:
            list3.append(result)
            length = int(len(list3))
    return


def generator4():   #generator for puzzle4
    length = int(len(list4))
    n = 1
    while length < 90:
        result = 1 + ((n*11) % 30)
        n += 1
        quantity = counter(list4, result)
        if quantity < 3:
            list4.append(result)
            length = int(len(list4))
    return


def slices(da_list):    #converts the raw numbers generated into slices of 3 numbers
    slices = [da_list[x:x+3] for x in range(0, len(da_list), 3)]
    return slices


generator1()
generator2()
generator3()
generator4()
print("Puzzle One Raw Data:")
print(*list1)
print("Puzzle Two Raw Data:")
print(*list2)
print("Puzzle Three Raw Data:")
print(*list3)
print("Puzzle Four Raw Data:")
print(*list4)
print(" ")
print("Puzzle One In Slices:")
slices1 = slices(list1)
print(*slices1)
print("Puzzle Two In Slices:")
slices2 = slices(list2)
print(*slices2)
print("Puzzle Three In Slices:")
slices3 = slices(list3)
print(*slices3)
print("Puzzle Four In Slices:")
slices4 = slices(list4)
print(*slices4)
