from tkinter import *

first_number = second_number = operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    global first_number, second_number, operator
    first_number = second_number = operator = None
    result_label.config(text='')
    input_label.config(text='')

def get_operator(op):
    global first_number, operator
    first_number = float(result_label['text'])  # Convert the first number to float
    operator = op
    result_label.config(text='')
    input_label.config(text=str(first_number) + ' ' + op)

def delete_last_digit():
    current = result_label['text']
    if current:
        new = current[:-1]  # Remove the last character
        result_label.config(text=new)

def get_result():
    global first_number, second_number, operator

    if first_number is not None and operator is not None:
        second_number = float(result_label['text'])  # Convert the second number to float

        if operator == '+':
            result = first_number + second_number
        elif operator == '-':
            result = first_number - second_number
        elif operator == '*':
            result = first_number * second_number
        else:
            if second_number == 0:
                result_label.config(text='Error')
                input_label.config(text='')
                return
            else:
                result = round(first_number / second_number, 2)

        result_label.config(text=str(result))
        input_label.config(text=str(first_number) + ' ' + operator + ' ' + str(second_number) + ' = ' + str(result))


root = Tk()
root.title('Calculator')
root.geometry('280x400')
root.resizable(0, 0)
root.configure(background='white')

input_label = Label(root, text='', fg='black', bg='white')
input_label.grid(row=0, column=0, columnspan=5, pady=(50, 5), sticky='w')
input_label.config(font=('Arial', 15))

result_label = Label(root, text='', fg='black', bg='white')
result_label.grid(row=1, column=0, columnspan=5, pady=(5, 25), sticky='w')
result_label.config(font=('Arial', 30, 'bold'))

for i in range(1, 10):
    btn = Button(root, text=str(i), bg='#0000FF', fg='white', width=5, height=2, command=lambda i=i: get_digit(i))
    row_num = (i - 1)//3 +1
    col_num = (i - 1) % 3
    btn.grid(row=row_num,column=col_num)
    btn.config(font=('Arial',15))


btn_clr = Button(root,text='C',bg='#0000FF',fg='white',width=5,height=2,command=lambda :clear())
btn_clr.grid(row=1,column=0)
btn_clr.config(font=('Arial',14))

btn_percentage = Button(root, text='%', bg='#0000FF', fg='white', width=5, height=2, command=lambda: get_operator('%'))
btn_percentage.grid(row=1, column=1)
btn_percentage.config(font=('Arial', 14))


btn_del = Button(root, text='del', bg='#0000FF', fg='white', width=5, height=2, command=delete_last_digit)
btn_del.grid(row=1, column=2)
btn_del.config(font=('Arial', 14))



btn_div = Button(root,text='/',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_operator('/'))
btn_div.grid(row=1,column=3)
btn_div.config(font=('Arial',14))


btn7 = Button(root,text='7',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_digit(7))
btn7.grid(row=2,column=0)
btn7.config(font=('Arial',14))

btn8 = Button(root,text='8',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_digit(8))
btn8.grid(row=2,column=1)
btn8.config(font=('Arial',14))

btn9 = Button(root,text='9',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_digit(9))
btn9.grid(row=2,column=2)
btn9.config(font=('Arial',14))

btn_mul = Button(root,text='*',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_operator('*'))
btn_mul.grid(row=2,column=3)
btn_mul.config(font=('Arial',14))

btn4 = Button(root,text='4',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_digit(4))
btn4.grid(row=3,column=0)
btn4.config(font=('Arial',14))

btn5 = Button(root,text='5',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_digit(5))
btn5.grid(row=3,column=1)
btn5.config(font=('Arial',14))

btn6 = Button(root,text='6',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_digit(6))
btn6.grid(row=3,column=2)
btn6.config(font=('Arial',14))

btn_sub = Button(root,text='-',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_operator('-'))
btn_sub.grid(row=3,column=3)
btn_sub.config(font=('Arial',14))

btn1 = Button(root,text='1',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_digit(1))
btn1.grid(row=4,column=0)
btn1.config(font=('Arial',14))

btn2 = Button(root,text='2',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_digit(2))
btn2.grid(row=4,column=1)
btn2.config(font=('Arial',14))

btn3 = Button(root,text='3',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_digit(3))
btn3.grid(row=4,column=2)
btn3.config(font=('Arial',14))

btn_add = Button(root,text='+',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_operator('+'))
btn_add.grid(row=4,column=3)
btn_add.config(font=('Arial',14))

btn00 = Button(root,text='00',bg='#FFA500',fg='white',width=5,height=2,command=lambda :get_digit(00))
btn00.grid(row=5,column=0)
btn00.config(font=('Arial',14))

btn0 = Button(root,text='0',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_digit(0))
btn0.grid(row=5,column=1)
btn0.config(font=('Arial',14))



btn_full_stop = Button(root,text='.',bg='#0000FF',fg='white',width=5,height=2,command=lambda :get_operator('.'))
btn_full_stop.grid(row=5,column=2)
btn_full_stop.config(font=('Arial',14))

btn_equals = Button(root,text='=',bg='#0000FF',fg='white',width=5,height=2,command=get_result)
btn_equals.grid(row=5,column=3)
btn_equals.config(font=('Arial',14))


root.mainloop()


