import os
import xlrd2
import xlsxwriter
import glob
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from openpyxl.styles import Side, Border
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter
class MakeExcel():
    biao_tou_total1_1 = "NULL"
    biao_tou_total1_2 = "NULL"
    biao_tou_total2_1 = "NULL"
    biao_tou_total2_2 = "NULL"
    biao_tou_total3_1 = "NULL"
    biao_tou_total3_2 = "NULL"
    wei_zhi = "NULL"
    # 保存第一个sheet数据
    all_data1 = []
    # 保存第二个sheet数据
    all_data2 = []
    # 保存第三个sheet数据
    all_data3 = []

    # 用于保存合并的所有行的数据
    # 获取要合并的所有exce表格
    def get_exce(self, filepath):
        # wei_zhi = input("请输入Excel文件所在的目录：")
        self.wei_zhi = (filepath)
        all_exce = glob.glob(self.wei_zhi + "*.xlsx")
        print("该目录下有" + str(len(all_exce)) + "个excel文件：")
        if (len(all_exce) == 0):
            return 0
        else:
            for i in range(len(all_exce)):
                print(all_exce[i])
            return all_exce

    # 打开Exce文件
    def open_exce(self, name):
        fh = xlrd2.open_workbook(name)
        return fh

    # 获取exce文件下的所有sheet名
    def get_sheet(self, fh):
        sheets = fh.sheets()
        #print(sheets)
        return sheets

    # 获取sheet下有多少行数据
    def get_sheetrow_num(self, sheet):
        return sheet.nrows

    # 获取sheet下的数据
    def get_sheet_data(self, sheet, row):
        for i in range(row):
            if (i == 0):
                self.biao_tou_total1_1 = sheet.row_values(i)
                continue
            if (i == 1):
                self.biao_tou_total1_2 = sheet.row_values(i)
                continue
            values = sheet.row_values(i)
            # print(values)
            self.all_data1.append(values)

        return self.all_data1

    def get_sheet_data2(self, sheet, row):
        for i in range(row):
            if (i == 0):
                self.biao_tou_total2_1 = sheet.row_values(i)
                continue
            if (i == 1):
                self.biao_tou_total2_2 = sheet.row_values(i)
                continue

            values = sheet.row_values(i)
            # print(values)
            self.all_data2.append(values)

        return self.all_data2

    def get_sheet_data3(self, sheet, row):
        for i in range(row):
            if (i == 0):
                self.biao_tou_total3_1 = sheet.row_values(i)
                continue
            if (i == 1):
                self.biao_tou_total3_2 = sheet.row_values(i)
                continue

            values = sheet.row_values(i)
            # print(values)
            self.all_data3.append(values)

        return self.all_data3

    def startwork(self, filepath):
        all_exce = self.get_exce(filepath)
        # 得到要合并的所有exce表格数据
        if (all_exce == 0):
            print("该目录下无.xlsx文件！请检查您输入的目录是否有误！")
            os.system('pause')
            exit()

        # 下面开始文件数据的获取
        for exce in all_exce:
            fh = self.open_exce(exce)
            # 打开文件
            sheets = self.get_sheet(fh)
            print(sheets)
            # 获取文件下的sheet数量

            for sheet in range(len(sheets)):
                # print(sheet)
                row = self.get_sheetrow_num(sheets[sheet])
                # print(row)
                # 获取一个sheet下的所有的数据的行数
                while sheet == 0:
                    sheet1 = self.get_sheet_data(sheets[sheet], row)
                    break
                while sheet == 1:
                    sheet2 = self.get_sheet_data2(sheets[sheet], row)
                    break
                while sheet == 2:
                    sheet3 = self.get_sheet_data3(sheets[sheet], row)
                    break
                # 获取一个sheet下的所有行的数据

        self.all_data1.insert(0, self.biao_tou_total1_2)
        self.all_data1.insert(0, self.biao_tou_total1_1)
        self.all_data2.insert(0, self.biao_tou_total2_2)
        self.all_data2.insert(0, self.biao_tou_total2_1)
        self.all_data3.insert(0, self.biao_tou_total3_2)
        self.all_data3.insert(0, self.biao_tou_total3_1)
        # 表头写入


        # 下面开始文件数据的写入
        new_exce = self.wei_zhi + "评分汇总.xlsx"
        # 新建的exce文件名字

        fh1 = xlsxwriter.Workbook(new_exce)
        # 新建一个exce表

        new_sheet1 = fh1.add_worksheet()
        new_sheet2 = fh1.add_worksheet()
        new_sheet3 = fh1.add_worksheet()
        # 新建一个sheet表
        # 写入sheet表数据
        for i in range(len(self.all_data1)):
            for j in range(len(self.all_data1[i])):
                c = self.all_data1[i][j]
                new_sheet1.write(i, j, c)

        for i in range(len(self.all_data2)):
            for j in range(len(self.all_data2[i])):
                c = self.all_data2[i][j]
                new_sheet2.write(i, j, c)

        for i in range(len(self.all_data3)):
            for j in range(len(self.all_data3[i])):
                c = self.all_data3[i][j]
                new_sheet3.write(i, j, c)

        fh1.close()
        # 关闭该exce表

        print("文件合并成功,请查看“" + self.wei_zhi + "”目录下的总数据.xlsx文件！")

        workbook = load_workbook(filename=self.wei_zhi + '评分汇总.xlsx')
        font = Font(name='宋体', size=18, bold=True)
        # sheetnames = workbook.sheetnames
        # mo_sheet = workbook[sheetnames[0]]
        # mo_sheet['A1'].font = font


        #修改边框
        border = Border(left=Side(border_style='thin'),
                        right=Side(border_style='thin'),
                        top=Side(border_style='thin'),
                        bottom=Side(border_style='thin'))
        alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        for ws in workbook:
            for row in ws.rows:
                for cell in row:
                    # 如果单元格有数据，则为它添加边框
                    if cell.value or cell.value == 0:
                        cell.border = border
                        cell.alignment = alignment

        mo_sheet_one = workbook['Sheet1']
        mo_sheet_one.title = '总成绩'
        mo_sheet_two = workbook['Sheet2']
        mo_sheet_two.title = '第一题'
        mo_sheet_three = workbook['Sheet3']
        mo_sheet_three.title = '第二题'
        #设置指定列宽

        #获取表1总列数
        column_count = mo_sheet_one.max_column

        #字母自增
        # _chr = 'A'
        # if _chr == 'Z':
        #     print('A')
        # else:
        #     print(chr(ord(_chr) + 1))
        #对表1进行列宽设置
        _chr = 'A'
        for i in range(column_count):

            if i == 0:
                mo_sheet_one.column_dimensions[chr(ord(_chr))].width = 5
                _chr = chr(ord(_chr) + 1)
                continue
            if i == 1:
                mo_sheet_one.column_dimensions[chr(ord(_chr))].width = 10
                _chr = chr(ord(_chr) + 1)
                continue
            else:
                # print(chr(ord(_chr)))
                mo_sheet_one.column_dimensions[chr(ord(_chr))].width = 20
                _chr = chr(ord(_chr) + 1)

        #对表2进行列宽设置
        _chr = 'A'
        #获取表2总列数
        column_count2 = mo_sheet_two.max_column
        for i in range(column_count2):

            if i == 0:
                mo_sheet_two.column_dimensions[chr(ord(_chr))].width = 5
                _chr = chr(ord(_chr) + 1)
                continue
            if i == 1:
                mo_sheet_two.column_dimensions[chr(ord(_chr))].width = 10
                _chr = chr(ord(_chr) + 1)
                continue
            else:
                # print(chr(ord(_chr)))
                mo_sheet_two.column_dimensions[chr(ord(_chr))].width = 20
                _chr = chr(ord(_chr) + 1)

        #对表3进行列宽设置
        _chr = 'A'
        #获取表3总列数
        column_count3 = mo_sheet_three.max_column
        for i in range(column_count3):

            if i == 0:
                mo_sheet_three.column_dimensions[chr(ord(_chr))].width = 5
                _chr = chr(ord(_chr) + 1)
                continue
            if i == 1:
                mo_sheet_three.column_dimensions[chr(ord(_chr))].width = 10
                _chr = chr(ord(_chr) + 1)
                continue
            else:
                # print(chr(ord(_chr)))
                mo_sheet_three.column_dimensions[chr(ord(_chr))].width = 20
                _chr = chr(ord(_chr) + 1)


        #合并表1单元格
        mo_sheet_one.merge_cells(start_row=1, start_column=3, end_row=1, end_column=4)
        mo_sheet_one.merge_cells(start_row=1, start_column=1, end_row=2, end_column=1)
        mo_sheet_one.merge_cells(start_row=1, start_column=2, end_row=2, end_column=2)

        # 合并表2单元格
        mo_sheet_two.merge_cells(start_row=1, start_column=1, end_row=2, end_column=1)
        mo_sheet_two.merge_cells(start_row=1, start_column=2, end_row=2, end_column=2)
        row_values = []
        init_value = []
        row_num = 0
        increase_num = 0
        for row in mo_sheet_two.iter_rows(min_col=1, max_col=mo_sheet_two.max_column, max_row=1):
            # row_values.append([cell.value for cell in row])
            for cell in row:
                if cell.value == '总分':
                    init_value.append(increase_num)
                elif cell.value != None:
                    increase_num += 1
                    row_num += 1
                elif cell.value == None:
                    increase_num += 1
                    if row_num not in init_value:
                        init_value.append(row_num)

        mo_sheet_two.merge_cells(start_row=1, start_column=init_value[0], end_row=1, end_column=init_value[1])
        # 合并表3单元格
        mo_sheet_three.merge_cells(start_row=1, start_column=1, end_row=2, end_column=1)
        mo_sheet_three.merge_cells(start_row=1, start_column=2, end_row=2, end_column=2)
        row_values = []
        init_value = []
        row_num = 0
        increase_num = 0
        for row in mo_sheet_three.iter_rows(min_col=1, max_col=mo_sheet_three.max_column, max_row=1):
            # row_values.append([cell.value for cell in row])
            for cell in row:
                if cell.value == '总分':
                    init_value.append(increase_num)
                elif cell.value != None:
                    increase_num += 1
                    row_num += 1
                elif cell.value == None:
                    increase_num += 1
                    if row_num not in init_value:
                        init_value.append(row_num)

        mo_sheet_three.merge_cells(start_row=1, start_column=init_value[0], end_row=1, end_column=init_value[1])

        #对序号排序
        for i in range(3, mo_sheet_one.max_row + 1):
            mo_sheet_one.cell(row=i, column=1).value = i-2
        for i in range(3, mo_sheet_two.max_row + 1):
            mo_sheet_two.cell(row=i, column=1).value = i-2
        for i in range(3, mo_sheet_three.max_row + 1):
            mo_sheet_three.cell(row=i, column=1).value = i-2

        #设置行高
        for row in range(1,mo_sheet_one.max_row + 1):
            mo_sheet_one.row_dimensions[row].height = 30
        for row in range(1,mo_sheet_two.max_row + 1):
            if row == 2:
                mo_sheet_two.row_dimensions[row].height = 55
            else:
                mo_sheet_two.row_dimensions[row].height = 30
        for row in range(1,mo_sheet_three.max_row + 1):
            if row == 2:
                mo_sheet_three.row_dimensions[row].height = 55
            else:
                mo_sheet_three.row_dimensions[row].height = 30

        workbook.save(self.wei_zhi + '评分汇总.xlsx')