import pandas
from openpyxl import load_workbook

book = load_workbook('Masterfile.xlsx')
writer = pandas.ExcelWriter('Masterfile.xlsx', engine='openpyxl') 
writer.book = book

## ExcelWriter for some reason uses writer.sheets to access the sheet.
## If you leave it empty it will not know that sheet Main is already there
## and will create a new sheet.

writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

data_filtered.to_excel(writer, "Main", cols=['Diff1', 'Diff2'])

writer.save()