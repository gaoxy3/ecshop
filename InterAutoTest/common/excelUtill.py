#1、导入包
import xlrd
# #2、创建workbook对象
# book = xlrd.open_workbook("../data/接口测试用例.xlsx")
# #3、获取要打开的sheet文件
# sheet = book.sheet_by_index(1)#通过索引
# # sheet = book.sheet_by_name("test")
# #4、获取行数和列数
# rows = sheet.nrows
# cols = sheet.ncols
# print(rows,cols)
# #5、获取每行的数据
# for i in range(rows):
#     print(sheet.row_values(i))
# #6、获取每列的数据
# for i in range(cols):
#     print(sheet.col_values(i))

class ExcelUtill():
    def __init__(self,src,index=0):
        self.book = xlrd.open_workbook(src)
        self.sheet = self.book.sheet_by_index(index)
    def getRows(self):
        return self.sheet.nrows
    def getCols(self):
        return self.sheet.ncols
    def getDatas(self,l):
        d = []
        for i in range(1,self.getRows()):
            v = self.sheet.row_values(i)
            if len(l)==1:
                d.append(v[l[0]])
            else:
                t = []
                for j in l:
                    t.append(v[j])
                d.append(tuple(t))
        return d

if __name__ == '__main__':
    print(ExcelUtill("../data/接口测试用例.xlsx",2).getDatas([3]))
