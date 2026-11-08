import csv
import math

file_path = 'data/experimentData.CSV'

with open(file_path, 'r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)
    rows = list(reader)


if 'SphereDensity' in header:
    density_index = header.index('SphereDensity')

else:
    density_index = len(header)
    header.append('SphereDensity')

for row in rows:

    Mass = float(row[2])
    Radius = float(row[3])
    velocity = float(row[1])
    Volume = (4/3) * math.pi * Radius**3
    radius = float()

    D = Mass / Volume

    if len(row) > density_index:
        row[density_index] = D
    else:
        row.append(D)

with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)


    



        

    

    

    