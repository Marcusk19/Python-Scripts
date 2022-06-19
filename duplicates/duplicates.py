import sys
import csv
# routenumb StreetName, MPLength, BeginMP1, EndMp1, RouteName

file_path = sys.argv[1]
# print("Operating on " + str(file_path))


values = dict()
individual_rows = []
with open(file_path, mode='r') as file:
    csvFile = csv.DictReader(file, delimiter=',')
    columnNames = csvFile.fieldnames
    # dictFromCSV = dict(list(csvFile)[0])
    # columnNames = list(dictFromCSV.keys())
    print(columnNames)

    row_index = 0
    for row in csvFile:
        id = row['FID_Divisi']
        print(id)

        if id not in values:
            values[id] = row_index
            individual_rows.append(row)
        row_index += 1

    print(individual_rows)

with open(str(file_path)[:len(str(file_path))-4] + "_new.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, columnNames)
    writer.writeheader()
    writer.writerows(individual_rows)

            

