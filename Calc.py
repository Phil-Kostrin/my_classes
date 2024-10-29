import tkinter as tk

def get_values():
    num1 = int(number1_entery.get())
    num2 = int(number2_entery.get())
    return num1, num2

def insert_values(value):
    answer_entery.delete(0, 'end')
    answer_entery.insert(0, value)

def add():
    num1, num2 = get_values()
    res = num1 +num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=2, height=1, command=add)
button_add.place(x=100,y=200)
button_sub = tk.Button(window, text='-', width=2, height=1, command=sub)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text='*', width=2, height=1, command=mul)
button_mul.place(x=200,y=200)
button_div = tk.Button(window, text='/', width=2, height=1, command=div)
button_div.place(x=250,y=200)
number1_entery = tk.Entry(window, width=28)
number1_entery.place(x=100,y=75)
number2_entery = tk.Entry(window, width=28)
number2_entery.place(x=100,y=150)
answer_entery = tk.Entry(window, width=28)
answer_entery.place(x=100,y=300)
number1 = tk.Label(window, text='Введите первое число: ')
number1.place(x=100,y=50)
number2 = tk.Label(window, text='Введите второе число: ')
number2.place(x=100,y=125)
answer = tk.Label(window, text='Результат: ')
answer.place(x=100,y=275)
window.mainloop()