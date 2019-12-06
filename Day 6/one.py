map_data = {}
orbits = open('input').readlines()
for orbit in orbits:
    map_data[orbit[:-1].split(')')[1]] = orbit.split(')')[0]
num_orbits = 0
for planete in map_data:
    path = [planete]
    while path[-1] != 'COM':
        path.append(map_data[path[-1]])
    num_orbits += len(path) - 1
print(num_orbits)