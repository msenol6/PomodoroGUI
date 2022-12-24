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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    check_label.config(text="")
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    print(reps)

    #If it's 8th reps:
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", foreground=RED, font=(FONT_NAME, 36, "bold"), bg=YELLOW)

    # If it's 2nd/4th/6th reps:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", foreground=PINK, font=(FONT_NAME, 36, "bold"), bg=YELLOW)
    #If it's 1st/3rd/5th/7th reps:
    else:
        count_down(work_sec)
        timer_label.config(text="Work Time", foreground=GREEN, font=(FONT_NAME, 36, "bold"), bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = "{:02d}".format(math.floor(count / 60))
    count_sec = "{:02d}".format(math.floor(count % 60))
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}" )
    if count>0:
        global timer
        timer = window.after(2, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += check_mark
        check_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=80 ,bg=YELLOW)
check_mark = "✔"


#LABELS:
timer_label = Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 36, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label(foreground=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
check_label.grid(column=1, row=3)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
canvas.grid(column=1, row=1)

#Buttons:
#calls action() when pressed
button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(column=2, row=2)

window.mainloop()
