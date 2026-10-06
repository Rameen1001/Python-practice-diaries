coordinates=(10,20)
print(coordinates)
#coordinates[0]=50 # tuples can't be changed
coordinates=list((coordinates))
print(coordinates)
coordinates.remove(10)
print(coordinates)
coordinates.insert(0,50)
coordinates=tuple((coordinates))
print(coordinates)


