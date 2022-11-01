#INTEGRATION
from tkinter import *
window = Tk()
window.geometry("1200x1200")
window.resizable(0,0)
window.configure(background="pink")
window.title("Candy Dispenser Project")
#image1
icon1 = PhotoImage(file = "C:/Users/HP/Downloads/sweets.png")
image1 = Label(window,image=icon1,bg="pink")
image1.place( x=200,y=30,height=100,width=100)
#image2
icon2 = PhotoImage(file = "C:/Users/HP/Downloads/sweets.png")
image2 = Label(window,image=icon2,bg="pink")
image2.place( x=800,y=30,height=100,width=100)

m =Label(window,text="CANDY DISPENSER",font=("Arial",30),bg="white")
m.place(x=300,y=50,height=60,width=500)
b =Label(window,text="PRESS A BUTTON",font=("Arial",14),bg="white")
b.place(x=20,y=150)
#buttons
import turtle
x = turtle.Turtle()
#drawing container
x.color("blue")
x.up()
x.goto(-100,-90)
x.forward(200)
x.left(90)
x.forward(200)
x.pendown()
x.backward(370)
x.left(90)
x.forward(200)
x.right(90)
x.forward(370)
x.up()
x.home()
#drawing rectangle
def draw_rect(x,y,color,fd):
    z.up()
    z.goto(x,y)
    z.down()
    z.begin_fill()
    z.fillcolor(color)
    z.forward(50)
    z.right(90)
    z.forward(fd)
    z.right(90)
    z.forward(50)
    z.right(90)
    z.forward(fd)
    z.right(90)
    z.end_fill()
    z.up()
    z.home()
def draw_circle(x,y,rad,color):
    c.goto(x,y)
    c.down()
    c.begin_fill()
    c.fillcolor(color)
    c.circle(rad)
    c.end_fill()
    c.up()
    c.home()

c = turtle.Turtle()
c.up()
z= turtle.Turtle()

def change():
    current_size = s.size()
    if current_size == 1:
        return 110 - (60 * current_size) +15
    else:
        return 110 - (45 * current_size)

#func for compressing spring lowering it
def compress_spring():
    current_rectsize = s.size()
    return 350 -(40*current_rectsize)
def lower_rectpos():
    current_pos =s.size()
    return 91 -(40*current_pos)
def clear_func():
    z.clear()
#func for compressing spring lowering it
def relax_spring():
    current_rectsize = s.size()
    return 220 +(-20*current_rectsize)
def lift_rectpos():
    current_pos =s.size()
    return -40 -(20*current_pos)
draw_rect(-30, 91, "blue", 350)
class Stack:
    def __init__(self):
     self.items =[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        if s.size() ==8:
            turtle.write("stack is full", align="center", font=("Cooper Black", 25, "italic"))
        else:
            self.items.append(item)
            draw_circle(-5, change(), 15, "green")
            z.clear()
            draw_rect(-30, lower_rectpos(), "black", compress_spring())



    def pop(self):
            erase()
            z.clear()
            draw_rect(-30, lift_rectpos(), "pink", relax_spring())
            return self.items.pop()


    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
s = Stack()

def finish():
    res = txt.get()
    s.push(res)
def do_pop():
    s.pop()

def do_top():
    p=s.peek()
    top_val= Label(window, text=p, bg="white")
    top_val.place(x=250, y=300,width=80, height=80)
def do_size():
    a = s.size()
    size_val = Label(window, text=a, bg="white")
    size_val.place(x=360, y=300, width=80, height=80)

q= s.size()

def erase():
    for i in range(7+q):
            c.undo()
    # or c.clear()

def do_empty():
    b= s.is_empty()
    d= "Yes" if b else "No"
    size_val = Label(window, text=d, bg="white")
    size_val.place(x=470, y=300, width=80, height=80)

def clicked():
    prompt =Label(window,text="enter value to be pushed",bg="white")
    prompt.place(x=32,y=310)

push=Button(window,text ="PUSH",bg="white",font=("Arial",8),command=clicked)
push.place(x=30,y=220,width=70,height=70,)
def close_window():
    window.destroy()
    exit()
func=Label(window,text="PUSH VALUE",bg="white")
func.place(x=32,y=340)
txt=Entry(window,width=15)
txt.place(x=32,y=380)

finish=Button(window,text ="FINISH",bg="white",font=("Arial",8),command=finish)
finish.place(x=32,y=420,width=70,height=70)

pop=Button(window,text ="POP",bg="white",font=("Arial",8),command=do_pop)
pop.place(x=140,y=220,width=70,height=70)

top=Button(window,text ="TOP",bg="white",font=("Arial",8),command=do_top)
top.place(x=250,y=220,width=70,height=70)

size=Button(window,text ="SIZE",bg="white",font=("Arial",8),command=do_size)
size.place(x=360,y=220,width=70,height=70)

isempty=Button(window,text ="IS EMPTY?",bg="white",font=("Arial",8),command=do_empty)
isempty.place(x=470,y=220,width=70,height=70)

close=Button(window,text ="CLOSE WINDOW",bg="white",font=("Arial",8),command=close_window)
close.place(x=580,y=220,width=200,height=70)

turtle.done()
window.mainloop()

