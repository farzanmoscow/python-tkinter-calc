from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value =int(scvalue.get())

        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
window=Tk()

window.geometry("390x500")
window.resizable(0,0)

window.title("Tkinter Calculator")


scvalue=StringVar()
scvalue.set("")

screen=Entry(window,textvar=scvalue, font="lucida 28 bold",bg="gainsboro")
screen.pack(fill=X, ipadx=8, padx=12, pady=12)

f=Frame(window,bg="grey")
b=Button(f, text="C", padx=5,pady=2, font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>" , click)


b=Button(f, text="AC", padx=5,pady=2, font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)

 
b=Button(f, text="%",padx=5,pady=2,  font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="*",padx=5,pady=2,  font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)

f.pack(expand=True,fill="both")


f=Frame(window,bg="grey")
b=Button(f, text="7",padx=5,pady=2,  font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)


b=Button(f, text="8",padx=5,pady=2,  font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)

 
b=Button(f, text="9",padx=5,pady=2, font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="-",padx=5,pady=2,  font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)

f.pack(expand=True,fill="both")

f=Frame(window,bg="grey")
b=Button(f, text="4", padx=5,pady=2,  font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)


b=Button(f, text="5",padx=5,pady=2,font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)

 
b=Button(f, text="6",padx=5,pady=2, font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5) 
b.bind("<Button-1>", click)

b=Button(f, text="+",padx=5,pady=2,  font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)

f.pack(expand=True,fill="both")

f=Frame(window,bg="grey")
b=Button(f, text="0",padx=5,pady=2,  font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)


b=Button(f, text="-",padx=5,pady=2,  font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)

 
b=Button(f, text="*",padx=5,pady=2, font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)
f.pack(expand=True,fill="both")

f=Frame(window,bg="grey")
b=Button(f, text="/",padx=5,pady=2,  font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)


b=Button(f, text="%",padx=5,pady=2,  font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)

 
b=Button(f, text="=", padx=5,pady=2, font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5) 
b.bind("<Button-1>", click)
f.pack(expand=True,fill="both")

f=Frame(window,bg="grey")
b=Button(f, text="C",padx=5,pady=2,  font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)

b=Button(f, text=".",padx=5,pady=2,  font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="00",padx=5,pady=2,  font="lucida 20 bold")
b.pack(side=LEFT,expand=True, fill="both",padx=18,pady=5)
b.bind("<Button-1>", click)


f.pack(expand=True,fill="both")

window.mainloop()