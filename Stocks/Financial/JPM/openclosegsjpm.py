import csv
import matplotlib
from matplotlib import style

style.use('ggplot')

f = open('jpm.csv')
csv_f = csv.reader(f)

csv_count = 0
close = []
close2 = []
for row in csv_f:
    csv_count+=1
    close.append(row[4])

close[0] = 0.0;
for each in close:
    a = float(each)
    close2.append(a)

length = len(close2)
diff = 0
for i in range(1, length-1):
    diff += (float(close2[i+1])-float(close2[i]))

av = float(diff/length)

first = close2[length-1]
futureclose = [first]
for i in range(1, 366):
    a = first+ i*av
    futureclose.append(a)
print(futureclose)





