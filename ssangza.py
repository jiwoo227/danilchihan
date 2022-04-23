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
    singular.geometry('600x60+0+0')

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
    hello = Label(singular, text=f'\n\n{"  ".join(list1)}\n\t{"  ".join(arr)}')
    pw = Label(singular, text=f'암호문 : {new_text}')
    board.pack()
    hello.pack()
    pw.pack()

def second():
    singular = Tk()
    singular.title('decryptedkey page')
    singular.geometry('600x60+0+0')


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

    board = Label(singular, text=f'암호판 : \t{"  ".join(list1)}\n\t{"  ".join(arr)}')
    pw = Label(singular, text=f'복호문 : {text}')
    board.pack()
    pw.pack()


singular = tk.Tk()
singular.title('main page')
singular.geometry('700x700')
str = StringVar()
str1 = StringVar()

textbox = Entry(singular, width=30, textvariable=str)
textbox.pack()
textbox1 = Entry(singular, width=30, textvariable=str1)
textbox1.pack()

button_put = ttk.Button(singular, height=2, width=10, text="암호화", command=first)
button_put.pack()
button_put1 = ttk.Button(singular, height=2, width=10, text="복호화", command=second)
button_put1.pack()

textbox.place(x=300, y=320)
textbox1.place(x=300, y=385)
button_put.place(x=180, y=520)
button_put1.place(x=445, y=520)


singular.mainloop()