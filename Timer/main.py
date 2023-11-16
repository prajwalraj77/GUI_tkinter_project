
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer
    global rep
    window.after_cancel(timer)
    timer_name.config(text="TIMER")
    canv.itemconfig(timer_txt, text=f"00:00")
    check_box.config(text="")
    rep=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_action():
    global  rep
    rep +=1
    work_sec=WORK_MIN*60
    short_brake_sec=SHORT_BREAK_MIN*50
    long_brake_sec=LONG_BREAK_MIN*60
    if rep %8==0:
        timer_name.config(text="LONG BRAKE" ,fg=RED)
        count_down(long_brake_sec)
    elif rep %2 ==0:
        timer_name.config(text="Short BRAKE", fg=PINK)
        count_down(short_brake_sec)
    else:
        timer_name.config(text="WORK", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(time):
    count_min= math.floor(time/60)
    count_sec=time%60
    if count_sec <10:
        count_sec=f"0{count_sec}"

    canv.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if time > 0:
        global timer
        timer=  window.after(1000, count_down, time-1)
    else:
        start_action()
        mark=""
        work_session=math.floor(rep/2)
        if i in work_session:
            mark+="✔"
        check_box.config(mark)
# ---------------------------- UI SETUP ------------------------------- #


window= Tk()
window.title("THIS IS A TIMER")
window.config(padx=100,pady=50 ,bg=YELLOW)

tomato_img=PhotoImage(file="tomato.png")
canv=Canvas(width=250,height=250 ,bg=YELLOW ,highlightthickness=0 )
canv.create_image(103,125, image=tomato_img)

timer_txt=canv.create_text(100,125, text="00:00" ,font=(FONT_NAME,35,"bold") ,fill="green")
canv.grid(column=1,row=1)


timer_name = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), fg=PINK, bg=YELLOW,)
timer_name.grid(column=1,row=0)

start_button=Button(text="START",font=(FONT_NAME, 10, "bold"), highlightthickness=0 ,command=start_action)
start_button.grid(column=0,row=2)

reset_button=Button(text="RESET",font=(FONT_NAME, 10, "bold"),highlightthickness=0 ,command=reset)
reset_button.grid(column=2,row=2)

check_box=Label(font=(FONT_NAME, 10, "bold") ,fg="green",bg=YELLOW)
check_box.grid(row=3,column=1)




window.mainloop()
