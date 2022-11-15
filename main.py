from tkinter import *
from PIL import ImageTk, Image

win = Tk()
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry("%dx%d" % (width, height))
win.configure(bg="white")
win.title("Bus Ticket Management System")

frame = Frame(win, bg="white")
img = (Image.open("./bus.jpg"))
resized_logo = img.resize((400, 300), Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized_logo)

homeimg = (Image.open("./home.png"))
home = ImageTk.PhotoImage(homeimg)

Label(frame, image=new_logo).pack(pady=10)
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

    def bus_book():
        newWin.iconify()
        bookWin = Toplevel(newWin)
        bookWin.title("Bus Ticketing M.S.")
        bookWin.geometry("%dx%d" % (width, height))
        bookWin.configure(bg="white")
        bookframe = Frame(bookWin, bg="white")
        Label(bookframe, image=new_logo).pack(pady=(70, 0))
        Label(bookframe, text="Online Bus Booking System", font=('Montserrat ExtraBold', 40), bg="LightBlue", fg="Red").pack(pady=25)
        Label(bookframe, text="Enter Journey Details", font=('Montserrat', 30), bg="Light Green", fg="Green").pack(pady=(20, 20))
        Label(bookframe, text="To", font=('Montserrat', 20), bg="White", fg="Black").pack(side=LEFT)
        Entry(bookframe, width=30).pack(side=LEFT, padx=(10, 40))
        Label(bookframe, text="From", font=('Montserrat', 20), bg="White", fg="Black").pack(side=LEFT)
        Entry(bookframe, width=30).pack(side=LEFT, padx=(10, 40))
        Label(bookframe, text="Journey Date", font=('Montserrat', 20), bg="White", fg="Black").pack(side=LEFT)
        Entry(bookframe, width=30).pack(side=LEFT)

        def bookavailable_open():
            avbframe = Frame(bookWin, bg="white")
            Label(avbframe, text="Select Bus").pack(side=LEFT)
            Label(avbframe, text="Operator").pack(side=LEFT)
            Label(avbframe, text="Bus Type").pack(side=LEFT)
            Label(avbframe, text="Available/Capacity").pack(side=LEFT)
            Label(avbframe, text="Fare").pack(side=LEFT)
            avbframe.pack()
            detailsframe = Frame(bookWin, bg="white")
            Button(detailsframe).pack(side=LEFT)
            Label(detailsframe).pack(side=LEFT)
            Label(detailsframe).pack(side=LEFT)
            Label(detailsframe).pack(side=LEFT)

            def psngdetails():
                entryframe = Frame(bookWin, bg="white")
                Label(entryframe, text="Fill Passenger Details to book the bus ticket", font=('Montserrat Bold', 30), bg="LightBlue", fg="Red").pack()
                Label(entryframe, text="Name").pack(side=LEFT)
                Entry(entryframe, width=20).pack(side=LEFT)
                Label(entryframe, text="Gender").pack(side=LEFT)
                options = [
                    "Male"
                    "Female"
                    "Other"
                ]
                clicked = StringVar()
                clicked.set("Select Gender")
                OptionMenu(entryframe, clicked, *options).pack(side=LEFT)
                Label(entryframe, text="No of Seats").pack(side=LEFT)
                Entry(entryframe, width=10).pack(side=LEFT)
                Label(entryframe, text="Mobile No.").pack(side=LEFT)
                Entry(entryframe, width=20).pack(side=LEFT)
                Label(entryframe, text="Age").pack(side=LEFT)
                Entry(entryframe, width=10).pack(side=LEFT)
                Button(entryframe, text="Book Seat(s)", cursor="hand2", fg="Black", bg="LightGreen").pack(side=LEFT)
                entryframe.pack()

            Button(detailsframe, text="Proceed to Book", bg="SeaGreen", fg="black", cursor="hand2", command=psngdetails).pack(side=LEFT)
            detailsframe.pack()

        Button(bookframe, text="Show Bus", fg="Black", bg="Medium Sea Green", font=('Montserrat Bold', 20), activebackground="Green", activeforeground="white", cursor="hand2", command=bookavailable_open).pack(side=LEFT, padx=(10, 20))
        Button(bookframe, image=home, cursor="hand2").pack(side=LEFT)
        bookframe.pack()

    #def check():

    #def add_bus():

    Button(newframe, text="Seat Booking", font=('Montserrat SemiBold', 23), bg="LightGreen", fg="Black", activebackground="SeaGreen", activeforeground="white", cursor="hand2", command=bus_book).pack(side=LEFT, padx=70, pady=(50, 0))
    Button(newframe, text="Checked Booked Seat", font=('Montserrat SemiBold', 23), bg="LightGreen", fg="Black", activebackground="SeaGreen", activeforeground="white", cursor="hand2", command="check").pack(side=LEFT, padx=70, pady=(50, 0))
    Button(newframe, text="Add Bus Details", font=('Montserrat SemiBold', 23), bg="Light Green", fg="Black", activebackground="Green", activeforeground="white", cursor="hand2", command="add_bus").pack(side=LEFT, padx=70, pady=(50, 0))

    newframe.pack()

    tagframe = Frame(newWin, bg="white")

    Label(tagframe, text="For Admins ONLY!!", font=('Montserrat Medium', 15), fg="red", bg="white").pack(padx=(900,0), pady=(30,0))

    tagframe.pack()

win.bind("<Key>", keypress)
win.mainloop()  # Start main eventloop
'''def main():'''
