import random
import PIL.ImageTk
import PIL.Image
from Tkinter import *


def thinking():
    T1.insert(INSERT, 'Thinking...', "center")
    T1.after(3000, empty_textbox)


def empty_textbox():
    T1.delete("1.0", END)


def new_question(event=None):
    empty_textbox()
    if len(entry.get()) == 0:
        T1.insert(END, 'Ask a question', "center")
    else:
        thinking()
        T1.after(3000, give_answer)


def give_answer():
    answers = ['Signs point to yes.',
               'Yes.',
               'Reply hazy',
               'try again.',
               'Without a doubt.',
               'My sources say no.',
               'As I see it, yes.',
               'You may rely on it.',
               'Concentrate and ask again.',
               'Outlook not so good.',
               'It is decidedly so.',
               'Better not tell you now.',
               'Very doubtful.',
               'Yes - definitely.',
               'It is certain.',
               'Cannot predict now.',
               'Most likely.',
               'Ask again later.',
               'My reply is no.',
               'Outlook good.',
               'Don\'t count on it.']
    answer = random.randint(1, 20)
    T1.insert(END, answers[answer], "center")


def end():
    exit()


def clear():
    entry.delete(0, 'end')
    T1.delete('1.0', END)


root = Tk()

load = PIL.Image.open("8-ball.png")
render = PIL.ImageTk.PhotoImage(load)

img = Label(root, image=render)
img.image = render
img.pack()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

entry = Entry(root, width=40)
entry.pack()

T1 = Text(root, width=26, height=1)
T1.tag_configure("center", justify='center')
T1.tag_add("center", 1.0, "end")
T1.pack()

root.bind('<Return>', new_question)

button1 = Button(bottomFrame, text="Ask", fg="blue", command=new_question)
button2 = Button(bottomFrame, text="Clear", fg="blue", command=clear)
button3 = Button(bottomFrame, text="Quit", fg="blue", command=end)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

root.mainloop()
