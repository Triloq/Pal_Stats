import pandas as pd


class ExcelSheet:
    def __init__(self, FILE_PATH, SHEET_NAME):
        self.file = pd.ExcelFile(FILE_PATH)
        self.sheet = SHEET_NAME

    def load_sheet(self):
        return self.file.parse(self.sheet, header=1)
        
    def get_pal_stats(self, id = 0, name= ''):
        sheet = self.load_sheet()
        if id != 0:
            # return sheet.loc[sheet[]]
            pass


    def sheet_names(self):
        print(self.file.sheet_names)

    def close_sheet(self):
        self.file.close()