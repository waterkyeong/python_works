from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path('H/ch16/weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# dates=[]
# highs=[]
# avgs=[]
# for row in reader:
#     current_date = datetime.strptime(row[2], '%Y-%m-%d')
#     dates.append(current_date)
#     high = int(row[4])
#     # avg = int(row[3]) #p.460 결측치
#     highs.append(high)
#     # avgs.append(avg)
# print(highs)
# # print(avgs)
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.plot(dates,highs,color='red')
# ax.plot(dates,lows,color='blue')
# ax.set_title('high temperature', fontsize=24)
# ax.set_xlabel('time',fontsize = 10)
# ax.set_ylabel('temperature',fontsize = 10)
# ax.tick_params(labelsize=8)
# plt.show()


for index,column_header in enumerate(header_row):
    print(index,header_row)

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
