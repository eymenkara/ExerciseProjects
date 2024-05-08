from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    reps = 1
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in (1, 3, 5, 7):
        label.config(text="WORK", fg=GREEN)
        countdown(work_sec)
    elif reps == 8:
        label.config(text="BREAK", fg=PINK)
        countdown(long_break_sec)
    elif reps in (2, 4, 6):
        label.config(text="BREAK", fg=PINK)
        countdown(short_break_sec)
    else:
        label.config(text="DONE", fg=RED)
        print("What the rep?!")

    # rep 1-3-5-7 work
    # rep 8 long
    # rep 2-4-6 short


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps, timer
    rem_min = int(count / 60)
    rem_sec = count % 60

    if rem_sec < 10:
        rem_sec = f"0{rem_sec}"

    canvas.itemconfig(timer_text, text=f"{rem_min}:{rem_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        reps += 1
        checks = "✔" * int(reps/2)
        checkmark.config(text=checks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.config(width=5, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset")
reset_button.config(width=5, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark = Label(text="", bg=YELLOW, fg=GREEN)
checkmark.grid(row=3, column=1)

window.mainloop()
