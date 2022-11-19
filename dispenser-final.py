from tkinter import *
from tkinter import messagebox
root = Tk()

root.title('Candy Dispenser')

my_canvas = Canvas(root, width=700, height=700, bg='pink')
my_canvas.grid(column=0, row=0, pady=20, padx=20)

#declaring vars
my_canvas.create_line(120, 650, 480, 650, width=10)
my_canvas.create_line(120, 650, 120, 30, width=5)
my_canvas.create_line(480, 650, 480, 30, width=5)

k = 50
candy_h = 30
candy_height =30
start_point_x = 120
start_point_y = 650

def draw_spring(start_point_x, start_point_y, k):
    i = 0
    level = 6
    while i <= level:
        my_canvas.create_line(start_point_x, start_point_y, 480, start_point_y - k, width=2)
        my_canvas.create_line(480, start_point_y - k, 120, start_point_y - k - k / 2, width=2)
        if i == level:
            my_canvas.create_line(120, start_point_y - k - k / 2, 480, start_point_y - k - k / 2, width=5)

        i = i + 1
        start_point_y = start_point_y - k - k / 2
    return start_point_y


def draw_candy(start_point_x, start_point_y, h, number_of_candies):
    i = 0
    while i < number_of_candies:
        my_canvas.create_oval(start_point_x, start_point_y - (h * (i + 1)), 480, start_point_y - (h * i), width=4,
                           outline='black', fill='green')
        text_x = (start_point_x + 480) / 2
        text_y = ((start_point_y - (h * (i + 1))) + (start_point_y - (h * i))) / 2

        my_canvas.create_text(text_x, text_y, text=f"{i + 1}", fill="black", font=('Arial 15 '))
        i = i + 1


draw_spring(start_point_x, start_point_y, k)

#Creating the stack
class Stack:
    def __init__(self):
     self.items = []
    def is_empty(self):
        return self.items == []
    def push(self,item):
             self.items.append(item)

             if(s.size()>=19):
                 messagebox.showinfo("Error", "Dispenser Full")

             my_canvas.delete('all')
             my_canvas.create_line(120, 650, 480, 650, width=10)
             my_canvas.create_line(120, 650, 120, 30, width=5)
             my_canvas.create_line(480, 650, 480, 30, width=5)

             print(s.size())
             k = 50
             k = k - s.size() * 2.5
             candy_start_point_y = draw_spring(start_point_x, start_point_y, k)
             draw_candy(start_point_x, candy_start_point_y, candy_h, s.size())


    def pop(self):
        if s.size()==0:
            messagebox.showinfo("Error", "Dispenser Empty")
        else:
            return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
s = Stack()

#FUNCTIONS FOR BUTTONS
def finish_push():
    res = txt.get()
    s.push(res)
    print(s.items)
def clicked():
    prompt =Label(root,text="push value",bg="white")
    prompt.place(x=15,y=60)
txt=Entry(root,width=10)
txt.place(x=25,y=90)
def close_window():
    root.destroy()
    exit()
def finish_pop():
    if(s.size()==0):
        messagebox.showinfo("Error", "Dispenser Empty")
    elif (s.size() > 0):
        my_canvas.delete('all')
        s.pop()
    my_canvas.create_line(120, 650, 480, 650, width=10)
    my_canvas.create_line(120, 650, 120, 30, width=5)
    my_canvas.create_line(480, 650, 480, 30, width=5)
    print(s.size())
    k = 50
    k = k - s.size() * 2.5
    candy_start_point_y = draw_spring(start_point_x, start_point_y, k)
    draw_candy(start_point_x, candy_start_point_y, candy_h, s.size())
def show_size():
    if (s.size()>0):
        messagebox.showinfo("Status",f"SIZE = {s.size()}")
    else:
        messagebox.showinfo("Error","SIZE=0")
def top():
    if(s.size()>0):
        messagebox.showinfo("Status", f" TOP= {s.peek()}")
    else:
        messagebox.showinfo("Error", "Empty Dispenser")
def show_isempty():
    if (s.size()==0):
        messagebox.showinfo("Status","TRUE")
    else:
        messagebox.showinfo("Status","FALSE")

#BUTTONS
push=Button(root, text ="PUSH", bg="white", font=("Arial", 8),command=clicked)
push.place(x=25, y=20, width=40, height=40)

finish=Button(root,text ="FINISH",bg="white",font=("Arial",8),command=finish_push)
finish.place(x=25,y=120,width=40,height=40)

pop = Button(root,text = "POP", bg="white", font=("Arial", 8), command=finish_pop)
pop.place(x=75, y=20, width=40, height=40)

top=Button(root,text ="TOP", bg="white", font=("Arial", 8),command=top)
top.place(x=125, y=20, width=40, height=40)

size=Button(root, text="SIZE",bg="white", font=("Arial", 8),command=show_size)
size.place(x=175, y=20, width=40, height=40)

isempty=Button(root, text ="IS EMPTY ?", bg="white", font=("Arial", 8),command=show_isempty)
isempty.place(x=225, y=20, width=40, height=40)
close = Button(root,text ="CLOSE", bg="white", font=("Arial", 8), command=close_window)
close.place(x=275, y=20, width=40, height=40)

root.mainloop()