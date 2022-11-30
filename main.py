from tkinter import *
from PIL import ImageTk, Image
from tkinter.messagebox import askokcancel, askyesnocancel, showinfo, WARNING, YES
import sqlite3

dbcon = sqlite3.connect("BUS MS")
cursor = dbcon.execute("SELECT * FROM bus")
bus_fetch = cursor.fetchall()

cursor = dbcon.execute("SELECT * FROM city")
city_fetch = cursor.fetchall()

cursor = dbcon.execute("SELECT * FROM operator")
operator_fetch = cursor.fetchall()

cursor = dbcon.execute("SELECT * FROM passenger")
passenger_fetch = cursor.fetchall()

cursor = dbcon.execute("SELECT * FROM payment")
payment_fetch = cursor.fetchall()

cursor = dbcon.execute("SELECT * FROM route")
route_fetch = cursor.fetchall()

cursor = dbcon.execute("SELECT * FROM runs")
runs_fetch = cursor.fetchall()

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
        Label(bookframe, image=new_logo).pack(pady=(40, 0))
        Label(bookframe, text="Online Bus Booking System", font=('Montserrat ExtraBold', 30), bg="LightBlue", fg="Red").pack(pady=25)
        Label(bookframe, text="Enter Journey Details", font=('Montserrat', 20), bg="Light Green", fg="Green").pack(pady=(10, 20))
        Label(bookframe, text="To", font=('Montserrat', 15), bg="White", fg="Black").pack(side=LEFT)
        to = Entry(bookframe, width=30)
        to.pack(side=LEFT, padx=(10, 40))
        Label(bookframe, text="From", font=('Montserrat', 20), bg="White", fg="Black").pack(side=LEFT)
        frm = Entry(bookframe, width=30)
        frm.pack(side=LEFT, padx=(10, 40))
        Label(bookframe, text="Journey Date", font=('Montserrat', 20), bg="White", fg="Black").pack(side=LEFT)
        jdate = Entry(bookframe, width=30)
        jdate.pack(side=LEFT)

        def bookavailable_open():
            dbcon = sqlite3.connect("BUS MS")
            cursor = dbcon.execute("""SELECT opr.name,bus.type,bus.capacity,runs.available,runs.fare FROM operator as opr,bus,runs,route where route.destination="{}" and route.origin="{}" and runs.date="{}" and bus.busid=runs.busid and route.rid=runs.routeid;""".format(to.get(), frm.get(), jdate.get()))
            query_fetch_one = (cursor.fetchall())
            print(query_fetch_one)
            count = len(query_fetch_one)
            print(count)

            avbframe = Frame(bookWin, bg="white", pady=25)
            Label(avbframe, text="Select Bus", bg="white", font=('Montserrat Bold', 15)).pack(side=LEFT, padx=(0, 90))
            Label(avbframe, text="Operator", bg="white", font=('Montserrat Bold', 15)).pack(side=LEFT, padx=(90, 90))
            Label(avbframe, text="Bus Type", bg="white", font=('Montserrat Bold', 15)).pack(side=LEFT, padx=(90, 90))
            Label(avbframe, text="Available/Capacity", bg="white", font=('Montserrat Bold', 15)).pack(side=LEFT, padx=(90, 90))
            Label(avbframe, text="Fare", bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT, padx=(90, 0))
            avbframe.pack()

            detailsframe = Frame(bookWin, bg="white")

            #radvar = IntVar(detailsframe, 1)
            for i in range(count):
                #Radiobutton(detailsframe, text="Bus 1", variable=radvar, value="1", bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT, padx=(150, 200))
                Label(detailsframe, text=query_fetch_one[i][0], bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT)
                Label(detailsframe, text=query_fetch_one[i][1], bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT)
                Label(detailsframe, text="{}/{}".format(query_fetch_one[i][2],query_fetch_one[i][3]), bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT)
                Label(detailsframe, text=query_fetch_one[i][4], bg="white", font=('Montserrat Medium', 15)).pack(side=LEFT)

            def psngdetails():
                entryframe = Frame(bookWin, bg="white")
                Label(entryframe, text="Fill Passenger Details to book the bus ticket", font=('Montserrat Bold', 20), bg="LightBlue", fg="Red").pack(pady=(20, 20))
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
                dbcon.close()

            Button(avbframe, text="Proceed to Book", font=('Montserrat Medium', 15), bg="SeaGreen", fg="White", cursor="hand2", command=psngdetails).pack(side=LEFT, padx=(90, 0))
            detailsframe.pack()


        Button(bookframe, text="Show Bus", fg="Black", bg="Medium Sea Green", font=('Montserrat Bold', 20), activebackground="Green", activeforeground="white", cursor="hand2", command=bookavailable_open).pack(side=LEFT, padx=(10, 20))

        def mv_home():
            bookWin.destroy()
            newWin.deiconify()

        Button(bookframe, image=home, cursor="hand2", command=mv_home).pack(side=LEFT)

        def bookWinclose_Handler():
            ansuser = askokcancel(
                title="Closing Confirmation",
                message="For exiting press Yes or No to return to menu",
            )
            if ansuser is True:
                win.destroy()
            else:
                print("User selected cancel")

        bookWin.protocol("WM_DELETE_WINDOW", bookWinclose_Handler)
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
        chk_mob_entry = Entry(checkheadframe, width=25, bg="white")
        chk_mob_entry.pack(side=LEFT, padx=(10, 30), pady=10)

        def chk_bk():
            dbcon = sqlite3.connect("BUS MS")
            cursor = dbcon.execute("""SELECT DISTINCT p.name, p.contact, p.gender, p.age, pay.no_of_seats, pay. payid, pay.amount, rt.destination, rt.origin, run.date FROM passenger as p, payment as pay, route as rt, runs as run where p.contact="{}" AND p.id=pay.passid AND pay.payed_route=rt.rid AND rt.rid=run.routeid;""".format(chk_mob_entry.get()))
            query_fetch_two = (cursor.fetchall())
            print(query_fetch_two)

            chkbklabelFrame = LabelFrame(checkWin, text="Ticket Details")

            Label(chkbklabelFrame, text="Passengers: {}".format(query_fetch_two[0][0])).pack()
            Label(chkbklabelFrame, text="No of Seats: {}".format(query_fetch_two[0][4])).pack()
            Label(chkbklabelFrame, text="Age: {}".format(query_fetch_two[0][3])).pack()
            Label(chkbklabelFrame, text="Booking Reference ID: {}".format(query_fetch_two[0][5])).pack()
            Label(chkbklabelFrame, text="Travel on: {}".format(query_fetch_two[0][9])).pack()

            Label(chkbklabelFrame, text="Gender: {}".format(query_fetch_two[0][2])).pack()
            Label(chkbklabelFrame, text="Phone: {}".format(query_fetch_two[0][1])).pack()
            Label(chkbklabelFrame, text="Fare: {}".format(query_fetch_two[0][6])).pack()
            #Label(chkbklabelFrame, text="Bus Detail:").pack()
            #Label(chkbklabelFrame, text="Booked on:").pack()
            Label(chkbklabelFrame, text="Boarding Point: {}".format(query_fetch_two[0][8])).pack()
            Label(chkbklabelFrame, text="Destination Point: {}".format(query_fetch_two[0][7])).pack()

            Label(chkbklabelFrame, text="* Total amount of Rs.{}/- will be paid at the time of boarding the bus.".format(query_fetch_two[0][4]*1000)).pack()

            chkbklabelFrame.pack()
            dbcon.close()
        Button(checkheadframe, text="Check Booking", font=('Montserrat Medium', 15), bg="White", fg="Black", command=chk_bk, cursor="hand2").pack(side=LEFT, padx=(10, 0), pady=10)

        def checkWinclose_Handler():
            ansuser = askokcancel(
                title="Closing Confirmation",
                message="For exiting press Yes or No to return to menu",
            )
            if ansuser is True:
                win.destroy()
            else:
                print("User selected cancel")

        checkWin.protocol("WM_DELETE_WINDOW", checkWinclose_Handler)
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

            def addopr():
                dbcon = sqlite3.connect("BUS MS")
                cursor = dbcon.execute("""INSERT INTO operator VALUES({},"{}","{}","{}","{}");""".format(int(oprentry.get()), nameentry.get(), phoneentry.get(), addressentry.get(), emailentry.get()))
                #cursor = dbcon.execute("SELECT * FROM operator;")
                dbcon.commit()
                print(cursor.fetchall())
                dbcon.close()

                showinfo(
                    title="Operator Entry Added",
                    message="Operator Record added successfully!!"
                )

                oprentry.delete(0, END)
                nameentry.delete(0, END)
                addressentry.delete(0, END)
                phoneentry.delete(0, END)
                emailentry.delete(0, END)

            def updateopr():
                dbcon = sqlite3.connect("BUS MS")
                cursor = dbcon.execute("""UPDATE operator SET(name="{}",contact="{}",address="{}",email="{}") WHERE operator.id={};""".format(nameentry.get(), phoneentry.get(), addressentry.get(), emailentry.get(), int(oprentry.get())))
                #cursor = dbcon.execute("SELECT * FROM operator;")
                dbcon.commit()
                print(cursor.fetchall())
                dbcon.close()

                showinfo(
                    title="Operator Entry Update",
                    message="Operator Record updated successfully"
                )

                oprentry.delete(0, END)
                nameentry.delete(0, END)
                addressentry.delete(0, END)
                phoneentry.delete(0, END)
                emailentry.delete(0, END)

            Button(newoprframe, text="Add", font=('Montserrat Medium', 20), bg="Lime Green", fg="Black", cursor="hand2", command=addopr).pack(side=LEFT, pady=20, padx=(10, 10))
            Button(newoprframe, text="Edit", font=('Montserrat Medium', 20), bg="Lime Green", fg="Black", cursor="hand2", command=updateopr).pack(side=LEFT, pady=20, padx=(10, 10))

            def mv_home():
                newoprWin.destroy()
                newWin.deiconify()
            Button(newoprframe, image=home, cursor="hand2", command=mv_home).pack(side=LEFT, pady=20)

            def newoprWinclose_Handler():
                ansuser = askokcancel(
                    title="Closing Confirmation",
                    message="For exiting press Yes or No to return to menu",
                )
                if ansuser is True:
                    win.destroy()
                else:
                    print("User selected cancel")

            newoprWin.protocol("WM_DELETE_WINDOW", newoprWinclose_Handler)
            newoprframe.pack()

        def new_bus():
            adminWin.withdraw()
            newbusWin = Toplevel(adminWin)
            newbusWin.title("Bus Ticketing M.S.")
            newbusWin.geometry("%dx%d" % (width, height))
            newbusWin.configure(bg="white")

            newbusframe = Frame(newbusWin, bg="white")

            Label(newbusframe, image=new_logo).pack(pady=(30, 0))
            Label(newbusframe, text="Online Bus Booking System", font=('Montserrat ExtraBold', 30), bg="LightBlue", fg="Red").pack(pady=15)

            Label(newbusframe, text="Add Bus Details", font=('Montserrat Bold', 30), bg="White", fg="Lime Green").pack(pady=20)

            Label(newbusframe, text="Bus ID", font=('Montserrat Bold', 15), bg="White", fg="Black").pack(side=LEFT, pady=20)
            busidentry = Entry(newbusframe, width=10)
            busidentry.pack(side=LEFT, pady=20, padx=5)
            Label(newbusframe, text="Bus Type", font=('Montserrat Bold', 15), bg="White", fg="Black").pack(side=LEFT, pady=20)
            options = [
                "AC 2X2",
                "AC 3X2",
                "Non AC 2X2",
                "Non AC 3X2",
                "AC-Sleeper 2x1",
                "Non AC-Sleeper 2x1"
            ]
            clicked = StringVar()
            clicked.set("Select Bus Type")
            typeentry= OptionMenu(newbusframe, clicked, *options)
            typeentry.pack(side=LEFT, padx=(10, 20))
            Label(newbusframe, text="Capacity", font=('Montserrat Bold', 15), bg="White", fg="Black").pack(side=LEFT, pady=20, padx=5)
            capentry = Entry(newbusframe, width=10)
            capentry.pack(side=LEFT, pady=20, padx=5)
            Label(newbusframe, text="Fare(in Rs.)", font=('Montserrat Bold', 15), bg="White", fg="Black").pack(side=LEFT, pady=20, padx=5)
            fareentry = Entry(newbusframe, width=10)
            fareentry.pack(side=LEFT, pady=20, padx=5)
            Label(newbusframe, text="Operator ID", font=('Montserrat Bold', 15), bg="White", fg="Black").pack(side=LEFT, pady=20, padx=5)
            opidentry = Entry(newbusframe, width=10)
            opidentry.pack(side=LEFT, pady=20, padx=5)
            Label(newbusframe, text="Route ID", font=('Montserrat Bold', 15), bg="White", fg="Black").pack(side=LEFT, pady=20, padx=5)
            routeidentry = Entry(newbusframe, width=10)
            routeidentry.pack(side=LEFT, pady=20, padx=5)

            def addbus():
                dbcon = sqlite3.connect("BUS MS")
                cursor= dbcon.execute("""SELECT id FROM OPERATOR WHERE id={};""".format(int(busidentry.get())))
                output = cursor.fetchall()
                if len(output) == 0:
                    print("OPERATOR NOT FOUND!!")
                    showinfo(
                        title="ERROR",
                        message="OPERATOR NOT FOUND!!"
                    )

                else:
                    cursor = dbcon.execute("""INSERT INTO bus VALUES({},{},{},{});""".format(int(busidentry.get()), int(typeentry.get()), int(capentry.get()), int(opidentry.get())))
                    dbcon.commit()
                    print(cursor.fetchall())
                    cursor = dbcon.execute("""SELECT MAX(runid) FROM runs;""")
                    max_run= cursor.fetchall()
                    max_runint = int(max_run[0]) + 1
                    cursor = dbcon.execute("""INSERT INTO runs (runid,busid,routeid,fare) VALUES({},{},{},{});""".format(max_runint, int(busidentry.get()),  int(routeidentry.get()), int(fareentry.get())))
                    dbcon.commit()
                    print(cursor.fetchall())
                    # cursor = dbcon.execute("SELECT * FROM operator;")
                    dbcon.close()

                    showinfo(
                        title="Bus Entry Added",
                        message="Bus Record added successfully!!"
                    )


                busidentry.delete(0, END)
                capentry.delete(0, END)
                fareentry.delete(0, END)
                opidentry.delete(0, END)
                routeidentry.delete(0, END)

            def updatebus():
                dbcon = sqlite3.connect("BUS MS")
                cursor= dbcon.execute("""SELECT id FROM OPERATOR WHERE id={};""".format(int(busidentry.get())))
                output = cursor.fetchall()
                if len(output) == 0:
                    print("OPERATOR NOT FOUND!!")
                    showinfo(
                        title="ERROR",
                        message="OPERATOR NOT FOUND!!"
                    )

                else:
                    cursor = dbcon.execute("""UPDATE bus SET({},{},{}) WHERE bus.busid={};""".format(int(typeentry.get()), int(capentry.get()), int(opidentry.get()), int(busidentry.get())))
                    print(cursor.fetchall())
                    dbcon.commit()
                    dbcon.close()
                    showinfo(
                        title="Bus Entry Update",
                        message="Bus Record updated successfully"
                    )

                busidentry.delete(0, END)
                capentry.delete(0, END)
                fareentry.delete(0, END)
                opidentry.delete(0, END)
                routeidentry.delete(0, END)

            Button(newbusframe, text="Add Bus", font=('Montserrat Medium', 20), bg="Lime Green", fg="Black", cursor="hand2", command=addbus).pack(side=LEFT, pady=50, padx=(10, 10))
            Button(newbusframe, text="Edit Bus", font=('Montserrat Medium', 20), bg="Lime Green", fg="Black", cursor="hand2", command=updatebus).pack(side=LEFT, pady=50, padx=(10, 10))

            def mv_home():
                newbusWin.destroy()
                newWin.deiconify()

            Button(newbusframe, image=home, cursor="hand2", command=mv_home).pack(side=LEFT, pady=20)

            def newbusWinclose_Handler():
                ansuser = askokcancel(
                    title="Closing Confirmation",
                    message="For exiting press Yes or No to return to menu",
                )
                if ansuser is True:
                    win.destroy()
                else:
                    print("User selected cancel")

            newbusWin.protocol("WM_DELETE_WINDOW", newbusWinclose_Handler)
            newbusframe.pack()

        def new_route():
            adminWin.withdraw()
            newrouteWin = Toplevel(adminWin)
            newrouteWin.title("Bus Ticketing M.S.")
            newrouteWin.geometry("%dx%d" % (width, height))
            newrouteWin.configure(bg="white")

            newrouteframe = Frame(newrouteWin, bg="white")

            Label(newrouteframe, image=new_logo).pack(pady=(30, 0))
            Label(newrouteframe, text="Online Bus Booking System", font=('Montserrat ExtraBold', 30), bg="LightBlue", fg="Red").pack(pady=15)

            Label(newrouteframe, text="Add Bus Route Details", font=('Montserrat Bold', 30), bg="White", fg="Lime Green").pack(pady=20)
            Label(newrouteframe, text="Route ID", font=('Montserrat Bold', 20), bg="White", fg="Black").pack(side=LEFT, pady=40)
            routeidentry = Entry(newrouteframe, width=10)
            routeidentry.pack(side=LEFT, pady=40, padx=(5, 10))
            Label(newrouteframe, text="Station Name", font=('Montserrat Bold', 20), bg="White", fg="Black").pack(side=LEFT, pady=40)
            stationnameentry = Entry(newrouteframe, width=10)
            stationnameentry.pack(side=LEFT, pady=40, padx=(5, 10))
            Label(newrouteframe, text="Station ID", font=('Montserrat Bold', 20), bg="White", fg="Black").pack(side=LEFT, pady=40)
            stationidentry = Entry(newrouteframe, width=10)
            stationidentry.pack(side=LEFT, pady=40, padx=(5, 10))

            def addroute():
                dbcon = sqlite3.connect("BUS MS")
                cursor = dbcon.execute("""SELECT routeid FROM runs WHERE rid={};""".format(int(routeidentry.get())))
                output = cursor.fetchall()
                if len(output) == 0:
                    print("ROUTE NOT FOUND!!")
                    showinfo(
                        title="ERROR",
                        message="ROUTE NOT FOUND!!"
                    )

                else:
                    cursor = dbcon.execute("""INSERT INTO city VALUES({},"{}");""".format(int(stationidentry.get()), stationnameentry.get()))
                    print(cursor.fetchall())
                    dbcon.commit()
                    cursor = dbcon.execute("""SELECT max(cid) FROM city;""")
                    max_city = cursor.fetchall()
                    max_cities= int(max_city[0])
                    cursor = dbcon.execute("""SELECT cname FROM city;""")
                    cities = cursor.fetchall()
                    print(cities)
                    for i in range(max_cities-1):
                        if cities[i] != stationnameentry.get():
                            cursor = dbcon.execute("""INSERT INTO route VALUES({},"{}","{}");""".format(int(routeidentry.get()), cities[i], cities[i+1]))
                            print(cursor.fetchall())
                            dbcon.commit()

                    dbcon.close()
                    showinfo(
                        title="Route Entry Added",
                        message="Route Record added successfully!!"
                    )

                routeidentry.delete(0, END)
                stationnameentry.delete(0, END)
                stationidentry.delete(0, END)

            def deleteroute():
                dbcon = sqlite3.connect("BUS MS")
                cursor = dbcon.execute("""SELECT rid FROM route WHERE route.rid={};""".format(int(routeidentry.get())))
                output = cursor.fetchall()
                if len(output) == 0:
                    print("ROUTE NOT FOUND!!")
                    showinfo(
                        title="ERROR",
                        message="ROUTE NOT FOUND!!"
                    )

                else:
                    cursor = dbcon.execute("""DELETE FROM city WHERE cid={} AND cname="{}";""".format(int(stationidentry.get()), stationnameentry.get()))
                    print(cursor.fetchall())
                    dbcon.commit()
                    dbcon.close()
                    showinfo(
                        title="Bus Route Update",
                        message="Bus Route Deleted successfully"
                    )
                routeidentry.delete(0, END)
                stationnameentry.delete(0, END)
                stationidentry.delete(0, END)

            Button(newrouteframe, text="Add Route", font=('Montserrat Medium', 20), bg="Lime Green", fg="Black", cursor="hand2", command=addroute).pack(side=LEFT, pady=40, padx=(10, 10))
            Button(newrouteframe, text="Delete Route", font=('Montserrat Medium', 20), bg="Lime Green", fg="Red", cursor="hand2", command=deleteroute).pack(side=LEFT, pady=40, padx=(10, 10))

            def mv_home():
                newrouteWin.destroy()
                newWin.deiconify()

            Button(newrouteframe, image=home, cursor="hand2", command=mv_home).pack(side=LEFT, pady=40)

            def newrouteWinclose_Handler():
                ansuser = askokcancel(
                    title="Closing Confirmation",
                    message="For exiting press Yes or No to return to menu",
                )
                if ansuser is True:
                    win.destroy()
                else:
                    print("User selected cancel")

            newrouteWin.protocol("WM_DELETE_WINDOW", newrouteWinclose_Handler)
            newrouteframe.pack()

        def new_run():
            adminWin.withdraw()
            newrunWin = Toplevel(adminWin)
            newrunWin.title("Bus Ticketing M.S.")
            newrunWin.geometry("%dx%d" % (width, height))
            newrunWin.configure(bg="white")

            newrunframe = Frame(newrunWin, bg="white")

            Label(newrunframe, image=new_logo).pack(pady=(30, 0))
            Label(newrunframe, text="Online Bus Booking System", font=('Montserrat ExtraBold', 30), bg="LightBlue", fg="Red").pack(pady=15)
            Label(newrunframe, text="Add Bus Running Details", font=('Montserrat Bold', 30), bg="White", fg="Lime Green").pack(pady=30)
            Label(newrunframe, text="Bus ID", font=('Montserrat Bold', 20), bg="White", fg="Black").pack(side=LEFT, pady=50)
            busidentry = Entry(newrunframe, width=15)
            busidentry.pack(side=LEFT, pady=40, padx=(5, 10))
            Label(newrunframe, text="Runing Date", font=('Montserrat Bold', 20), bg="White", fg="Black").pack(side=LEFT, pady=50)
            runningdateentry = Entry(newrunframe, width=15)
            runningdateentry.pack(side=LEFT, pady=50, padx=(5, 10))
            Label(newrunframe, text="Seat(s) Available", font=('Montserrat Bold', 20), bg="White", fg="Black").pack(side=LEFT, pady=50)
            seatavbentry = Entry(newrunframe, width=15)
            seatavbentry.pack(side=LEFT, pady=50, padx=(5, 10))

            def addrun():
                dbcon = sqlite3.connect("BUS MS")
                cursor = dbcon.execute("""SELECT busid FROM bus WHERE busid={}""".format(int(busidentry.get())))
                output = cursor.fetchall()
                if len(output) == 0:
                    print("ROUTE OR BUS NOT FOUND!!")
                    showinfo(
                        title="ERROR",
                        message="BUS NOT FOUND!!"
                    )

                else:
                    cursor= dbcon.execute("""SELECT MAX(runid) FROM runs;""")
                    max_run = cursor.fetchall()
                    maxrunint = int(max_run[0]) + 1
                    cursor = dbcon.execute("""INSERT INTO runs(runid,busid,date,available) VALUES({},{},"{}",{});""".format(maxrunint, int(busidentry.get()), runningdateentry.get(), int(seatavbentry.get())))
                    print(cursor.fetchall())
                    dbcon.commit()
                    dbcon.close()

            def deleterun():
                showinfo(
                    title="Bus Run Update",
                    message="Bus Run updated successfully"
                )
                busidentry.delete(0, END)
                runningdateentry.delete(0, END)
                seatavbentry.delete(0, END)

            Button(newrunframe, text="Add Run", font=('Montserrat Medium', 20), bg="Lime Green", fg="Black", cursor="hand2", command=addrun).pack(side=LEFT, pady=50, padx=(10, 10))
            Button(newrunframe, text="Delete Run", font=('Montserrat Medium', 20), bg="Lime Green", fg="Red", cursor="hand2", command=deleterun).pack(side=LEFT, pady=50, padx=(10, 10))

            def mv_home():
                newrunWin.destroy()
                newWin.deiconify()

            Button(newrunframe, image=home, cursor="hand2", command=mv_home).pack(side=LEFT, pady=50)

            def newrunWinclose_Handler():
                ansuser = askokcancel(
                    title="Closing Confirmation",
                    message="For exiting press Yes or No to return to menu",
                )
                if ansuser is True:
                    win.destroy()
                else:
                    print("User selected cancel")

            newrunWin.protocol("WM_DELETE_WINDOW", newrunWinclose_Handler)
            newrunframe.pack()

        Button(adminframe, text="New Operator", font=('Montserrat Medium', 25), bg="lawn green", fg="Black", border=3, command=new_opr, cursor="hand2").pack(side=LEFT, padx=(0, 50), pady=40)
        Button(adminframe, text="New Bus", font=('Montserrat Medium', 25), bg="orange red", fg="Black", border=3, command=new_bus, cursor="hand2").pack(side=LEFT, padx=(50, 50), pady=40)
        Button(adminframe, text="New Route", font=('Montserrat Medium', 25), bg="SlateBlue2", fg="Black", border=3, command=new_route, cursor="hand2").pack(side=LEFT, padx=(50, 50), pady=40)
        Button(adminframe, text="New Run", font=('Montserrat Medium', 25), bg="DarkOrchid2", fg="Black", border=3, command=new_run, cursor="hand2").pack(side=LEFT, padx=(50, 0), pady=40)

        def adminWinclose_Handler():
            ansuser = askokcancel(
                title="Closing Confirmation",
                message="For exiting press Yes or No to return to menu",
            )
            if ansuser is True:
                win.destroy()
            else:
                print("User selected cancel")

        adminWin.protocol("WM_DELETE_WINDOW", adminWinclose_Handler)

        adminframe.pack()

    Button(newframe, text="Seat Booking", font=('Montserrat SemiBold', 23), bg="LightGreen", fg="Black", activebackground="SeaGreen", activeforeground="white", cursor="hand2", command=bus_book).pack(side=LEFT, padx=70, pady=(50, 0))
    Button(newframe, text="Checked Booked Seat", font=('Montserrat SemiBold', 23), bg="LightGreen", fg="Black", activebackground="SeaGreen", activeforeground="white", cursor="hand2", command=check_book).pack(side=LEFT, padx=70, pady=(50, 0))
    Button(newframe, text="Add Bus Details", font=('Montserrat SemiBold', 23), bg="Light Green", fg="Black", activebackground="Green", activeforeground="white", cursor="hand2", command=admin_ms).pack(side=LEFT, padx=70, pady=(50, 0))

    def newWinclose_Handler():
        ansuser = askokcancel(
            title="Closing Confirmation",
            message="For exiting press Yes or No to return to menu",
        )
        if ansuser is True:
            win.destroy()
        else:
            print("User selected cancel")

    newWin.protocol("WM_DELETE_WINDOW", newWinclose_Handler)
    newframe.pack()

    tagframe = Frame(newWin, bg="white")
    Label(tagframe, text="For Admins ONLY!!", font=('Montserrat Medium', 15), fg="red", bg="white").pack(padx=(900, 0), pady=(30, 0))
    tagframe.pack()


dbcon.close()
win.bind("<Key>", keypress)
win.mainloop()  # Start main eventloop
'''def main():'''
