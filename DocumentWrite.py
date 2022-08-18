#this is a test code that reads from csv file and fills the template from the csv values

from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
import csv

template = "SHIPPING_INSTRUCTION_TEMPLATE.docx"
document = MailMerge(template)

print(document.get_merge_fields())

with open("test.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    
    for row in csv_reader:
        if line_count==0:
            print(f'Column names are {", ".join(row)}')
            line_count+=1
        else:
            values=row
            line_count+=1
            document.merge(
                Destination='smg',
                consignee=values[2],
                Notes=values[6],
                Loading=values[4],
                Goods=values[0],
                Shipper=values[1],
                Contract='xxxx',
                Date='today',    
                Shipment='Mr. Jones')

            document.write('testoutput.docx')
            break

