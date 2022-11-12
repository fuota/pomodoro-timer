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
LONG_BREAK_MIN = 15
reps=0
mark=""
timer=None


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1
    work_sec= WORK_MIN*60
    short_break_sec= SHORT_BREAK_MIN*60
    long_break_sec= LONG_BREAK_MIN*60

    if reps==8:
        countdown(long_break_sec)
        timer_label.config(text="Break", foreground=RED )
    elif reps%2==0:
        countdown(short_break_sec)
        timer_label.config(text="Break", foreground=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", foreground=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global mark
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer=window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps%2==0:
           mark+= "✔"
           check_mark.config(text=mark)

def reset():
    global timer_text
    global mark

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    mark=""






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 50, "bold"), foreground=GREEN)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
start.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, command=reset)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, background=YELLOW)
check_mark.grid(column=1, row=2)

window.mainloop()
