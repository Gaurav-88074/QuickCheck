# Writing to an excel
# sheet using Python
import xlwt
from xlwt import Workbook
# with open('output.csv', 'w', newline='\n', encoding='utf-8') as f:

## Python program to demonstrate
# writing to CSV


import csv
	
# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
	
# data rows of csv file
rows = [ ['Nikhil', 'COE', '2', '9.0'],
		['Sanchit', 'COE', '2', '9.1'],
		['Aditya', 'IT', '2', '9.3'],
		['Sagar', 'SE', '1', '9.5'],
		['Prateek', 'MCE', '3', '7.8'],
		['Sahil', 'EP', '2', '9.1']]
	
# name of csv file
filename = "university_records1.csv"
	
# writing to csv file
with open(filename, 'w',newline='\n') as csvfile:
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)
		
	# writing the fields
	csvwriter.writerow(fields)
		
	# writing the data rows
	csvwriter.writerows(rows)
