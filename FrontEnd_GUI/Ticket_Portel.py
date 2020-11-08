from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk, messagebox
from PDF_Creator.text_to_pdf import Print_PDF as pdf
import datetime


def registration():
    messagebox.showinfo("Payment", "This is not any online method\nSkipping the payment, Here.")
    pdf(f"{Start_stn.get()}-{Desti_stn.get()} Express", Passenger_Name.get(), DoB.get(), Gender.get(), Address.get(), Aadhaar.get(), f"{datetime.datetime.now().strftime('%y%M%d%h%m%s')}", DoJ.get(), Start_stn.get(), Desti_stn.get(), "Confirmed", Coach.get(), Mobile.get(), Email_ID.get())
    messagebox.showinfo("Ticket", "Your ticket is here")


root = Tk()
root.title("Indian Railway Ticket Reservation Channel")
root.geometry("500x570")
root.minsize(500, 570)
root.maxsize(500, 570)
root.config(bg='cyan2')

Label(root, text="Indian Railways", font="Courier 20 bold italic underline", padx=15, pady=4, fg='thistle1', bg='turquoise3',).pack(anchor=N, side=TOP, padx=10, pady=8)
Label(root, text="Ticket Reservation Channel", font="Courier 18 bold italic underline", padx=16, pady=5, fg='thistle1', bg='turquoise3',).pack(anchor=N, side=TOP, padx=10, pady=1)


Frame1 = Frame(root, padx=4, pady=3 ,bg='lavender')

Label(Frame1, justify=LEFT,  text="Enter Passenger Name: ", font="Times 14 roman bold", bg='alice blue', padx=8, pady=2).grid(row=0, column=0, padx=2, pady=2)
Passenger_Name = Entry(Frame1, font="Times 12 italic")
Passenger_Name.grid(row=0, column=1)


Label(Frame1, justify=LEFT,  text="Enter Aadhaar Number: ", font="Times 14 roman bold", bg='alice blue', padx=5, pady=2).grid(row=1, column=0, padx=2, pady=2)
Aadhaar = Entry(Frame1, font="Times 12 italic")
Aadhaar.grid(row=1, column=1)


Label(Frame1, justify=LEFT,  text="Enter Date of Birth: ", font="Times 13 roman bold", bg='alice blue', padx=30, pady=2).grid(row=2, column=0, padx=2, pady=2)
DoB = DateEntry(Frame1, width=18, bg="darkblue", fg="white", font="Times 11 italic")
DoB.grid(row=2, column=1)


Label(Frame1, justify=LEFT,  text="Select gender: ", font="Times 13 roman bold", bg='alice blue', padx=52, pady=2).grid(row=3, column=0, pady=2)
Gender = StringVar()
sex = ttk.Combobox(Frame1, textvariable=Gender, state='readonly', width=24, height=25)
sex['values'] = ['Male', 'Female', 'Other']
sex.grid(row=3, column=1)


Label(Frame1, justify=LEFT,  text="Enter Mobile Number: ", font="Times 14 roman bold", bg='alice blue', padx=12, pady=2).grid(row=4, column=0, padx=2, pady=2)
Mobile = Entry(Frame1, font="Times 12 italic")
Mobile.grid(row=4, column=1)


Label(Frame1, justify=LEFT,  text="Enter Email-ID: ", font="Times 14 roman bold", bg='alice blue', padx=38, pady=2).grid(row=5, column=0, padx=2, pady=2)
Email_ID = Entry(Frame1, font="Times 12 italic")
Email_ID.grid(row=5, column=1)


Label(Frame1, justify=LEFT,  text="Enter Address: ", font="Times 14 roman bold", bg='alice blue', padx=43, pady=2).grid(row=6, column=0, padx=2, pady=2)
Address = Entry(Frame1, font="Times 12 italic")
Address.grid(row=6, column=1)


Label(Frame1, justify=LEFT,  text="Enter Date of Journey: ", font="Times 13 roman bold", bg='alice blue', padx=20, pady=2).grid(row=7, column=0, padx=2, pady=2)
DoJ = DateEntry(Frame1, width=18, bg="darkblue", fg="white", font="Times 11 italic")
DoJ.grid(row=7, column=1)


Label(Frame1, justify=LEFT,  text="Starting Station: ", font="Times 14 roman bold", bg='alice blue', padx=37, pady=2).grid(row=8, column=0, padx=2, pady=2)
Start_stn = StringVar()
Starting_Station = ttk.Combobox(Frame1, textvariable=Start_stn, state='readonly', width=24, height=25)
Starting_Station['values'] = ['New Delhi Station', 'Howrah Station', 'Mumbai Station', 'Chennai Station']
Starting_Station.grid(row=8, column=1)


Label(Frame1, justify=LEFT,  text="Destination Station: ", font="Times 14 roman bold", bg='alice blue', padx=24, pady=2).grid(row=9, column=0, padx=2, pady=2)
Desti_stn = StringVar()
Destination_Station = ttk.Combobox(Frame1, textvariable=Desti_stn, state='readonly', width=24, height=25)
Destination_Station['values'] = ['New Delhi Station', 'Howrah Station', 'Mumbai Station', 'Chennai Station']
Destination_Station.grid(row=9, column=1)


Label(Frame1, justify=LEFT,  text="Select Your Coach: ", font="Times 13 roman bold", bg='alice blue', padx=33, pady=2).grid(row=10, column=0, pady=2)
Coach = StringVar()
coach = ttk.Combobox(Frame1, textvariable=Coach, state='readonly', width=24, height=25)
coach['values'] = ['General', 'Sleeper', '1st AC', '2nd AC', '3rd AC']
coach.grid(row=10, column=1)

Frame1.pack(padx=10, pady=5, anchor=N)

Button(root, text="Book Now", command=registration, font="Arial 16 bold", bg='green2', fg='white', padx=17, pady=1, ).pack(side=TOP, anchor=N, fill=BOTH, padx=140, pady=10)


root.mainloop() 
