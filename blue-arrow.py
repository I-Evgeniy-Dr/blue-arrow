Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from tkinter import*
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
1
canvas.move(1, 5, 0)
my_triangle = canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.move(my_triangle, 5, 0)
from tkinter import*
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
my_triangle = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='red')

def move_triangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    elif event.keysym == '1':
        canvas.move(1, -3, 3)
     elif event.keysym == '7':
         canvas.move(1, -3, -3)
     elif event.keysym == '9':
         canvas.move(1, 3, -3)
     elif event.keysym == '3':
         canvas.move(1, 3, 3)
     else:
         canvas.move(1, 3, 0)
         
SyntaxError: unindent does not match any outer indentation level
def move_triangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    elif event.keysym == '1':
        canvas.move(1, -3, 3)
     elif event.keysym == '7':
         canvas.move(1, -3, -3)
     elif event.keysym == '9':
         canvas.move(1, 3, -3)
     elif event.keysym == '3':
         canvas.move(1, 3, 3)
     else:
         canvas.move(1, 3, 0)
         
SyntaxError: unindent does not match any outer indentation level
def move_triangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
        
    elif event.keysym == 'Left':
        
        canvas.move(1, -3, 0)
        
    elif event.keysym == '1':
        
        canvas.move(1, -3, 3)
        
     elif event.keysym == '7':
         
         canvas.move(1, -3, -3)
         
     elif event.keysym == '9':
         
         canvas.move(1, 3, -3)
         
     elif event.keysym == '3':
         
         canvas.move(1, 3, 3)
         
     else:
         
         canvas.move(1, 3, 0)
         
SyntaxError: unindent does not match any outer indentation level
def move_triangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    elif event.keysym == '1':
        canvas.move(1, -3, 3)
     elif event.keysym == '7':
         canvas.move(1, -3, -3)
     elif event.keysym == '9':
         canvas.move(1, 3, -3)
     elif event.keysym == '3':
         canvas.move(1, 3, 3)
     else:
         canvas.move(1, 3, 0)
         
SyntaxError: unindent does not match any outer indentation level
>>> def move_triangle(event):
...     if event.keysym == 'Up':
...         canvas.move(1, 0, -3)
...     elif event.keysym == 'Down':
...         canvas.move(1, 0, 3)
...     elif event.keysym == 'Left':
...         canvas.move(1, -3, 0)
...     elif event.keysym == '1':
...         canvas.move(1, -3, 3)
...     elif event.keysym == '7':
...         canvas.move(1, -3, -3)
...     elif event.keysym == '9':
...         canvas.move(1, 3, -3)
...     elif event.keysym == '3':
...         canvas.move(1, 3, 3)
...     else:
...         canvas.move(1, 3, 0)
... 
...         
>>> canvas.bind_all('<KeyPress-Up>', move_triangle)
'2790470037120move_triangle'
>>> canvas.bind_all('<KeyPress-Down>', move_triangle)
'2790470037312move_triangle'
>>> canvas.bind_all('<KeyPress-Left>', move_triangle)
'2790470036992move_triangle'
>>> KeyboardInterrupt
>>> canvas.bind_all('<KeyPress-Right>', move_triangle)
'2790470098176move_triangle'
>>> canvas.bind_all('<KeyPress-1>', move_triangle)
'2790470098368move_triangle'
>>> canvas.bind_all('<KeyPress-7>', move_triangle)
'2790470098624move_triangle'
>>> canvas.bind_all('<KeyPress-9>', move_triangle)
'2790470098944move_triangle'
>>> canvas.bind_all('<KeyPress-3>', move_triangle)
'2790470099200move_triangle'
>>> canvas.itemconfig(my_triangle, fill='blue')
>>> canvas.itemconfig(my_triangle, outline='red')
