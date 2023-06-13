from tkinter import Tk, Button


root = Tk()
root.geometry('300x200')
root.title('Тестовый GUI')

btn = Button(
    root,
    text='НАЖМИ МЕНЯ',
    command=lambda: root.title('Нажатие на кнопку мышкой')
)
btn.grid(
    row=0,
    column=0,
    padx=15,
    pady=15,
    sticky='nsew'
)
root.bind_all(
    '<KeyPress-Return>', 
    lambda event: root.title('Нажатие Enter')
)


root.mainloop()
