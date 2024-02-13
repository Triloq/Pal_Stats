from tkinter import *
from sheet import ExcelSheet
from tkinter.ttk import *


class Window(ExcelSheet):
    def __init__(self, FILE_PATH, SHEET_NAME, width=800, height=600):
        self.root = Tk()
        self.root.title('PalDex')
        self.canvas = Canvas(self.root, bg='#acccdb', width=width, height=height)

        self.canvas.pack(fill=BOTH, expand=True)

        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self._close)

        self.width = width
        self.height = height

        self.current_selection = ''

        super().__init__(FILE_PATH, SHEET_NAME)

        self.__setup()
        
    def __update(self):
        self.root.update_idletasks()
        self.root.update()

    def _wait_for_close(self):
        self.running = True
        while self.running:
            self.__update()
    
    def _close(self):
        self.running = False

    def create_text_box(self, text, x, y, font='Helvetica 15', fill='black'):
        self.canvas.create_text(x, y, 
                                text=text, 
                                fill=fill, 
                                font=font, 
                                )

    def __setup(self):
        font_title = 'Helvetica 18 bold'
        self.create_text_box('PalDex', self.width//2, self.height//20, font='Helvetica 18 bold')
        self.create_text_box('Choose Pal:', self.width//8 - 25, self.height//12)
        self.__dropdown(self.width//8 + 100, self.height//12)
        
    
    def __dropdown(self, x, y):
        variable = StringVar(self.root)
        pal_names = self._get_Pal_Names().tolist()
        
        variable.set('Choose --Pal--')
        
        menu = Combobox(
                        self.root, 
                        textvariable=variable, 
                        values=pal_names,
                        width=15,
                        font='Helvetica 12',
                        state='readonly'
                    )
        menu.current(0)
        self.canvas.create_window(x, y, window=menu)
        menu.bind("<<ComboboxSelected>>", self._pal_select_changed)
        
        
        # button = Button( self.root, text='Submit', command=self._pal_chosen(variable))
        # button.grid(column=0, row=6)

    def _pal_select_changed(self, event):
        print(f'Selected: {event.widget.get()}')
        

    
    
        