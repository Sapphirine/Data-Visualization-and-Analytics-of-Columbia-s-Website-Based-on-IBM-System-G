import csv
import sys

input_file_name = sys.argv[1]

original = csv.reader(open(input_file_name + '.csv', 'rb'))
node_1 = csv.writer(open(input_file_name + '_node_1.csv', 'wb'))
node_2 = csv.writer(open(input_file_name + '_node_2.csv', 'wb'))
edge = csv.writer(open(input_file_name + '_edge.csv', 'wb'))
url_1 = {}
url_2 = {}
node_1.writerow(['url', 'title'])
node_2.writerow(['url', 'title'])
edge.writerow(['source', 'target'])

t = 0

for i in original:
    t+=1
    if i[0] == 'url' or len(i) < 4:
        continue
    if url_1.get(i[0]) is None:
        node_1.writerow([i[0], i[3].split(',')[0]])
        url_1[i[0]] = 1
    if url_2.get(i[2]) is None:
        node_2.writerow([i[2], i[1].split(',')[0]])
        url_1[i[2]] = 1
    edge.writerow([i[0], i[2]])

print t
