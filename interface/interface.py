from tkinter import *
import tkinter  
from tkinter.ttk import Radiobutton 
from tkinter import scrolledtext  
import tok
import spacy
  
text = "Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». (1999)"
nlp = spacy.load('ru_core_news_sm')
doc = nlp(text)

# Шаги интерфейса: 
# *** n = ?
# ** по дефолту (tokenize_filter) или с выбором критериев?
# *1) отбор частей речи нужен?
# *2) фильтр стоп-слов нужен?
# *3) фильтр ents нужен?

def clicked_first_frame():    
    value_first_frame = selected_first.get()
    label_frame_second.pack(padx=10, pady=10)
    return value_first_frame
  
def clicked_second_frame():  
    value_second_frame = selected_second.get()
    if value_second_frame == 2:
        txt.pack_forget()
        label_frame_third.pack(padx=10, pady=10)
    else:
        label_frame_third.pack_forget()
        label_frame_fourth.pack_forget()
        label_frame_fifth.pack_forget()
        label_frame_sixth.pack_forget()
        label_frame_seventh.pack_forget()
        txt.pack(padx=10, pady=10)
        txt.delete(1.0, END)
        txt.insert(INSERT, "".join(str([ngram for ngram in tok.tokenize_filter_ents(doc, clicked_first_frame())])))
    return value_second_frame

def clicked_third_frame():  
    value_third_frame = selected_third.get()
    if value_third_frame == 2:
        txt.pack_forget()
        label_frame_fourth.pack_forget()
        label_frame_sixth.pack_forget()
        label_frame_seventh.pack_forget()
        label_frame_fifth.pack(padx=10, pady=10)
    else:
        txt.pack_forget()
        label_frame_fifth.pack_forget()
        label_frame_sixth.pack_forget()
        label_frame_seventh.pack_forget()
        label_frame_fourth.pack(padx=10, pady=10)
    return value_third_frame

def clicked_fourth_frame():  
    value_fourth_frame = selected_fourth.get()
    if value_fourth_frame == 2:
        txt.pack(padx=10, pady=10)
        txt.delete(1.0, END)
        txt.insert(INSERT, "".join(str([ngram for ngram in tok.tokenize_checkPOS(doc, clicked_first_frame())])))
    else:
        txt.pack(padx=10, pady=10)
        txt.delete(1.0, END)
        txt.insert(INSERT, "".join(str([ngram for ngram in tok.tokenize_filter_checkPOS(doc, clicked_first_frame())])))
    return value_fourth_frame

def clicked_fifth_frame():  
    value_fifth_frame = selected_fifth.get()
    if value_fifth_frame == 2:
        txt.pack_forget()
        label_frame_sixth.pack_forget()
        label_frame_seventh.pack(padx=10, pady=10)
    else:
        txt.pack_forget()
        label_frame_seventh.pack_forget()
        label_frame_sixth.pack(padx=10, pady=10)
    return value_fifth_frame

def clicked_sixth_frame():  
    value_sixth_frame = selected_sixth.get()
    if value_sixth_frame == 2:
        txt.pack(padx=10, pady=10)
        txt.delete(1.0, END)
        txt.insert(INSERT, "".join(str([ngram for ngram in tok.tokenize_filter(doc, clicked_first_frame())])))
    else:
        txt.pack(padx=10, pady=10)
        txt.delete(1.0, END)
        txt.insert(INSERT, "".join(str([ngram for ngram in tok.tokenize_filter_ents(doc, clicked_first_frame())])))
    return value_sixth_frame

def clicked_seventh_frame():  
    value_seventh_frame = selected_seventh.get()
    if value_seventh_frame == 2:
        txt.pack(padx=10, pady=10)
        txt.delete(1.0, END)
        txt.insert(INSERT, "".join(str([ngram for ngram in tok.tokenize_only(doc, clicked_first_frame())])))
    else:
        txt.pack(padx=10, pady=10)
        txt.delete(1.0, END)
        txt.insert(INSERT, "".join(str([ngram for ngram in tok.tokenize_ents(doc, clicked_first_frame())])))
    return value_seventh_frame

window = Tk()  
window.title("Алгоритм декомпозиции текста на ключевые элементы")  
window.geometry('600x800') 

scroll_bar = Scrollbar(window)
scroll_bar.pack(side = RIGHT, fill = Y)

# ---1---
label_frame_first = LabelFrame(window, text='На какие токены хотите декомпозировать текст?')
label_frame_first.pack(padx=10, pady=10)
frame_first_rad = Frame(label_frame_first)
frame_first_rad.pack(padx=10, pady=0)
selected_first = IntVar()  
rad1 = Radiobutton(frame_first_rad,text='Униграммы', value=1, variable=selected_first).pack(side=tkinter.LEFT, padx=10, pady=5)
rad2 = Radiobutton(frame_first_rad,text='Биграммы', value=2, variable=selected_first).pack(side=tkinter.LEFT, padx=10, pady=5) 
rad3 = Radiobutton(frame_first_rad,text='Триграммы', value=3, variable=selected_first).pack(side=tkinter.LEFT, padx=10, pady=5)
rad4 = Radiobutton(frame_first_rad,text='1-2-3-граммы', value=4, variable=selected_first).pack(side=tkinter.LEFT, padx=10, pady=5)
btn = Button(label_frame_first, text="Выбрать", command=clicked_first_frame).pack(padx=10, pady=5)


# ---2---
label_frame_second = LabelFrame(window, text='Делаем декомпозицию по умолчанию?')
label_frame_second.pack_forget()
lbl21 = Label(label_frame_second, text='Декомпозиция по умолчанию - с фильтрацией стоп-слов и цифр').pack(padx=10, pady=3)
frame_second_rad = Frame(label_frame_second)
frame_second_rad.pack(padx=10, pady=0)
selected_second = IntVar()  
rad11 = Radiobutton(frame_second_rad,text='Декомпозиция по умолчанию', value=1, variable=selected_second).pack(side=tkinter.LEFT, padx=10, pady=5)
rad21 = Radiobutton(frame_second_rad,text='Выбрать параметры декомпозиции', value=2, variable=selected_second).pack(side=tkinter.LEFT, padx=10, pady=5) 
btn2 = Button(label_frame_second, text="Выбрать", command=clicked_second_frame).pack(padx=10, pady=5)


txt = scrolledtext.ScrolledText(window, width=60, height=10) 
txt.pack_forget() 


# ---3---
label_frame_third = LabelFrame(window, text='Нужен отбор частей речи?')
label_frame_third.pack_forget()
lbl31 = Label(label_frame_third, text='При выборе опции "отбор частей речи" в выходных данных алгоритма Вы увидите только').pack(padx=10, pady=0)
lbl31 = Label(label_frame_third, text='существительные и прилагательные (именные сущности будут удалены).').pack(padx=10, pady=0)
frame_third_rad = Frame(label_frame_third)
frame_third_rad.pack(padx=10, pady=0)
selected_third = IntVar()  
rad31 = Radiobutton(frame_third_rad,text='Нужен', value=1, variable=selected_third).pack(side=tkinter.LEFT, padx=10, pady=5)
rad32 = Radiobutton(frame_third_rad,text='Не нужен', value=2, variable=selected_third).pack(side=tkinter.LEFT, padx=10, pady=5) 
btn3 = Button(label_frame_third, text="Выбрать", command=clicked_third_frame).pack(padx=10, pady=5)


# ---4---
label_frame_fourth = LabelFrame(window, text='Нужен фильтр стоп-слов и цифр?')
label_frame_fourth.pack_forget()
frame_fourth_rad = Frame(label_frame_fourth)
frame_fourth_rad.pack(padx=10, pady=0)
selected_fourth = IntVar()  
rad41 = Radiobutton(frame_fourth_rad,text='Нужен', value=1, variable=selected_fourth).pack(side=tkinter.LEFT, padx=10, pady=5)
rad42 = Radiobutton(frame_fourth_rad,text='Не нужен', value=2, variable=selected_fourth).pack(side=tkinter.LEFT, padx=10, pady=5) 
btn4 = Button(label_frame_fourth, text="Выбрать", command=clicked_fourth_frame).pack(padx=10, pady=5)


# ---5---
label_frame_fifth = LabelFrame(window, text='Нужен фильтр стоп-слов и цифр?')
label_frame_fifth.pack_forget()
frame_fifth_rad = Frame(label_frame_fifth)
frame_fifth_rad.pack(padx=10, pady=0)
selected_fifth = IntVar()  
rad51 = Radiobutton(frame_fifth_rad,text='Нужен', value=1, variable=selected_fifth).pack(side=tkinter.LEFT, padx=10, pady=5)
rad52 = Radiobutton(frame_fifth_rad,text='Не нужен', value=2, variable=selected_fifth).pack(side=tkinter.LEFT, padx=10, pady=5) 
btn5 = Button(label_frame_fifth, text="Выбрать", command=clicked_fifth_frame).pack(padx=10, pady=5)


# ---6---
label_frame_sixth = LabelFrame(window, text='Нужен фильтр именных сущностей?')
label_frame_sixth.pack_forget()
frame_sixth_rad = Frame(label_frame_sixth)
frame_sixth_rad.pack(padx=10, pady=0)
selected_sixth = IntVar()  
rad61 = Radiobutton(frame_sixth_rad,text='Нужен', value=1, variable=selected_sixth).pack(side=tkinter.LEFT, padx=10, pady=5)
rad62 = Radiobutton(frame_sixth_rad,text='Не нужен', value=2, variable=selected_sixth).pack(side=tkinter.LEFT, padx=10, pady=5) 
btn6 = Button(label_frame_sixth, text="Выбрать", command=clicked_sixth_frame).pack(padx=10, pady=5)


# ---7---
label_frame_seventh = LabelFrame(window, text='Нужен фильтр именных сущностей?')
label_frame_seventh.pack_forget()
frame_seventh_rad = Frame(label_frame_seventh)
frame_seventh_rad.pack(padx=10, pady=0)
selected_seventh = IntVar()  
rad71 = Radiobutton(frame_seventh_rad,text='Нужен', value=1, variable=selected_seventh).pack(side=tkinter.LEFT, padx=10, pady=5)
rad72 = Radiobutton(frame_seventh_rad,text='Не нужен', value=2, variable=selected_seventh).pack(side=tkinter.LEFT, padx=10, pady=5) 
btn7 = Button(label_frame_seventh, text="Выбрать", command=clicked_seventh_frame).pack(padx=10, pady=5)


window.mainloop()