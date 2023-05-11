from tkinter import *
import datetime
from tkinter.messagebox import *
from tkinter.ttk import *
from playsound import playsound


window = Tk()
window.title("Alarm clock by sammiie.com")
window.config(padx=20, pady=50, bg='#2C3639')
window.geometry("500x300")

# ************************************* function that set the alarm and trigger the alarm tone ***********************************


def alarm():
    if not period.get():    # Check if a value has been selected for AM or PM
        showerror("Error", "Kindly indicate if it's AM or PM")
    else:
        try:
            if period.get() == "AM":
                alarm_hour = int(hour_entry.get())
                alarm_minute = int(minute_entry.get())
            if period.get() == "PM":
                alarm_hour = int(hour_entry.get())+12
                alarm_minute = int(minute_entry.get())
        except ValueError:
            showinfo("info", "Invalid time entered!")
        else:
            showinfo("notification", "alarm has been set")

            while True:
                if alarm_hour == datetime.datetime.now().hour and alarm_minute == datetime.datetime.now().minute:
                    playsound('audio.mp3')
                    # for _ in range(0, 100):
                    #     winsound.Beep(1000, 100)
                    break

# **************************************** USER INTERFACE DESIGN ****************************************************************


hour_label = Label(window, text = "HOURS:", font=("Courier", 15, "bold"))
minute_label = Label(window, text= "MINUTES:", font=("Courier", 15, "bold"))

hour_label.grid(row=0, column=0)
minute_label.grid(row=0, column=2, padx=10)

hour_entry = Entry(window)
minute_entry = Entry(window)

hour_entry.grid(row=0, column=1, padx=10)
minute_entry.grid(row=0, column=3)

period_label = Label(window,text="AM OR PM:", font=("Courier", 9, "bold"))
period_label.place(relx=0.25,rely=0.31)
period = Combobox(window, values=["AM", "PM"])
period.place(relx=0.42, rely=0.3)

set_btn = Button(window, text="Set Alarm", command=alarm)
set_btn.place(relx=0.4, rely=0.5)


mainloop()
