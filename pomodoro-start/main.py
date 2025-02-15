from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = '#189AC7'
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_id,text="00:00")
    check_marks.config(text="")
    Timer_lable.config(text="Timer",fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    work_secs = WORK_MIN*60
    short_break_secs = SHORT_BREAK_MIN*60
    long_break_secs = LONG_BREAK_MIN*60

    if reps%8==0:
        Timer_lable.config(text="Long-Break",fg=RED)
        countdown(long_break_secs)
    elif reps%2 == 0:
        Timer_lable.config(text="Short-Break",fg=BLUE)
        countdown(short_break_secs)
    else:
        Timer_lable.config(text="Work",fg=GREEN)
        countdown(work_secs)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    mins,secs=divmod(count,60)
    if secs<10:
        secs=f"0{secs}"
    if mins <10:
        mins = f"0{mins}"
    canvas.itemconfig(timer_id,text=f"{mins}:{secs}")
    if count>0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        start_timer()
        marks=""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
Timer_lable = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
Timer_lable.grid(row=1,column=2)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
photo=PhotoImage(file=r"pomodoro-start\tomato.png")
canvas.create_image(100,112,image=photo)
timer_id=canvas.create_text(100,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)

start_button =Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=3,column=1)
reset_button =Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=3,column=3)

check_marks=Label(text="",fg=GREEN,bg=YELLOW)
check_marks.grid(row=3,column=2)


window.mainloop()