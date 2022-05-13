from tkinter import *
import tkinter  
from tkinter.ttk import Radiobutton 
from tkinter import scrolledtext  
import tok
import spacy
  
text = "Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». Я-то из-за угла вышел 7 апреля."
nlp = spacy.load('ru_core_news_sm')
doc = nlp(text)

# Шаги интерфейса: 
# *** n = ?
# ** по дефолту (tokenize_filter) или с выбором критериев?
# *1) фильтр стоп-слов нужен?
# *2) отбор частей речи нужен?

def clicked_first_frame():    
    value_first_frame = selected_first.get()
    # value_first_frame = combo.get()
    label_frame_second.pack(padx=10, pady=10)
    lbl.configure(text=value_first_frame)
    return value_first_frame
  
def clicked_second_frame():  
    value_second_frame = selected_second.get()
    if value_second_frame == 2:
        txt.pack_forget()
        label_frame_third.pack(padx=10, pady=10)
    else:
        label_frame_third.pack_forget()
        txt.pack(padx=10, pady=10)
        txt.delete(1.0, END)
        txt.insert(INSERT, tok.tokenize_filter(doc, clicked_first_frame()))
    lbl2.configure(text=value_second_frame)  
    return value_second_frame

def clicked_third_frame():  
    value_third_frame = selected_third.get()
    lbl3.configure(text=value_third_frame)  
    return value_third_frame

window = Tk()  
window.title("Алгоритм декомпозиции текста на ключевые элементы")  
window.geometry('600x800') 

label_frame_first = LabelFrame(window, text='На какие токены хотите декомпозировать текст?')
label_frame_first.pack(padx=10, pady=10)
frame_first_rad = Frame(label_frame_first)
frame_first_rad.pack(padx=10, pady=0)
selected_first = IntVar()  
rad1 = Radiobutton(frame_first_rad,text='Униграммы', value=1, variable=selected_first).pack(side=tkinter.LEFT, padx=10, pady=10)
rad2 = Radiobutton(frame_first_rad,text='Биграммы', value=2, variable=selected_first).pack(side=tkinter.LEFT, padx=10, pady=10) 
rad3 = Radiobutton(frame_first_rad,text='Триграммы', value=3, variable=selected_first).pack(side=tkinter.LEFT, padx=10, pady=10)
rad4 = Radiobutton(frame_first_rad,text='1-2-3-граммы', value=4, variable=selected_first).pack(side=tkinter.LEFT, padx=10, pady=10)
btn = Button(label_frame_first, text="Выбрать", command=clicked_first_frame).pack(padx=10, pady=5)
lbl = Label(label_frame_first)
lbl.pack(side=tkinter.TOP, padx=10, pady=5)
 
# 0 - false - нет
# 1 - true - да

label_frame_second = LabelFrame(window, text='Делаем декомпозицию по умолчанию?')
label_frame_second.pack_forget()
# label_frame_second.pack(padx=10, pady=10)
lbl21 = Label(label_frame_second, text='Декомпозиция по умолчанию -- с фильтрацией стоп-слов и цифр').pack(padx=10, pady=10)
frame_second_rad = Frame(label_frame_second)
frame_second_rad.pack(padx=10, pady=0)
selected_second = IntVar()  
rad11 = Radiobutton(frame_second_rad,text='Декомпозиция по умолчанию', value=1, variable=selected_second).pack(side=tkinter.LEFT, padx=10, pady=10)
rad21 = Radiobutton(frame_second_rad,text='Выбрать параметры декомпозиции', value=2, variable=selected_second).pack(side=tkinter.LEFT, padx=10, pady=10) 
btn2 = Button(label_frame_second, text="Выбрать", command=clicked_second_frame).pack(padx=10, pady=5)
lbl2 = Label(label_frame_second)
lbl2.pack(padx=10, pady=5)


txt = scrolledtext.ScrolledText(window, width=60, height=10) 
txt.pack_forget() 


label_frame_third = LabelFrame(window, text='Нужен фильтр стоп-слов и цифр?')
label_frame_third.pack_forget()
frame_third_rad = Frame(label_frame_third)
frame_third_rad.pack(padx=10, pady=0)
selected_third = IntVar()  
rad31 = Radiobutton(frame_third_rad,text='Нужен', value=1, variable=selected_third).pack(side=tkinter.LEFT, padx=10, pady=10)
rad32 = Radiobutton(frame_third_rad,text='Не нужен', value=2, variable=selected_third).pack(side=tkinter.LEFT, padx=10, pady=10) 
btn3 = Button(label_frame_third, text="Выбрать", command=clicked_third_frame).pack(padx=10, pady=5)
lbl3 = Label(label_frame_third)
lbl3.pack(padx=10, pady=5)

window.mainloop()