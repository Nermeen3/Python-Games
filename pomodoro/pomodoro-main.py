import tkinter
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
check_icon = ""
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    global reps
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    labelCheck.config(text="", fg=RED)
    labelTimer.config(text="Timer", fg=GREEN)
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global check_icon
    if reps < 7:
        if reps % 2 == 0:
            labelTimer.config(text=f"You are in working time", fg=GREEN)
            count_down(WORK_MIN)
        else:
            labelTimer.config(text=f"You are in a short break", fg=PINK)
            count_down(SHORT_BREAK_MIN)
        reps += 1
    elif reps == 7:
        labelTimer.config(text=f"You are in a long break", fg=RED)
        count_down(LONG_BREAK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(time):
    global check_icon
    global TIMER
    minutes = math.floor(time / 60)
    seconds = time % 60

    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if time > 0:
        TIMER = window.after(1000, count_down, time - 1)
    else:
        if reps % 2 and reps > 0:
            check_icon += "✓"
            labelCheck.config(text=f"{check_icon}", fg=RED)

        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pamodoro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=500, height=400, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(250, 200, image=img)
timer_text = canvas.create_text(250, 225, text="00:00", font=(FONT_NAME, 35, 'bold'), fill="white")
canvas.grid(column=1, row=1)

labelTimer = Label(text="Timer", font=(FONT_NAME, 40, ''), bg=YELLOW, fg=GREEN)
labelTimer.grid(column=1, row=0)

buttonStart = Button(text="Start", font=(FONT_NAME, 20, ''), fg=PINK, highlightthickness=0, command=start_timer)
buttonStart.grid(column=0, row=2)

labelCheck = Label(font=(FONT_NAME, 40, ''), bg=YELLOW, fg=GREEN)
labelCheck.grid(column=1, row=2)

buttonReset = Button(text="Reset", font=(FONT_NAME, 20, ''), fg=PINK, highlightthickness=0, command=reset_time)
buttonReset.grid(column=2, row=2)

window.mainloop()
