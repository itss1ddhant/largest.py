largest = None
print('Before:', =largest)
for iterval in [41,3, 12, 9, 74, 15]:
    if largest is None or largest < iterval:
        largest = iterval
    print('Loop:', iterval, largest)
print('Largest:', largest)
