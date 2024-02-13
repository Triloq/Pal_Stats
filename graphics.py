from tkinter import *


class Window:
    def __init__(self, width=800, height=600):
        self.root = Tk()
        self.root.title('PalDex')
        self.canvas = Canvas(self.root, bg='#acccdb', width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self._close)

    def __update(self):
        self.root.update_idletasks()
        self.root.update()

    def _wait_for_close(self):
        self.running = True
        while self.running:
            self.__update()
    
    def _close(self):
        self.running = False

    def create_text_box(self, text, x, y):
        self.canvas.create_text(x, y, text=text, fill='black', font='Helvetica 15')
        # self.canvas.pack()

    def create_entry_box(self):
        pass

    def _populate_stats_text(self):
        pass