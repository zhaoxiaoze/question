import xlrd
import xlwt




data = xlrd.open_workbook('questionandanswer.xlsx')

sheet_names = data.sheet_names()

print(sheet_names)


for sheet in sheet_names:
        # 获取sheet
    table = data.sheet_by_name(sheet)
        # 获取总行数
    nrows = table.nrows  # 包括标题
        # 获取总列数
    ncols = table.ncols

print(nrows)
print(ncols)



def read_excel(filename, sheetname):

    new_workbook = xlwt.Workbook()
    new_sheet = new_workbook.add_sheet('question')
    rbook = xlrd.open_workbook(filename)
    sheet = rbook.sheet_by_name(sheetname)
    rows = sheet.nrows
    cols = sheet.ncols
    all_content = []
    for i in range(rows):
        row_content = []
        for j in range(cols):
            cell = sheet.cell_value(i, j)
            row_content.append(cell)
        all_content.append(row_content)

    print(all_content)

    return all_content




if __name__ == '__main__':

    filename = 'questionandanswer.xls'
    sheetname = 'questionandanswer'
    result = read_excel(filename, sheetname)

    new_workbook = xlwt.Workbook()
    new_sheet = new_workbook.add_sheet('questionandanswer')
    for i in range(ncols):
        new_sheet.write(i, 0, result[i])

    new_workbook.save(r"questionandanswer.xls")
    print(result)

