# coding:utf-8
import xlrd
import xlwt


class ExcelUtil:
    def __init__(self):
        pass

    @staticmethod
    def dict_data(filename, sheetName="Sheet1"):

        data = xlrd.open_workbook(filename)
        table = data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        keys = table.row_values(0)
        # 获取总行数
        rowNum = table.nrows
        # 获取总列数
        colNum = table.ncols
        if rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(rowNum - 1)):
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i + 1
                # print(s['rowNum'])
                values = table.row_values(j)

                for x in list(range(colNum)):
                    s[keys[x]] = values[x]
                r.append(s)
                j += 1

            return r, keys

    @staticmethod
    def write_excel(filename, datas, names):
        """写入数据"""
        f = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
        n = []
        for i in range(len(names)):
            sheet.write(0, i, names[i])
            n.append(names[i])

        # 写入数据
        d = []
        for i in range(len(datas)):
            value = datas[i]
            # print("正在写入第{0}行，数据{1}".format(i+1,value))
            for j in range(len(names)):
                key = names[j]
                if key == 'Id':
                    strValue = int(value[key])
                else:
                    strValue = str(value[key])
                sheet.write(i + 1, j, strValue)

            d.append(datas[i])
        f.save(filename)
        print ("write finished")


if __name__ == "__main__":
    pass
