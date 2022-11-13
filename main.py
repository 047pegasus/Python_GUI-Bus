from tkinter import *
from PIL import ImageTk, Image

win = Tk()
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry("%dx%d" % (width, height))
win.configure(bg="white")
win.title("Bus Ticket Management System")

frame = Frame(win, bg="white")
img = (Image.open("bus.jpg"))
resized_logo = img.resize((300, 300), Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized_logo)
Label(frame, image=new_logo).pack(pady=(70, 0))
Label(frame, text="Online Bus Booking System", font=('Montserrat ExtraBold', 40), bg="LightBlue", fg="Red").pack(pady=25)

Label(frame, text="Name: Tanishq Agarwal", font=('Montserrat ExtraBold', 20), fg="Blue", bg="white").pack(pady=(50, 25))
Label(frame, text="Enrollment: 211B326", font=('Montserrat ExtraBold', 20), fg="Blue", bg="white").pack(pady=25)
Label(frame, text="Mobile: 9984429317", font=('Montserrat ExtraBold', 20), fg="Blue", bg="white").pack(pady=(25, 0))

frame.pack()

footer = Label(frame, text="Submitted to: Dr. Mahesh Kumar", font=('Montserrat SemiBold', 25), bg="LightBlue", fg="Red")
footer.pack(padx=(0, 0), pady=(100, 0))
footer1 = Label(frame, text="Project Based Learning", font=('Montserrat Medium', 20), fg="Red")
footer1.pack(padx=(0, 0), pady=(0, 0))


def keypress(event):
    win.iconify()
    newWin = Toplevel(win)
    newWin.title("Bus Ticketing M.S.")
    newWin.geometry("%dx%d" % (width, height))
    newWin.configure(bg="white")

    newframe = Frame(newWin, bg="white")

    Label(newframe, image=new_logo).pack(pady=(70, 0))
    Label(newframe, text="Online Bus Booking System", font=('Montserrat ExtraBold', 40), bg="LightBlue", fg="Red").pack(pady=25)

    def book_bus():
        newWin.iconify()
        bookWin = Toplevel(newWin)
        bookWin.title("Bus Ticketing M.S.")
        bookWin.geometry("%dx%d" % (width, height))
        bookWin.configure(bg="white")

        bookframe= Frame(bookWin, bg="white")

        Label(bookframe, image=new_logo).pack(pady=(70, 0))
        Label(bookframe, text="Online Bus Booking System", font=('Montserrat ExtraBold', 40), bg="LightBlue",fg="Red").pack(pady=25)
        Label(bookframe, text="Enter Journey Details", font=('Montserrat', 30), bg="Light Green", fg="Green").pack(pady=(20,20))

        Label(bookframe, text="To", font=('Montserrat', 20), bg="White", fg="Black").pack(side=LEFT)
        Entry(bookframe)
        Label(bookframe, text="From", font=('Montserrat', 20), bg="White", fg="Black").pack(side=LEFT)
        Entry(bookframe)
        Label(bookframe, text="Journey Date", font=('Montserrat', 20), bg="White", fg="Black").pack(side=LEFT)
        Entry(bookframe)
        Button(bookframe, text="Show Bus",fg="Black", bg="Light Green", font=('Montserrat', 20), activebackground="Green", activeforeground="white", cursor="hand2")
        #Button(bookframe, text="Show Bus", image=("Home.jpg"), cursor="hand2")

    Button(newframe, text="Seat Booking", font=('Montserrat SemiBold', 23), bg="LightGreen", fg="Black", activebackground="SeaGreen", activeforeground="white", cursor="hand2", command="book_bus").pack(side=LEFT, padx=70, pady=(50, 0))
    Button(newframe, text="Checked Booked Seat", font=('Montserrat SemiBold', 23), bg="LightGreen", fg="Black", activebackground="SeaGreen", activeforeground="white", cursor="hand2", command="check").pack(side=LEFT, padx=70, pady=(50, 0))
    Button(newframe, text="Add Bus Details", font=('Montserrat SemiBold', 23), bg="Light Green", fg="Black", activebackground="Green", activeforeground="white", cursor="hand2", command="add_bus").pack(side=LEFT, padx=70, pady=(50, 0))

    newframe.pack()

    tagframe = Frame(newWin, bg="white")

    Label(tagframe, text="For Admins ONLY!!", font=('Montserrat Medium', 15), fg="red", bg="white").pack(padx=(900,0), pady=(30,0))

    tagframe.pack()

win.bind("<Key>", keypress)
win.mainloop()  # Start main eventloop
'''def main():'''
