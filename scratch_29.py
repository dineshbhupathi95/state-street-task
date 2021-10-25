import pandas as pd

def excel_data(file,sheet_name):
    file = pd.read_excel(file,sheet_name=sheet_name)
    df = pd.DataFrame(file)
    s = df.to_numpy()
    l = [y for x in s for y in x if str(y)!='nan']
    return l
print(excel_data("C:/Users/bupat/Downloads/SheetWithMultiTables.xlsx","Data"))