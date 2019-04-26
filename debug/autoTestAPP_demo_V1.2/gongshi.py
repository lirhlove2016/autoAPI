import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write(1, 8, xlwt.Formula('COUNTIF(A3:B3,"PASS"))'))
worksheet.write(2, 8, xlwt.Formula('COUNTIF(A3:B3,"FAIL"))'))
workbook.save(df)