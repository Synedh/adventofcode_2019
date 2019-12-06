map_data = {}
orbits = open('input').readlines()
for orbit in orbits:
    map_data[orbit[:-1].split(')')[1]] = orbit.split(')')[0]

your_path = [map_data['YOU']]
santa_path = [map_data['SAN']]
while your_path[-1] != 'COM':
    your_path.append(map_data[your_path[-1]])
while santa_path[-1] != 'COM':
    santa_path.append(map_data[santa_path[-1]])

while your_path and santa_path and your_path[-1]==santa_path[-1]:
    your_path.pop(-1)
    santa_path.pop(-1)

print(len(your_path) + len(santa_path))