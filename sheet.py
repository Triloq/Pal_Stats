import pandas as pd
import numpy as np
import string


class ExcelSheet:
    def __init__(self, FILE_PATH, SHEET_NAME):
        self.file = pd.ExcelFile(FILE_PATH)
        self.sheet = SHEET_NAME

    def load_sheet(self):
        # return the sheet in the file which matches the tab name
        return self.file.parse(self.sheet, header=1)
        
    def get_pal_stats(self, id):
        # Loads the current sheet then returns the row attributed to either the pal id or the name of the pal
        sheet = self.load_sheet()
        names = sheet['Name'].values
        names = np.array([x.lower() if isinstance(x, str) else x for x in names])

        if isinstance(id, str):
            if id.lower() not in names:
                raise Exception('Not a known Pal')
            return sheet.loc[sheet['Name'] == string.capwords(id)]
        elif id != 0 and id <= 111:
            return sheet.loc[sheet['#'] == id]
        else:
            raise Exception('Invalid entry')

    


    def sheet_names(self):
        # just looks to see what the names of the different tabs are in the file
        print(self.file.sheet_names)

    def close_sheet(self):
        # maybe unnecessary, here to close if that seems to become necessary
        self.file.close()