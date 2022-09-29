from tkinter import *
from tkinter import font
from  googletrans import Translator
from gtts import gTTS

tk_window = Tk()
tk_window.geometry("600x300")
tk_window.config(bg="Light blue")

lang_option = []

entry_window = Entry(tk_window, bg="black", fg="white", font=("Arial", 16,"bold"))
enter_window.place(x=20, y=40)

drop_down = StringVar()
drop_down.set("Select Language")

list_lang = OptionMenu(tk_window, drop_down, *lang_option)
list_lang.configure(bg = "yellow", fb="black", font=("arial",16 , "bold"))
list_lang.place(x=400, y=40)

one_label = Label(tk_window, text = "\t\t\t\t\t", bg="black", fg="white", font=("arial",42 , "bold"))
one_label.place(x=0, y=120)

# 48:03

tk_window.mainloop()