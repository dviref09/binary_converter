from tkinter.constants import END
import bin_interpreter as bin
import tkinter

app = tkinter.Tk()
app.title('Mode select')

app.geometry("500x500+650+200")
def bin_to_number():
    lbl = tkinter.Label(app, text ="Please enter binary code").pack(pady=25)
    enter = tkinter.Entry(app).pack(pady=0)
    button2 = tkinter.Button(app, text="Convert", command=run).pack()
    return enter

def run():
    enter = bin_to_number()
    enterget = enter.get()

lbl = tkinter.Label(app, text="Please select mode:").pack(pady=25)

button1 = tkinter.Button(app, text="Binary to number", command=bin_to_number).pack()

lbl2 = tkinter.Label(app).pack()

app.mainloop()
