import csv
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt
import matplotlib.dates as mdates

style.use('ggplot')

f = open('apa.csv')
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

days = []
first = close2[length-1]
futureclose = [first]
for i in range(1, 366):
    a = first+ i*av
    futureclose.append(a)
for i in range(1, 366):
    days.append(i)

dates = ['01/01/2017','12/31/2017']
x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
y = futureclose[len(futureclose)-1]

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x,y)
plt.savefig('apa.svg')



