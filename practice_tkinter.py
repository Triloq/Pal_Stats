from tkinter import *

root = Tk()
root.title('PalDex')
canvas = Canvas(root, bg='#acccdb', width=800, height=600)

canvas.create_text(400, 100, text="Pal Stats", fill='black', )
canvas.pack()

root.mainloop()