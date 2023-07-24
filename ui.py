from tkinter import Tk , Label , Button , PhotoImage , Canvas
from constants import *
from math import floor

class Ui:
    def __init__(self) :
        self.reps = 0
        self.timer = None
        self.createUi()


    def start_handler(self):
        try:
            self.reset_handler()
        except Exception:
            pass
        
        self.reps += 1
        if(self.reps %8==0):
            self.count_down(LONG_BREAK_MIN *60)
            self.timer_label.config(text=BREAK)
        elif self.reps % 2 ==0:
            self.count_down(SHORT_BREAK_MIN*60)
            self.timer_label.config(text=BREAK,fg=PINK)
        else:
            self.count_down(WORK_MIN*60)
            self.timer_label.config(text=WORK)


    def reset_handler(self):
        self.wd.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text,text ="00:00")
        self.timer_label.config(text=TIMER)
        self.check_label.config(text="")
        self.reps = 0

    def createUi(self):
        self.wd = Tk(className = TITLE)
        self.wd.config(padx=100, pady=50, background=YELLOW)


        self.canvas = Canvas(width = 200, height =224,background=YELLOW,highlightthickness=0)
        self.tomato_img = PhotoImage(file = FILE_PATH)
        self.canvas.create_image(100, 112, image = self.tomato_img)
        self.timer_text = self.canvas.create_text(100, 130, text = STARTING_TIME, fill = WHITE, font = (FONT_NAME, FONT_SIZE, BOLD))

        self.canvas.grid(column=1,row=1)

        self.timer_label = Label(text=TIMER,font=(FONT_NAME,FONT_SIZE),fg=GREEN,background=YELLOW)
        self.timer_label.grid(row=0,column=1)
        self.check_label =Label(font=(FONT_NAME,FONT_SIZE),fg=GREEN,background=YELLOW)
        self.check_label.grid(row=3,column=1)
        self.start_btn = Button(text=START,command=self.start_handler)
        self.start_btn.grid(row=2,column=0)

        self.reset_btn = Button(text=RESET,command=self.reset_handler)
        self.reset_btn.grid(row=2,column=2)

        self.wd.mainloop()
    
    
    def count_down(self,count):
        count_min = floor(count/60)
        minutes = str(count_min) if count_min >=10 else f"0{count_min}"
        count_sec = count % 60
        seconds = str(count_sec) if count_sec >=10 else f"0{count_sec}"
        self.canvas.itemconfig(self.timer_text, text= f"{minutes}:{seconds}")
        if count >0:
          self.timer = self.wd.after(1000,self.count_down, count -1 )
        else:
            self.start_handler()
            mark = ""
            working_sessions = floor(self.reps/2)
            for _ in range(working_sessions):
                mark += CHECKMARK
            self.check_label.config(text=mark)