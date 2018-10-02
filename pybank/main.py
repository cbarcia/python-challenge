#pybank main
import os
import csv
k=0
def Bankfunction(delta):
    while (row[2] != ''):
        banktotal=  k +1
        netsum = int(netsum) + int(row[2])
        

# Path to collect data from the folder
bankcsv = os.path.join('budget_data.csv')

# Read in the CSV file
with open(bankcsv, 'r') as csvfile:

 # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        while (row[2]==''):
        print(f'''
        ---------------------------------------------
        Number of transactions: {banktotal}
                  Net Value: {netsum}
        --------- -----------------------------------''')
        print(row)
        Bankfunction(row[2])


        #COUNT TOTAL NUMBER OF MONTHS (ROW 1)
        # TOTAL NET PROFITS
        #AVERAGE CHANGE BETWEEN MONTHS
        #GREATEST INCREASE IN PROFITS (mONTH & VALUE)
        #GREATEST DECREASE IN PROFIT (MONTH AND VALUE)

        #PRINT ANALYSIS TO TERMINAL
        #EXPORT RESULTS TO CSV FILE
