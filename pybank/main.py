#pybank main
import os
import csv

# Path to collect data from the folder
bankcsv = os.path.join('budget_data')

# Read in the CSV file
with open(wrestlingCSV, 'r') as csvfile:

 # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader: