from sheet import ExcelSheet
from graphics import Window

def __main__():
    # Sheet names to use for now: 'Pal Stats' , 

    FILE_PATH = 'data/Palworld_ Breeding Combinations and Calculator (v1.3-014).xlsx'
    SHEET_NAME = {'stats': 'Pal Stats'}
    
    pal_stats_sheet = ExcelSheet(FILE_PATH, SHEET_NAME['stats'])
    sheet = pal_stats_sheet.load_sheet()
    # print(type(pal_stats_sheet.get_pal_stats('jolthog cryst')))

    win = Window()

    win.create_text_box('howdy',400, 300)

    win._wait_for_close()
    
__main__()





# x = sheet.loc[sheet['#'] == 109]
    # print(x.to_string())