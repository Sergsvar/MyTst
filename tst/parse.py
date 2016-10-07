def parser():
    import xlrd
    from collections import Counter

    rb = xlrd.open_workbook('1212.xls', formatting_info=True)
    sheet = rb.sheet_by_index(0)
    lst = []
    dct = {}
    def getList(key):
        dct = {}
        lst = []
        for i in range(1, sheet.nrows):
            if sheet.cell_value(i,0)==key:
                lst.append(sheet.cell_value(i,1))
                lst.append(sheet.cell_value(i,2))
        dct[key]=lst
        return dct
    for i in range(1,sheet.nrows):
        lst.append(sheet.cell_value(i,0))
    c = dict(Counter(lst))
    for key in c:
        dct.update(getList(key))
    return dct

