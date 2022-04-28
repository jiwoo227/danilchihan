import tkinter as ttk
import tkinter
import tkinter as tk
from tkinter import *

text1 = ''
text2 = ''

def indexx(arr):
    result = []
    for a in arr:
        if a not in result:
            result.append(a)

    return result

def first():
    singular = Tk()
    singular.title('cryptogram page')
    singular.geometry('700x300')

    list1 = ['a', 'b', 'c', 'd', 'e',
             'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']


    arr = list(textbox.get().strip())
    text = textbox1.get().strip()
    print(arr)
    print(text)

    index = list1.index(arr[-1])
    arr.extend(list1[index:])
    arr.extend(list1)
    arr = indexx(arr)


    new_text = ''
    for index, a in enumerate(text):
        if a == ' ':
            new_text += ' '
            continue
        print(list1.index(a))
        new_text += arr[list1.index(a)]
    print(new_text)
    print(arr)

    board = Label(singular, text=f'암호판', font=(5))
    hello = Label(singular, text=f'{"  ".join(list1)}'
                                 f'\n\n{"  ".join(arr)}', bg='#A5E151', font=(3))
    pw = Label(singular, text=f'암호문 : {new_text}', font=(3))
    board.pack()
    hello.pack()
    board.place(x=300, y=60)
    hello.place(x=50, y=100)
    pw.pack()
    pw.place(x=200, y=200)

def second():
    singular = Tk()
    singular.title('decryptedkey page')
    singular.geometry('700x300')

    list1 = ['a', 'b', 'c', 'd', 'e',
             'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']


    arr = list(textbox.get().strip())
    text = textbox1.get().strip()
    print(arr)
    print(text)

    index = list1.index(arr[-1])
    arr.extend(list1[index:])
    arr.extend(list1)
    arr = indexx(arr)


    new_text = ''
    for index, a in enumerate(text):
        if a == ' ':
            new_text += ' '
            continue
        print(list1.index(a))
        new_text += arr[list1.index(a)]
    print(new_text)
    print(list1)
    print(arr)

    board = Label(singular, text=f'암호판', font=(5))
    hello = Label(singular, text=f'{"  ".join(list1)}'
                                 f'\n\n{"  ".join(arr)}', bg='#A5E151', font=(3))
    pw = Label(singular, text=f'복호문 : {text}', font=(3))
    board.pack()
    hello.pack()
    board.place(x=300, y=60)
    hello.place(x=50, y=100)
    pw.pack()
    pw.place(x=200, y=200)


singular = tk.Tk()
singular.title('main page')
singular.geometry('700x700')
str = StringVar()
str1 = StringVar()

mainBack = tkinter.PhotoImage(file='input.png')
mainBackL = tkinter.Label(image=mainBack)
mainBackL.place(x=-2, y=-2)

textbox = Entry(singular, width=30, textvariable=str)
textbox.pack()
textbox1 = Entry(singular, width=30, textvariable=str1)
textbox1.pack()

button_put = ttk.Button(singular, height=3, width=34, text="암호화",bg='#C2C2C2', command=first)
button_put.pack()
button_put1 = ttk.Button(singular, height=3, width=34, text="복호화",bg='#C2C2C2', command=second)
button_put1.pack()

textbox.place(x=300, y=320)
textbox1.place(x=300, y=385)
button_put.place(x=87, y=510)
button_put1.place(x=360, y=510)


singular.mainloop()