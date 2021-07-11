f = open('myfile.csv')

f = open(r'C:\Python33\Scripts\myfile.csv')

# Write to a csv file
import csv

with open('myfile.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Bob', '25', 'Manager', 'Seattle'])
    writer.writerow(['Sam', '30', 'Developer', 'New York'])

# Read a csv file into a dict
import csv

with open('myfile.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# Prints:
# {'job': 'Manager', 'city': 'Seattle', 'age': '25', 'name': 'Bob'}
# {'job': 'Developer', 'city': 'New York', 'age': '30', 'name': 'Sam'}

import csv

with open('myfile.csv') as f:
    keys = ['name', 'age', 'job', 'city']
    reader = csv.DictReader(f, fieldnames=keys)
    for row in reader:
        print(row)

# Prints:
# {'job': 'Manager', 'city': 'Seattle', 'age': '25', 'name': 'Bob'}
# {'job': 'Developer', 'city': 'New York', 'age': '30', 'name': 'Sam'}

# Write csv from dictionary
import csv

with open('myfile.csv', mode='w') as f:
    keys = ['name', 'age', 'job', 'city']
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()    # add column names in the CSV file
    writer.writerow({'job': 'Manager', 'city': 'Seattle', 'age': '25', 'name': 'Bob'})
    writer.writerow({'job': 'Developer', 'city': 'New York', 'age': '30', 'name': 'Sam'})

# Different Dimlimiter
# Write a file with different delimiter '|'
import csv

with open('myfile.csv', mode='w') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerow(['Bob', '25', 'Manager', 'Seattle'])
    writer.writerow(['Sam', '30', 'Developer', 'New York'])

# Read a file with different delimiter '|'
import csv

with open('myfile.csv') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        print(row)

# Prints:
# ['Bob', '25', 'Manager', 'Seattle']
# ['Sam', '30', 'Developer', 'New York']

# Handle comma within data
import csv

with open('myfile.csv', mode='w') as f:
    writer = csv.writer(f, quotechar='"')
    writer.writerow(['Bob', '25', '113 Cherry St, Seattle, WA 98104, USA'])
    writer.writerow(['Sam', '30', '150 Greene St, New York, NY 10012, USA'])

import csv

with open('myfile.csv') as f:
    reader = csv.reader(f, quotechar='"')
    for row in reader:
        print(row)

# Prints:
# ['Bob', '25', '113 Cherry St, Seattle, WA 98104, USA']
# ['Sam', '30', '150 Greene St, New York, NY 10012, USA']

# Catch and handle errors
import csv, sys
filename = 'myfile.csv'
with open(filename, newline='') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))