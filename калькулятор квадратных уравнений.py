import math
import tkinter as tk
from tkinter import font, messagebox

# характеристика окна и переменные
flag = 0
bonus = 10
win = tk.Tk()
win.title('QEcalculate')
win.geometry(('500x600'))
canvas = tk.Canvas(win, width=400, height=500, bg='white')
canvas.place(x=50, y=50)
answfont = font.Font(family='Times New Romans', size=10)


# Основная расчитывающая функция
def calc(yrav=None, symb='='):
    # проверка является ли уравнение полным
    print(yrav)
    koef = list(map(lambda x: x.lstrip('+'), yrav.split('x')))
    print(koef)
    if len(koef) != 1:
        if (yrav[-1] == 'x' or 2 < yrav.count('x') < 2):
            messagebox.showerror('Ошибка 3', 'не полное уравнение')
            return


    # проверка на допустимые символы и пустоту
    try:
        koef = [1 if koef[i] == '' else koef[i] for i in range(3)]
        print(koef)
    except IndexError:
        if len(koef) == 1:
            messagebox.showerror('Ошибка 1', 'Ты ничего не ввел или недопустимые символы')
    koef = [-1 if koef[i] == '-' else koef[i] for i in range(3)]
    # Расчет Дискрименанта, проверка на наличие корней, проверка на праивильность символов
    try:
        d = (int(koef[1]) ** 2) - (4 * int(koef[0]) * int(koef[2]))
    except ValueError:
        messagebox.showerror('Ошибка 2', 'Недопустимые символы')
    if int(d) < 0:
        canvas.create_text(5, 30, text=f'{vvod.get()} {symb} 0', \
                           justify=tk.LEFT, anchor='w')
        canvas.create_text(5, 50, text=f'Дискриминант отрицательный {d}, корней нет', justify=tk.LEFT, \
                           anchor='w')
        return
    else:
        x1 = (-int(koef[1]) - math.sqrt(d)) / (2 * int(koef[0]))
        x2 = (-int(koef[1]) + math.sqrt(d)) / (2 * int(koef[0]))

    # меняет местами значения переменных, чтобы первым шло число с большим значением
    if x1 > x2:
        x1, x2 = x2, x1
    # Создает краткую запись и координатную прямую
    canvas.create_line((0, 270, 390, 270))
    canvas.create_line((390, 270, 370, 250))
    canvas.create_line((390, 270, 370, 300))
    canvas.create_text(120, 285, text=round(x1, 1))
    canvas.create_text(217, 285, text=round(x2, 1))
    canvas.create_text(5, 50, text=f'D = ({koef[1]})^2 - 4*{koef[0]}*{koef[2]} = √{d}', justify=tk.LEFT, anchor='w')
    canvas.create_text(5, 30, text=f'{vvod.get()} {symb} 0', justify=tk.LEFT, anchor='w')
    canvas.create_text(5, 75, text=f'x1 = -({koef[1]}) - √{d} = {x1}', anchor='w', justify=tk.LEFT)
    if len(str(x1)[1:]) > 3:
        canvas.create_line(15 + bonus, 84, 80 + bonus, 84)
    else:
        canvas.create_line(30, 84, 80, 84)
    canvas.create_text(45, 90, text=f'2 * {koef[0]}', justify=tk.LEFT, anchor='w')
    canvas.create_text(5, 110, text=f'x2 = -({koef[1]}) + √{d} = {x2}', anchor='w', justify=tk.LEFT)
    if len(str(x1)[1:]) > 3:
        canvas.create_line(15 + bonus, 120, 80 + bonus, 120)
    else:
        canvas.create_line(30, 120, 80, 120)
    canvas.create_text(45, 130, text=f'2 * {koef[0]}', justify=tk.LEFT, anchor='w')
    # рисует параболу в соответствии с выбором пользователя и рисует точки на плоскости
    oval = canvas.create_oval((140, 170, 200, 370), outline='black')
    if symb == '>' or symb == '<':
        canvas.create_oval(137, 265, 147, 275, fill='white', outline='black')
        canvas.create_oval(193, 265, 203, 275, fill='white', outline='black')
    elif symb == '>=' or symb == '<=':
        canvas.create_oval(137, 265, 147, 275, fill='black', outline='black')
        canvas.create_oval(193, 265, 203, 275, fill='black', outline='black')
    if int(koef[0]) < 0:
        canvas.move(oval, 0, 40)
        canvas.create_rectangle(140, 320, 200, 470, fill='white', outline='white')
        canvas.create_line(170, 230, 170, 250)
        canvas.create_line(160, 240, 180, 240)
        canvas.create_line(50, 300, 60, 300)
        canvas.create_line(270, 300, 280, 300)
        if symb == '>':
            answer = f'x ∈({round(x1, 1)};{round(x2, 1)})'
        elif symb == '<':
            answer = f'x ∈(+∞;{round(x1, 1)})⋃({round(x2, 1)};-∞)'
        elif symb == '<=':
            answer = f'x ∈(+∞;{round(x1, 1)}]⋃[{round(x2, 1)};-∞)'
        elif symb == '>=':
            answer = f'x ∈[{round(x1, 1)};{round(x2, 1)}]'
        else:
            answer = f'{round(x1, 1)};{round(x2, 1)}'
    else:
        canvas.move(oval, 0, -40)
        canvas.create_rectangle(140, 120, 200, 210, fill='white', outline='white')
        canvas.create_line(160, 300, 180, 300)
        canvas.create_line(60, 240, 60, 260)
        canvas.create_line(50, 250, 70, 250)
        canvas.create_line(260, 240, 260, 260)
        canvas.create_line(250, 250, 270, 250)
        if symb == '>':
            answer = f'x ∈(+∞;{round(x1, 1)})⋃({round(x2, 1)};-∞)'
        elif symb == '<':
            answer = f'x ∈({round(x1, 1)};{round(x2, 1)})'
        elif symb == '<=':
            answer = f'x ∈[{round(x1, 1)};{round(x2, 1)}]'
        elif symb == '>=':
            answer = f'x ∈(-∞;{round(x1, 1)}]⋃[{round(x2, 1)};+∞)'
        else:
            answer = f'{round(x1, 1)};{round(x2, 1)}'
    # пишет ответ
    canvas.create_text(5, 400, text=f'Ответ: {answer}', justify=tk.LEFT, anchor='w', font=answfont)


# Функция получения значения через кнопку "решить" и удаления холста \
# после повторного нажатия
def get(symb='='):
    canvas.delete('all')
    calc(vvod.get().lower(), symb)
    vvod['state'] = 'normal'
    vvod.delete(0, tk.END)
    vvod['state'] = 'disabled'


# получает символ который пользователь выбрал если тот хочет решить неравенство
def nerav(symb):
    get(symb)


# функция ввода значения через клавиатуру без кликанья мышки\
# удаление символов, нажатие на кнопку решить через 'Enter',\
# кнопки быстрого выбора неравенств,\
# запрет ввода символов, которые могут вызвать ошибку
def enter(event):
    vvod['state'] = 'normal'
    if event.char == '\x08':
        vvod.delete(len(vvod.get()) - 1, tk.END)
    elif event.char == '\r':
        get()
    elif event.char == 'q':
        get('>')
    elif event.char == 'w':
        get('<')
    elif event.char == 'e':
        get('>=')
    elif event.char == 'r':
        get('<=')
    if event.char in '1234567890':
        vvod.insert(tk.END, event.char)
    elif event.char.lower() in 'x+-':
        vvod.insert(tk.END, event.char)
    vvod['state'] = 'disabled'


# позволяет пользователю через двоеное нажатие взаимодействовать со строкой \
# и переход в ручной режим
def handentry(event):
    global flag
    flag += 1
    vvod['state'] = 'normal'
    if event.char == '\r':
        get()
    win.unbind('<KeyPress>')
    if flag == 2:
        flag = 0
        vvod['state'] = 'disabled'
        win.bind('<KeyPress>', enter)


# кнопочки и их располодение
vvod = tk.Entry(win)
vvod.place(x=53, y=52)
vvod['state'] = 'disabled'
button = tk.Button(win, text='Решить', command=get)
btn1 = tk.Button(win, text='>', command=lambda: nerav('>'))
btn2 = tk.Button(win, text='<', command=lambda: nerav('<'))
btn3 = tk.Button(win, text='>=', command=lambda: nerav('>='))
btn4 = tk.Button(win, text='<=', command=lambda: nerav('<='))
btn1.place(x=200, y=52)
btn2.place(x=220, y=52)
btn3.place(x=240, y=52)
btn4.place(x=270, y=52)
button.place(x=150, y=52)
win.bind('<KeyPress>', enter)
win.bind('<Double-Button-1>', handentry)
win.mainloop()
