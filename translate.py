from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator
root = Tk()
root.title('Translator')
root.geometry("1090x440")
root.configure(bg='#856ff8')

arro_image = PhotoImage(file='arrow.png')
image_lable = Label(root, image=arro_image, width=130)
image_lable.place(x=477, y=165)


def label_change():
    c1 = combo1.get()
    c2 = combo2.get()

    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1000, label_change)


def translate_now():
    if (combo1.get() == 'Select language' or combo2.get() == 'Select language'):
        messagebox.showerror("Error!","Select the language")
    else:
        text = text1.get(1.0, END)
        t1 = Translator()
        trans_text = t1.translate(text, src=combo1.get(), dest=combo2.get())
        trans_text = trans_text.text
        text2.delete(1.0, END)
        text2.insert(END, trans_text)


def clear_text():
    text1.delete(1.0, END)
    text2.delete(1.0, END)
    combo2.set('Select language')
    combo1.set('Select language')


languages = googletrans.LANGUAGES
languageV = list(languages.values())

combo1 = ttk.Combobox(root, values=languageV, font='Times 14', state='r')
combo1.place(x=100, y=20)
combo1.set('Select language')

label1 = Label(root, font='Times 30 bold',
               bg='white', width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f1 = Frame(root, bg='Black', bd=5)
f1.place(x=10, y=118, width=460, height=230)

text1 = Text(f1, font='Times 20', bg='white', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=450, height=220)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill='y')
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font='Times 14', state='r')
combo2.place(x=730, y=20)
combo2.set('Select language')

label2 = Label(root, font='Times 30 bold',
               bg='white', width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f2 = Frame(root, bg='Black', bd=5)
f2.place(x=620, y=118, width=460, height=230)

text2 = Text(f2, font='Times 20', bg='white', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=450, height=220)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill='y')
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

translate_button = Button(root, text='Translate', font='Times 15 bold italic', cursor='hand2',
                          bg='red', fg='white', command=translate_now, padx=5, pady=5)
translate_button.place(x=450, y=370)

clear_button = Button(root, text="Clear", command=clear_text,
                      font='Times 15 bold italic', cursor='hand2', bg='red', fg='white', padx=5, pady=5)
clear_button.place(x=570, y=370)
label_change()
root.mainloop()
