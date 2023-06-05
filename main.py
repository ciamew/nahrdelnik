import tkinter as tk
import random

w = 600
h = 500
# colours = ["pink", "yellow", "blue", "green"]
colours = ["black", "red", "orange", "gray"]
count = 10
size = 32
move_list = []
proces_list = []
max_beads = 0
bead_bfr = size

def setup():
    global move_list
    for i in range(40):
        x = random.randrange(0, w - size)
        y = random.randrange(0, h - size*3)
        move_list.append(canvas.create_oval(x, y, x + size, y + size, fill=colours[i//10]))
    # canvas.create_image(0, h - size-size//2, image=image, anchor=tk.NW)

def check_it(e):
    global proces_list, move_list, max_beads
    if max_beads >= 15: #maximalne 15 koralikov
        end_game()
        return
    zoz = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(zoz) != 0 and zoz[0] in move_list:
        if len(proces_list) == 0:
            proces_list.append(zoz[0])
            move_list.remove(zoz[0])
            max_beads += 1
            print("ideeeeeeeeeeeeeeee")
    move_it()

def move_it():
    global proces_list
    if len(proces_list) != 0:
        coord_ball = canvas.coords(proces_list[0])
        final_pos = (w-size//2,h-size//2)
        dx = w-coord_ball[2]
        dy = final_pos[1]-coord_ball[3]
        if dx>dy:
            dx = dx/dy
            dy = 1
        elif dx < dy:
            dy = dy / dx
            dx = 1
        canvas.move(proces_list[0],dx,dy)
        if coord_ball[2] == w:
            move_thread()
    canvas.after(10,move_it)

def move_thread():
    global proces_list, bead_bfr
    coord_ball = canvas.coords(proces_list[0])
    while coord_ball[0] > bead_bfr:
        canvas.move(proces_list[0], -1, 0)
        coord_ball = canvas.coords(proces_list[0])
        win.update()
    bead_bfr += size
    proces_list = []
    canvas.after(10,move_thread)

def end_game():
    canvas.create_text(w // 2,h // 2, text="THE END :(", font="Arial 12")

win = tk.Tk()

canvas = tk.Canvas(win,width=w,height=h,bg="white")
canvas.bind("<Button-1>", check_it)
canvas.pack()

thread = canvas.create_line(25,470,560,470)
canvas.create_oval(23,466,31,474,fill="black")
# image = tk.PhotoImage(file="img.png")

setup()

win.mainloop()
