#pybank main
import os
import csv
import pandas as pd


k=0
i=0
netsum=0
rho = []
beta = [0,0]
delta = []
gamma = []
def Bankfunction(delta):
    if (row[2] != ''):
        k =  k +1
        banktotal = k
        netsum = 0
        old = "hello"
        new = "hello"
        chg = 0
        high = 0
        low = 0
        return 
# Path to collect data from the folder
bankcsv = os.path.join('budget_data.csv')

# Read in the CSV file
with open(bankcsv, 'r') as csvfile:

 # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvfile)

    # Loop through the data
    for row in csvreader:
        
        rho = row[:]
        beta[:] = rho[:]+beta[:]
        gamma[:]= rho[:]+gamma[:]
        gamma.pop(0)
        high = max(gamma)
        low = min(gamma)
               
                #beta.append(rho)
        #del beta[0]
        
        chg = int(beta[3])-int(beta[1])

        delta.append(chg)
        avgchg = sum(delta)/len(delta)
        k =  k +1
        banktotal = k
        #netsum = sum(gamma)

        
        
        
    print(f'''
        ---------------------------------------------
        Number of transactions: {banktotal}
                     Net Value: {netsum}
                Average Change: {avgchg}
                Maximum Profit: {high}
                  Biggest Loss: {low}

        --------- -----------------------------------''')
exportfiledf = pd.DataFrame(
    {"Number of Transactions": [banktotal],
     "Net Value": [netsum],
     "Average Change": [avgchg],
     "Maximum Profit": [high],
     "Biggest Loss": [low]
     })
writer = pd.ExcelWriter('output.xlsx')
exportfiledf.to_excel(writer,'sheet1')
writer.save()


    
            
        


        #COUNT TOTAL NUMBER OF MONTHS (ROW 1)
        # TOTAL NET PROFITS
        #AVERAGE CHANGE BETWEEN MONTHS
        #GREATEST INCREASE IN PROFITS (mONTH & VALUE)
        #GREATEST DECREASE IN PROFIT (MONTH AND VALUE)

        #PRINT ANALYSIS TO TERMINAL
        #EXPORT RESULTS TO CSV FILE
