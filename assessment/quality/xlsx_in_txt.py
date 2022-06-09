from openpyxl import load_workbook


def read_data():
    wb = load_workbook('popisyat.xlsx')
    sheet = wb['Лист1']

    list_text = []
    for i in range(1, sheet.max_row + 1):
        list_text.append(sheet.cell(row=i, column=1).value)
    return list_text
