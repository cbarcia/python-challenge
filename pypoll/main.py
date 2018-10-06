#main pypoll
import os
import csv
import pandas as pd

file_one = ('election_data.csv')
file_df = pd.read_csv(file_one)

# Import the books.csv file as a DataFrame
countdf = file_df.count()
uniquedf = file_df.drop_duplicates(subset='Candidate')
#uniquedf.head(5)
votedf = file_df.groupby('Candidate')
votecountdf = votedf.count()
totalvotes = []
totalvotes = votecountdf
votesplit = []
votesplit = votecountdf['County']


total = votecountdf['County'].sum()
tot = [total,total,total,total]
new = []
new = votesplit[:]/ tot[:]
print(f'''
        ---------------------------------------------
        Election Results
        {totalvotes[:]}
        Election Percent Splits
        {new[:]}
        
        --------- -----------------------------------''')

#exportfiledf = pd.DataFrame(
   # { [totalvotes[:]]
   # [new[:]]
    # })
#writer = pd.ExcelWriter('output.xlsx')
#exportfiledf.to_excel(writer,'sheet1')
#writer.save()