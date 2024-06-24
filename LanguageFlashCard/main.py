import random

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
random_element=None
file = pandas.read_csv("./data/french_words.csv")
word_dictionary = file.to_dict(orient="records")
# print(word_dictionary)
list=[]

def click():
    global random_element
    global word_dictionary
    if random_element in word_dictionary:
        word_dictionary.remove(random_element)
    crazy()

def crazy():
    global random_element
    global word_dictionary
    random_element = random.choice(word_dictionary)
    french_word = random_element["French"]
    canvas.itemconfig(canvas_image, image=Card_front)
    canvas.itemconfig(word, text=french_word, fill='black')
    canvas.itemconfig(title, text='French', fill='black')
    window.after(3000, flip)
def flip():
    global random_element
    global word_dictionary
    canvas.itemconfig(canvas_image, image=Card_back, )
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=random_element['English'], fill='white')
    # word_dictionary.remove(random_element)

def click2():
    global word_dictionary
    global random_element
    list.append(random_element)
    if 0 in list:
        list.remove(0)
    print(list)
    data=pandas.DataFrame(list)
    data.to_csv("./data/FRENCH_WORDS_TO_LEARN.csv")

    crazy()

window=Tk()
window.minsize(height=700,width=700)
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

Card_front=PhotoImage(file="./images/card_front.png")
Card_back=PhotoImage(file="./images/card_back.png")
check_sign=PhotoImage(file="./images/right.png")
cross_sign=PhotoImage(file="./images/wrong.png")

canvas=Canvas()
canvas.config(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_image=canvas.create_image(400,526/2,image=Card_front)
title=canvas.create_text(400,150,text="Click on ✅ button to start.",font=("Ariel",40,'italic'))
word=canvas.create_text(400,263,text="",font=("Ariel",60,'bold'))
canvas.grid(row=0,column=0,columnspan=2)

check=Button()
check.config(image=cross_sign,highlightthickness=0,bg=BACKGROUND_COLOR,command=click2)
check.grid(row=1, column=0)

cross=Button()
cross.config(image=check_sign,highlightthickness=0,bg=BACKGROUND_COLOR,command=click)
cross.grid(row=1,column=1)


window.mainloop()

