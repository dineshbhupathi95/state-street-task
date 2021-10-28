import pandas as pd
import numpy as np
from skimage.measure import label, regionprops

def parse_excel_multiple_data(file,sheetname):
    file = pd.read_excel(file, sheet_name=sheetname)
    df = pd.DataFrame(file)
    # df1 = df.iloc[0:3,0:3]
    # df2 = df.iloc[4:8,6:9]
    # print(df1)
    # print(df2)
    binary_rep = np.array(df.notnull().astype('int'))
    list_of_dataframes = []
    l = label(binary_rep)
    for s in regionprops(l):
        df1=df.iloc[s.bbox[0]:s.bbox[2],s.bbox[1]:s.bbox[3]]
        # values_to_numpy = df1.to_numpy()
        list_of_dataframes.append(df1)
    for each_data_frame in list_of_dataframes:
        print(each_data_frame)
    # print(list_of_dataframes)
print(parse_excel_multiple_data("/home/dinesh/Downloads/SheetWithMultiTables.xlsx","Data"))



# # s = (1,2,3)
# # d = (3,4,5)
# # a = lambda x,y: x+y
# # print(a)
#
# #'abc'
# # abc,bac,bca,cab,cba.acb
# #in:scratch
# #in: ratchsc
# s = 'scratch'
# s1= 'rcthsca'
# s2='ratchsc'
# # for
# if s[:2] == s2[-2:]:
#     print('rota'

# import pandas as pd
# def excel_data(file,sheet_name):
#     file = pd.read_excel(file,sheet_name=sheet_name)
#     df = pd.DataFrame(file)
#     s = df.to_numpy()
#     lst_data = [y for x in s for y in x if str(y)!='nan']
#     data = pd.DataFrame(data=lst_data)
#     return data
# print(excel_data("/home/dinesh/Downloads/SheetWithMultiTables.xlsx","Data"))


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
