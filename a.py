import tkinter

app = tkinter.Tk()
app.title('hello')
app.geometry("300x300+650+200")

lbl = tkinter.Label(app, text="לא לגעת", font="144").pack(pady=75)

app.mainloop()