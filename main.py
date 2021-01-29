import csv

from Adjacency import Adjacency

file_to_open = "adjacencies.csv"
file_to_save = "newfile.csv"

with open(file_to_open, "r") as my_csv_file:
    my_csv_file = csv.reader(my_csv_file, delimiter=",")
    header = next(my_csv_file)
    adjacencies_list = []

    for line in my_csv_file:
        adjacency = Adjacency(line[0], line[1], line[2], line[3], line[4], line[5])
        adjacencies_list.append(adjacency)

adjacencies_list.sort(key=lambda x: x.priority)

with open(file_to_save, 'w') as new_file:
    write = csv.writer(new_file, delimiter=',')
    write.writerow(header)
    for adjacency in adjacencies_list:
        write.writerow([adjacency.object_Id, adjacency.priority, adjacency.distance, adjacency.tier, adjacency.attempts, adjacency.hosr])
