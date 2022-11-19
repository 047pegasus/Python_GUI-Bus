from tkinter import *
from PIL import ImageTk, Image
from tkinter.messagebox import askokcancel, askyesnocancel, showinfo, WARNING, YES

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
    win.withdraw()
    newWin = Toplevel(win)
    newWin.title("Bus Ticketing M.S.")
    newWin.geometry("%dx%d" % (width, height))
    newWin.configure(bg="white")

    newframe = Frame(newWin, bg="white")

    Label(newframe, image=new_logo).pack(pady=(70, 0))
    Label(newframe, text="Online Bus Booking System", font=('Montserrat ExtraBold', 40), bg="LightBlue", fg="Red").pack(pady=25)

    def bus_book():
        newWin.withdraw()
        bookWin = Toplevel(newWin)
        bookWin.title("Bus Ticketing M.S.")
        bookWin.geometry("%dx%d" % (width, height))
        bookWin.configure(bg="white")
        bookframe = Frame(bookWin, bg="white")
        Label(bookframe, image=new_logo).pack(pady=(70, 0))
        Label(bookframe, text="Online Bus Booking System", font=('Montserrat ExtraBold', 40), bg="LightBlue", fg="Red").pack(pady=25)
        Label(bookframe, text="Enter Journey Details", font=('Montserrat', 30), bg="Light Green", fg="Green").pack(pady= (20, 20))
        Label(bookframe, text="To", font=('Montserrat', 20), bg="White", fg="Black").pack(side=LEFT)
        Entry(bookframe, width=30).pack(side=LEFT, padx=(10, 40))
        Label(bookframe, text="From", font=('Montserrat', 20), bg="White", fg="Black").pack(side=LEFT)
        Entry(bookframe, width=30).pack(side=LEFT, padx=(10, 40))
        Label(bookframe, text="Journey Date", font=('Montserrat', 20), bg="White", fg="Black").pack(side=LEFT)
        Entry(bookframe, width=30).pack(side=LEFT)

        def bookavailable_open():
            avbframe = Frame(bookWin, bg="white")
            Label(avbframe, text="Select Bus", bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT, padx=(0, 30))
            Label(avbframe, text="Operator", bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT, padx=(15, 30))
            Label(avbframe, text="Bus Type", bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT, padx=(15, 30))
            Label(avbframe, text="Available/Capacity", bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT,
                                                                                                        padx=(15, 30))
            Label(avbframe, text="Fare", bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT, padx=(15, 0))
            avbframe.pack()
            detailsframe = Frame(bookWin, bg="white")

            # Button(detailsframe).pack(side=LEFT)
            # Label(detailsframe).pack(side=LEFT)
            # Label(detailsframe).pack(side=LEFT)
            # Label(detailsframe).pack(side=LEFT)

            def psngdetails():
                entryframe = Frame(bookWin, bg="white")
                Label(entryframe, text="Fill Passenger Details to book the bus ticket", font=('Montserrat Bold', 30), bg="LightBlue", fg="Red").pack(pady=(20, 20))
                Label(entryframe, text="Name", bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT, padx=(0, 20))
                Entry(entryframe, width=20, bg="white").pack(side=LEFT, padx=(0, 10))
                Label(entryframe, text="Gender", bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT, padx=(15, 20))
                options = [
                    "Male",
                    "Female",
                    "Other",
                ]
                clicked = StringVar()
                clicked.set("Select Gender")
                OptionMenu(entryframe, clicked, *options).pack(side=LEFT, padx=(10, 20))
                Label(entryframe, text="No of Seats", bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT, padx=(15, 20))
                Entry(entryframe, width=10, bg="white").pack(side=LEFT, padx=(5, 20))
                Label(entryframe, text="Mobile No.", bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT, padx=(15, 20))
                Entry(entryframe, width=20, bg="white").pack(side=LEFT, padx=(5, 20))
                Label(entryframe, text="Age", bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT, padx=(15, 20))
                Entry(entryframe, width=10, bg="white").pack(side=LEFT, padx=(5, 20))

                def book_seatButton():
                    answer = askokcancel(
                        title="Fare Confirm",
                        message="Total amount to be paid will be:",
                        icon=WARNING
                    )
                    if answer:
                        bookWin.withdraw()
                        bookedWin = Toplevel(bookWin)
                        bookedWin.title("Bus Ticketing M.S.")
                        bookedWin.geometry("%dx%d" % (width, height))
                        bookedWin.configure(bg="white")
                        bookedframe = Frame(bookedWin, bg="white")
                        Label(bookedframe, image=new_logo).pack(pady=(70, 0))
                        Label(bookedframe, text="Online Bus Booking System", font=('Montserrat ExtraBold', 40), bg="LightBlue", fg="Red").pack(pady=25)
                        Label(bookedframe, text="Bus Ticket", font=('Montserrat Bold', 20), bg="white", fg="Black").pack()
                        bookedlabelFrame = LabelFrame(bookedWin, text="Ticket Details")

                        Label(bookedlabelFrame, text="Passengers:").pack()
                        Label(bookedlabelFrame, text="No of Seats:").pack()
                        Label(bookedlabelFrame, text="Age:").pack()
                        Label(bookedlabelFrame, text="Booking Reference ID:").pack()
                        Label(bookedlabelFrame, text="Travel on:").pack()
                        Label(bookedlabelFrame, text="No of seats:").pack()

                        Label(bookedlabelFrame, text="Gender:").pack()
                        Label(bookedlabelFrame, text="Phone:").pack()
                        Label(bookedlabelFrame, text="Fare:").pack()
                        Label(bookedlabelFrame, text="Bus Detail:").pack()
                        Label(bookedlabelFrame, text="Booked on:").pack()
                        Label(bookedlabelFrame, text="Boarding Point:").pack()

                        Label(bookedlabelFrame, text="* Total amount of Rs.1000.00/- will be paid at the time of boarding the bus.").pack()

                        bookedframe.pack()
                        bookedlabelFrame.pack()

                        showinfo(
                            title="Success Transaction",
                            message="Seat Booked"
                        )

                        def bookedWinclose_Handler():
                            answin= askyesnocancel(
                                title="Closing Confirmation",
                                message="For exiting press Yes or No to return to menu",
                                default=YES
                            )
                            if answin is True:
                                showinfo(
                                    title="Appreciation Message",
                                    message="Thank you for using my Bus Ticket Management system!!"
                                )
                                win.destroy()
                            elif answin is None:
                                print("Pressed Cancel!!")
                            else:
                                bookedWin.destroy()
                                newWin.deiconify()

                        bookedWin.protocol("WM_DELETE_WINDOW", bookedWinclose_Handler)
                Button(entryframe, text="Book Seat(s)", font=('Montserrat Medium', 15), cursor="hand2", fg="Black", bg="LightGreen", command=book_seatButton).pack(side=LEFT, padx=(20, 0))
                entryframe.pack()

            Button(avbframe, text="Proceed to Book", font=('Montserrat Medium', 15), bg="SeaGreen", fg="black", cursor="hand2", command=psngdetails).pack(side=LEFT, padx=(30, 0))
            detailsframe.pack()

        Button(bookframe, text="Show Bus", fg="Black", bg="Medium Sea Green", font=('Montserrat Bold', 20), activebackground="Green", activeforeground="white", cursor="hand2", command=bookavailable_open).pack(side=LEFT, padx=(10, 20))

        def mv_home():
            newWin.deiconify()

        Button(bookframe, image=home, cursor="hand2", command=mv_home).pack(side=LEFT)
        bookframe.pack()

    def check_book():
        newWin.withdraw()
        checkWin = Toplevel(newWin)
        checkWin.title("Bus Ticketing M.S.")
        checkWin.geometry("%dx%d" % (width, height))
        checkWin.configure(bg="white")

        checkheadframe = Frame(checkWin, bg="white")

        Label(checkheadframe, image=new_logo).pack(pady=(30, 0))
        Label(checkheadframe, text="Online Bus Booking System", font=('Montserrat ExtraBold', 30), bg="LightBlue", fg="Red").pack(pady=15)

        Label(checkheadframe, text="Check Your Booking", font=('Montserrat Bold', 20), bg="Sea Green", fg="White").pack(pady=10)
        Label(checkheadframe, text="Enter your Mobile No: ", font=('Montserrat Medium', 15), bg="white", fg="black").pack(side=LEFT, padx=(0, 30), pady=10)
        Entry(checkheadframe, width=25, bg="white").pack(side=LEFT, padx=(10, 30), pady=10)

        def chk_bk():
            chkbklabelFrame = LabelFrame(checkWin, text="Ticket Details")

            Label(chkbklabelFrame, text="Passengers:").pack()
            Label(chkbklabelFrame, text="No of Seats:").pack()
            Label(chkbklabelFrame, text="Age:").pack()
            Label(chkbklabelFrame, text="Booking Reference ID:").pack()
            Label(chkbklabelFrame, text="Travel on:").pack()

            Label(chkbklabelFrame, text="Gender:").pack()
            Label(chkbklabelFrame, text="Phone:").pack()
            Label(chkbklabelFrame, text="Fare:").pack()
            #Label(chkbklabelFrame, text="Bus Detail:").pack()
            #Label(chkbklabelFrame, text="Booked on:").pack()
            Label(chkbklabelFrame, text="Boarding Point:").pack()
            Label(chkbklabelFrame, text="Destination Point:").pack()

            Label(chkbklabelFrame, text="* Total amount of Rs./- will be paid at the time of boarding the bus.").pack()

            chkbklabelFrame.pack()

        Button(checkheadframe, text="Check Booking", font=('Montserrat Medium', 15), bg="White", fg="Black", command=chk_bk, cursor="hand2").pack(side=LEFT, padx=(10, 0), pady=10)

        checkheadframe.pack()

    def admin_ms():
        newWin.withdraw()
        adminWin = Toplevel(newWin)
        adminWin.title("Bus Ticketing M.S.")
        adminWin.geometry("%dx%d" % (width, height))
        adminWin.configure(bg="white")

        adminframe = Frame(adminWin, bg="white")

        Label(adminframe, image=new_logo).pack(pady=(30, 0))
        Label(adminframe, text="Online Bus Booking System", font=('Montserrat ExtraBold', 30), bg="LightBlue", fg="Red").pack(pady=15)
        Label(adminframe, text="Add New Bus Details to Database", font=('Montserrat Bold', 30), bg="White", fg="SpringGreen2").pack(pady=20)

        def new_opr():
            adminWin.withdraw()
            newoprWin = Toplevel(adminWin)
            newoprWin.title("Bus Ticketing M.S.")
            newoprWin.geometry("%dx%d" % (width, height))
            newoprWin.configure(bg="white")

            newoprframe = Frame(newoprWin, bg="white")

            Label(newoprframe, image=new_logo).pack(pady=(30, 0))
            Label(newoprframe, text="Online Bus Booking System", font=('Montserrat ExtraBold', 30), bg="LightBlue", fg="Red").pack(pady=15)

            Label(newoprframe, text="Add Bus Operator Details", font=('Montserrat Bold', 30), bg="White", fg="Lime Green").pack(pady=20)

            Label(newoprframe, text="Operator ID", font=('Montserrat Bold', 15), bg="White", fg="Black").pack(side=LEFT, pady=20)
            oprentry=Entry(newoprframe, width=15)
            oprentry.pack(side=LEFT, pady=20, padx=5)
            Label(newoprframe, text="Name", font=('Montserrat Bold', 15), bg="White", fg="Black").pack(side=LEFT, pady=20, padx=5)
            nameentry=Entry(newoprframe, width=25)
            nameentry.pack(side=LEFT, pady=20, padx=5)
            Label(newoprframe, text="Address", font=('Montserrat Bold', 15), bg="White", fg="Black").pack(side=LEFT, pady=20, padx=5)
            addressentry=Entry(newoprframe, width=35)
            addressentry.pack(side=LEFT, pady=20, padx=5)
            Label(newoprframe, text="Phone", font=('Montserrat Bold', 15), bg="White", fg="Black").pack(side=LEFT, pady=20, padx=5)
            phoneentry=Entry(newoprframe, width=25)
            phoneentry.pack(side=LEFT, pady=20, padx=5)
            Label(newoprframe, text="Email", font=('Montserrat Bold', 15), bg="White", fg="Black").pack(side=LEFT, pady=20, padx=5)
            emailentry=Entry(newoprframe, width=25)
            emailentry.pack(side=LEFT, pady=20, padx=5)

            def updateopr():
                showinfo(
                    title="Operator Entry Update",
                    message="Operator Record updated successfully"
                )
                oprentry.delete(0, END)
                nameentry.delete(0, END)
                addressentry.delete(0, END)
                phoneentry.delete(0, END)
                emailentry.delete(0, END)

            Button(newoprframe, text="Add", font=('Montserrat Medium', 20), bg="Lime Green", fg="Black", cursor="hand2").pack(side=LEFT, pady=20, padx=(10, 10))
            Button(newoprframe, text="Edit", font=('Montserrat Medium', 20), bg="Lime Green", fg="Black", cursor="hand2", command=updateopr).pack(side=LEFT, pady=20, padx=(10, 10))

            def mv_home():
                newWin.deiconify()
            Button(newoprframe, image=home, cursor="hand2",command= mv_home).pack(side=LEFT, pady=20)

            newoprframe.pack()

        #def new_bus():

        Button(adminframe, text="New Operator", font=('Montserrat Medium', 25), bg="lawn green", fg="Black", border=3, command=new_opr, cursor="hand2").pack(side=LEFT, padx=(0, 50), pady=40)
        Button(adminframe, text="New Bus", font=('Montserrat Medium', 25), bg="orange red", fg="Black", border=3, command="new_bus", cursor="hand2").pack(side=LEFT, padx=(50, 50), pady=40)
        Button(adminframe, text="New Route", font=('Montserrat Medium', 25), bg="SlateBlue2", fg="Black", border=3, command="new_route", cursor="hand2").pack(side=LEFT, padx=(50, 50), pady=40)
        Button(adminframe, text="New Run", font=('Montserrat Medium', 25), bg="DarkOrchid2", fg="Black", border=3, command="new_run", cursor="hand2").pack(side=LEFT, padx=(50, 0), pady=40)

        adminframe.pack()

    Button(newframe, text="Seat Booking", font=('Montserrat SemiBold', 23), bg="LightGreen", fg="Black", activebackground="SeaGreen", activeforeground="white", cursor="hand2", command=bus_book).pack(side=LEFT, padx=70, pady=(50, 0))
    Button(newframe, text="Checked Booked Seat", font=('Montserrat SemiBold', 23), bg="LightGreen", fg="Black", activebackground="SeaGreen", activeforeground="white", cursor="hand2", command=check_book).pack(side=LEFT, padx=70, pady=(50, 0))
    Button(newframe, text="Add Bus Details", font=('Montserrat SemiBold', 23), bg="Light Green", fg="Black", activebackground="Green", activeforeground="white", cursor="hand2", command=admin_ms).pack(side=LEFT, padx=70, pady=(50, 0))

    newframe.pack()

    tagframe = Frame(newWin, bg="white")
    Label(tagframe, text="For Admins ONLY!!", font=('Montserrat Medium', 15), fg="red", bg="white").pack(padx=(900, 0), pady=(30, 0))
    tagframe.pack()


win.bind("<Key>", keypress)
win.mainloop()  # Start main eventloop
'''def main():'''
