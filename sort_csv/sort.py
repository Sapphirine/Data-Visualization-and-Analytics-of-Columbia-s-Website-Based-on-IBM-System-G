import sys
import csv

graph_name = sys.argv[1]
position = int(sys.argv[2])
a_de = int(sys.argv[3])
reader_1 = csv.reader(open(graph_name + '_vertex_1.csv', 'rb'))
reader_0 = csv.reader(open(graph_name + '_vertex_0.csv', 'rb'))
t_1 = []
t_2 = []
for i in reader_1:
    t_1.append([i[0], i[position]])
for i in reader_0:
    t_2.append([i[0], i[position]])

final = t_1[1:] + t_2[1:]
if a_de == 1:
    a = sorted(final, key=lambda x: float(x[1]))
else:
    a = sorted(final, key=lambda x: float(x[1]),reverse=True)
t = 0
for i in a:
    if t > 10:
        break
    if float(i[1]) == 0:
        continue
    print i
    t += 1