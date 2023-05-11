from tkinter import *



# ----------------------------------------------------GUI Design----------------------------------------------------------------

window = Tk()
window.title("Flash Card App")
window.config(padx=20, pady=20, bg="#13e27a")


canvas = Canvas(width=800, height=526, bg="#13e27a")
canvas.grid(row=0, column=0, columnspan=2, pady=50)
# --------------------------Images----------------------------------

yes_image = PhotoImage(file="./yes.png")
no_image = PhotoImage(file="./no.png")




# ------------------Buttons----------------------------------

btn_wrong = Button(image=no_image,  width=100, height=100, highlightthickness=0)
btn_wrong.grid(row=1, column=0)
btn_right = Button(image=yes_image, width=100, height=100, highlightthickness=0)
btn_right.grid(row=1, column=1)



mainloop()