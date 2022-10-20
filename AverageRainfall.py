#Tim Koklic
years = int(input('Number of years: '))
while years < 1:
    years = int(input('Invalid: Enter a positive number: '))
print('*************************')
total = 0
for year in range(1,years+1):
    for month in range(1,13):
        monthly_rainfall = float(input(f'Enter the rainfall for year {year}, month {month}: '))
        total += monthly_rainfall
average = total/(years*12)
print(f'Number of months: {years*12}, Total rainfall in inches: {total:.2f} , Average rainfall: {average:.2f}')
