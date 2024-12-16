import csv
from datetime import datetime
from matplotlib import pyplot as plt

#Read the filename path
filename = '../csd325/module-4/sitka_weather_2018_simple.csv'

# Get dates and high temperatures from this file.
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)

# Get dates and low temperatures from this file.
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, lows = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        low = int(row[6])
        lows.append(low)
    


while True:
    entry = input("Please enter High to see high temperature, Low to see low temperature, or Exit for exit out: ")

    if entry.lower() == 'high':
        # Plot the high temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif entry.lower() == 'low':
        # Plot the low temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        # Format plot.
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif entry.lower() == 'exit':
        print('You have successfully exit the program.')
        break

    else:
        print('Please follow the instruction.')