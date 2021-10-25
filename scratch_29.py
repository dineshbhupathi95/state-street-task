import pandas as pd
def excel_data(file,sheet_name):
    file = pd.read_excel(file,sheet_name=sheet_name)
    df = pd.DataFrame(file)
    s = df.to_numpy()
    lst_data = [y for x in s for y in x if str(y)!='nan']
    data = pd.DataFrame(data=lst_data)
    return data
print(excel_data("/home/dinesh/Downloads/SheetWithMultiTables.xlsx","Data"))


# import pandas as pd
# xl = pd.ExcelFile('C:/Users/bupat/Downloads/SheetWithMultiTables.xlsx')
# # df = pd.read_excel(xl, 'Data')
#     # print(df)
# # print(xl.sheet_names)
# nrows = xl.book.sheet_by_name('Data').nrows
# df1 = xl.parse(0, skip_footer= nrows-(10+1)).dropna(axis=1, how='all')
# df2 = xl.parse(0, skip_footer=12).dropna(axis=1, how='all')
# print(df1
#       )
# print(df2)
